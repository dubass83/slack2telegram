#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# bug-report: makssych@gmail.com

""" send message from slack to telegram """

import sys
import os
import re
import logging
import logging.handlers
import argparse
import slack
import telegram
from telegram.bot import Bot
from telegram.error import TelegramError, BadRequest


# Configure Slack
SLACK_TOKEN = os.environ['SLACK_TOKEN']
sc = slack.RTMClient(token=SLACK_TOKEN)
# Configure Telegram
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_TARGET = os.environ['TELEGRAM_TARGET']
telegram_bot = Bot(TELEGRAM_TOKEN)


class CustomFormatter(argparse.RawDescriptionHelpFormatter,
                      argparse.ArgumentDefaultsHelpFormatter,):
    pass


parser = argparse.ArgumentParser(description=sys.modules[__name__].__doc__,
                                 formatter_class=CustomFormatter,)
logger = logging.getLogger(os.path.splitext(os.path.basename(sys.argv[0]))[0])


def setup_logging(options):
    """Configure logging."""
    root = logging.getLogger('')
    root.setLevel(logging.WARNING)
    logger.setLevel(options.debug and logging.DEBUG or logging.INFO)
    if not options.silent:
        ch = logging.StreamHandler()
        ch.setFormatter(
            logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            ),
        )
        root.addHandler(ch)


def parse_args(args=sys.argv[1:]):
    """Parse arguments."""

    g = parser.add_mutually_exclusive_group()
    g.add_argument(
        '--debug', '-d', action='store_true',
        default=True,
        help='enable debugging',
    )
    g.add_argument(
        '--silent', '-s', action='store_true',
        default=False,
        help="don't log to console",
    )

    return parser.parse_args(args)


def get_options():
    """ main entrance """
    # try get options
    options = parse_args()
    setup_logging(options)

    return options


@slack.RTMClient.run_on(event='message')
def main(**payload):
    data = payload['data']
    logger.debug(data)
    try:
        if 'jira' in data['bot_profile']['name']:
            attachments = data['attachments']
            logger.debug(attachments)
            message = parse_atach(attachments)
            send_telegram(message)
    except KeyError:
        logger.error(data)


def parse_atach(attachments):
    message = {}

    message['user'] = "Jira-bot"
    message['channel'] = "callc_notification"

    first_line_link = attachments[0]['pretext']
    link = re.search('<(.+?\|(.+?))>', first_line_link)
    sub_str = "[{}]({})".format(link.group(2), link.group(1).split("|")[0])
    f_line = format(re.sub(r"<(.+?)>", sub_str, first_line_link))
    format_text = '{}\n[{}]({})\n{}'.format(f_line,
                                            attachments[0]['title'],
                                            attachments[0]['title_link'],
                                            attachments[0].get('text', " ")
                                            )

    message['text'] = format_text

    return message


def send_telegram(message):
    try:
        msg_string = '@{} posted to #`{}`:\n{}'.format(message['user'],
                                                       message['channel'],
                                                       message['text'])
        telegram_bot.sendMessage(TELEGRAM_TARGET,
                                 msg_string,
                                 parse_mode=telegram.ParseMode.MARKDOWN)
    except(TelegramError, BadRequest):
        logger.error('Could not send message with markdown format.')
        logger.error("Unexpected error:", sys.exc_info()[0])
        logger.debug('Try send message without formating')
        msg_string = '@{} posted to #`{}`:\n\n```{}```'.format(
                                                        message['user'],
                                                        message['channel'],
                                                        message['text']
                                                        )
        telegram_bot.sendMessage(TELEGRAM_TARGET,
                                 msg_string,
                                 parse_mode=telegram.ParseMode.MARKDOWN)


if __name__ == "__main__":
    options = get_options()
    sc.start()
