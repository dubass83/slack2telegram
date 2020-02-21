# slack2telegram

Send jira message from slack to telegram

## usage:

1. Create [Slack token](https://api.slack.com/legacy/custom-integrations/legacy-tokens)
 and add slack-bot to chanel where Jira send message.
2. Create [Telegram bot](https://core.telegram.org/bots).
3. Find [chanel id](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id) where to post message from slack.
4. Run in terminal

```shell
$ git clone https://github.com/dubass83/slack2telegram.git && cd slack2telegram
$ docker build -t app .
$ docker run \
        -e "SLACK_TOKEN=Your_SLACK_TOKEN" \
        -e "TELEGRAM_TOKEN=Your_TELEGRAM_TOKEN" \
        -e "TELEGRAM_TARGET=Your_TELEGRAM_TARGET" \
        -d app  
```
