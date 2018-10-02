# -*- coding: utf-8 -*-
import random
import re
import time
from smart_qq_bot.signals import on_all_message
from smart_qq_bot.signals import on_private_message

# killer = False
# poisoner = False

@on_all_message(name='DiceRoller[rolldice]')
def rolldice(msg, bot):
    cmd_roll = re.compile(r"roll\((.*)\)")
    if re.match(cmd_roll, msg.content):
        reply = bot.reply_msg(msg, return_function=True)
        reply_content = "输入格式不正确，请按照roll(1,6)输入。"
        parameters = re.compile(r"\((.*)\)").search(msg.content).group().strip("(").rstrip(")")
        nums = parameters.split(",")
        if len(nums) != 0 and nums[0].isdigit() and nums[1].isdigit() and nums[0] < nums[1]:
            lower_bound = int(nums[0])
            upper_bound = int(nums[1])
            result = random.randint(lower_bound, upper_bound)
            reply_content = "范围:(" + str(lower_bound) + "," + str(upper_bound) + ") 结果:" + str(result)
        reply(reply_content)

@on_all_message(name='DiceRoller[quickroll]')
def rolldice(msg, bot):
    # global killer
    # global poisoner
    cmd_roll = re.compile(r"^.{,2}d.{,4}$")
    if re.match(cmd_roll, msg.content):
        reply = bot.reply_msg(msg, return_function=True)
        reply_content = "输入格式不正确，请按照1d6输入。"
        nums = re.compile(r".*d.*").search(msg.content).group().split("d")
        if len(nums) != 0 and nums[0].isdigit() and nums[1].isdigit():
            num_dice = int(nums[0])
            upper_bound = int(nums[1])
            if num_dice < 10 and num_dice >= 1 and upper_bound < 9999 and upper_bound > 0:
                reply_content = ""
                for i in range(num_dice):
                    result = random.randint(1, upper_bound)


                    # if killer and num_dice == 1:
                    #     if upper_bound == 100:
                    #         result = random.randint(upper_bound-2, upper_bound)
                    #     elif upper_bound == 50:
                    #         result = random.randint(upper_bound-1, upper_bound)
                    #     elif upper_bound == 10:
                    #         result = upper_bound
                    #     if upper_bound != 100:
                    #         result = upper_bound
                    #     killer = False


                    reply_content += "范围:(1" + "," + str(upper_bound) + ") 结果:" + str(result) + "\n"
                reply_content = reply_content.strip()
            if num_dice == 1 and result == upper_bound:
                reply("ごめん～(^_^*)")
            if num_dice == 1 and result <= 3 and upper_bound >= 10:
                reply("打得不错～")
        reply(reply_content)


@on_all_message(name='DiceRoller[timer]')
def rolldice(msg, bot):
    cmd_roll = re.compile(r"^timer.{,2}$")
    if re.match(cmd_roll, msg.content):
        reply = bot.reply_msg(msg, return_function=True)
        reply_content = "输入格式不正确，请按照timer1输入。"
        nums = msg.content[5:]

        if len(nums) != 0 and nums.isnumeric():
            nums = int(nums)
            if nums < 10:
                seconds = nums * 60 -30
                reply("倒计时：" + str(nums) + "分钟")
                time.sleep(seconds)
                reply("倒计时：还剩30秒")
                time.sleep(20)
                reply("倒计时：还剩10秒")
                time.sleep(10)
                reply("倒计时：时间到！后面的行动都不算啦！")
            elif nums < 60:
                seconds = nums - 10
                reply("倒计时：" + str(nums) + "秒")
                time.sleep(seconds)
                reply("倒计时：还剩10秒")
                time.sleep(10)
                reply("倒计时：时间到！后面的行动都不算啦！")
            else:
                reply("倒计时：时间数值范围(0,60)")
        else:
            reply(reply_content)

# @on_private_message(name='killer')
# def turnonkiller(msg, bot):
#     global killer
#     global poisoner
#     reply = bot.reply_msg(msg, return_function=True)
#     if "kstart" == msg.content:
#         killer = True
#         reply("kstart")
#     elif "kstop" == msg.content:
#         killer = False
#         reply("stop")
#     elif "pstart" == msg.content:
#         poisoner = True
#         reply("pstart")
#     elif "pstop" == msg.content:
#         poisoner = False
#         reply("pstop")
