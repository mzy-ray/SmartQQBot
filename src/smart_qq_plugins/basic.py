# -*- coding: utf-8 -*-
import random

from smart_qq_bot.logger import logger
from smart_qq_bot.signals import (
    on_all_message,
    on_group_message,
    on_private_message,
    on_discuss_message,
)

# =====唤出插件=====

# 机器人连续回复相同消息时可能会出现
# 服务器响应成功,但实际并没有发送成功的现象
# 所以尝试通过随机后缀来尽量避免这一问题
REPLY_SUFFIX = (
    '~',
    '!',
    '?',
)

REPLY_CUTE = (
    "干嘛？(,,•́ . •̀,,)",
    "ヾ(^▽^*)在哦在哦～",
    "嗷！(✧◡✧)",
    "嘿嘿嘿～(⁎⁍̴̛ᴗ⁍̴̛⁎)",
    "安排上了(๑¯◡¯๑)੭",
    "不，要，碰，我，(￢_￢)"
)


@on_all_message(name='basic[callout]')
def callout(msg, bot):
    if "上海人形" == msg.content:
        reply = bot.reply_msg(msg, return_function=True)
        logger.info("RUNTIMELOG " + str(msg.from_uin) + " calling me out, trying to reply....")
        reply_content = "有何吩咐" + random.choice(REPLY_SUFFIX)
        reply(reply_content)

@on_all_message(name='basic[callcute]')
def callcute(msg, bot):
    if "@上海人形" in msg.content and "摸" in msg.content :
        reply = bot.reply_msg(msg, return_function=True)
        logger.info("RUNTIMELOG " + str(msg.from_uin) + " calling me out, trying to reply....")
        reply_content = random.choice(REPLY_CUTE)
        reply(reply_content)


# =====复读插件=====
class Recorder(object):
    def __init__(self):
        self.last_msg = ""
        self.last_reply = ""

recorder = Recorder()

@on_group_message(name='basic[repeat]')
def repeat(msg, bot):
    global recorder
    reply = bot.reply_msg(msg, return_function=True)

    if recorder.last_msg == msg.content and recorder.last_reply != msg.content \
            and "@" not in msg.content and "d" not in msg.content and "timer" not in msg.content:
        if str(msg.content).strip() not in ("", " ", "[图片]", "[表情]"):
            logger.info("RUNTIMELOG " + str(msg.group_code) + " repeating, trying to reply " + str(msg.content))
            reply(msg.content)
            recorder.last_reply = msg.content
    recorder.last_msg = msg.content

@on_discuss_message(name='basic[repeat]')
def repeat(msg, bot):
    global recorder
    reply = bot.reply_msg(msg, return_function=True)

    if recorder.last_msg == msg.content and recorder.last_reply != msg.content and "@" not in msg.content:
        if str(msg.content).strip() not in ("", " ", "[图片]", "[表情]"):
            logger.info("RUNTIMELOG " + str(msg.did) + " repeating, trying to reply " + str(msg.content))
            reply(msg.content)
            recorder.last_reply = msg.content
    recorder.last_msg = msg.content

# @on_group_message(name='basic[三个问题]')
# def nick_call(msg, bot):
#     if "我是谁" == msg.content:
#         bot.reply_msg(msg, "你是{}({})!".format(msg.src_sender_card or msg.src_sender_name, msg.src_sender_id))
#
#     elif "我在哪" == msg.content:
#         bot.reply_msg(msg, "你在{name}({id})!".format(name=msg.src_group_name, id=msg.src_group_id))
#
#     elif msg.content in ("我在干什么", "我在做什么"):
#         bot.reply_msg(msg, "你在调戏我!!")


# @on_discuss_message(name='basic[讨论组三个问题]')
# def discuss_three_questions(msg, bot):
#     if "我是谁" == msg.content:
#         bot.reply_msg(msg, "你是{}!".format(msg.src_sender_name))
#
#     elif "我在哪" == msg.content:
#         bot.reply_msg(msg, "你在{name}!".format(name=msg.src_discuss_name))
#
#     elif msg.content in ("我在干什么", "我在做什么"):
#         bot.reply_msg(msg, "你在调戏我!!")