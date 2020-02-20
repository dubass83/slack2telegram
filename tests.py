#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# bug-report: makssych@gmail.com

import pytest
from bot import parse_atach


testdata = [
    (
        [
            {
                "fallback": "New comment added to Task <https://jira.com/WEB-627|WEB-627> by Ringo Star",
                "text": "19.02 с этой карты были поплнения на счет ид 55531 и\xa0587782\n15.02 на счет ид\xa05853232 (под бонус)",
                "pretext": "New comment added to Task <https://jira.com/WEB-627|WEB-627> by Ringo Star",
                "title": "Найти аккаунт ",
                "id": 1,
                "title_link": "https://jira.com/WEB-627?focusedCommentId=44127",
                "color": "205081",
                "mrkdwn_in": ["text"]
            }
        ],
        {
            'user': 'Jira-bot',
            'channel': 'callc_notification',
            'text': 'New comment added to Task [WEB-627](https://jira.com/WEB-627) by Ringo Star\n[Найти аккаунт ](https://jira.com/WEB-627?focusedCommentId=44127)\n19.02 с этой карты были поплнения на счет ид 55531 и\xa0587782\n15.02 на счет ид\xa05853232 (под бонус)'
        }
    ),
    (
        [
           {
               "fallback": "New comment added to Task <https://jira.com/WEB-627|WEB-627> by Jhon Lennon",
               "text": "Просто текст небольшой текст",
               "pretext": "New comment added to Task <https://jira.com/WEB-627|WEB-627> by Jhon Lennon",
               "title": "Найти аккаунт ",
               "id": 1,
               "title_link": "https://jira.com/WEB-627?focusedCommentId=44127",
               "color": "205081",
               "mrkdwn_in": ["text"]
            }
        ],
        {
            'user': 'Jira-bot',
            'channel': 'callc_notification',
            'text': 'New comment added to Task [WEB-627](https://jira.com/WEB-627) by Jhon Lennon\n[Найти аккаунт ](https://jira.com/WEB-627?focusedCommentId=44127)\nПросто текст небольшой текст'
        }
    ),
    (
        [
            {
                "fallback": "New comment added to Task <https://jira.com/WEB-627|WEB-627> by Kurt Cobein",
                "text": "Функция будет вызвана из значения каждого элемента из параметризации. Поскольку параметризация представляет собой список объектов Task, id_func() будет вызываться с объектом Task, что позволяет нам использовать методы доступа namedtuple для доступа к одному объекту Task для генерации идентификатора одного объекта Task за раз. Это немного чище, чем генерировать полный список раньше времени, и выглядит одинаково:",
                "pretext": "New comment added to Task <https://jira.com/WEB-627|WEB-627> by Kurt Cobein",
                "title": "Найти аккаунт ",
                "id": 1,
                "title_link": "https://jira.com/WEB-627?focusedCommentId=44127", 
                "color": "205081",
                "mrkdwn_in": ["text"]
            }
        ],
        {
            'user': 'Jira-bot',
            'channel': 'callc_notification',
            'text': 'New comment added to Task [WEB-627](https://jira.com/WEB-627) by Kurt Cobein\n[Найти аккаунт ](https://jira.com/WEB-627?focusedCommentId=44127)\nФункция будет вызвана из значения каждого элемента из параметризации. Поскольку параметризация представляет собой список объектов Task, id_func() будет вызываться с объектом Task, что позволяет нам использовать методы доступа namedtuple для доступа к одному объекту Task для генерации идентификатора одного объекта Task за раз. Это немного чище, чем генерировать полный список раньше времени, и выглядит одинаково:'
        }
    )
]


@pytest.mark.parametrize("a,expected", testdata)
def test_parse(a, expected):
    """test_parse sample atachments."""
    # GIVEN testdata with sample atachments
    # WHEN parse atachments
    # THEN expected == parse_atach(a)
    assert expected == parse_atach(a)


if __name__ == "__main__":
    for sample in testdata:
        print(parse_atach(sample[0]))
