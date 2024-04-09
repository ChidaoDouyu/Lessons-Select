# 开源协议：
import time as t
import sys
import os

version = "v0.1.0-Alpha"
global first, last
# 事先声明：本程序由PYTHON初学者设计编写！


def choose2():
    global last
    last = input("请输入您的备选科目{化学生物(1),化学政治(2)，化学地理(3)，政治地理(4)，政治生物(5)，地理生物(6)，返回(C)}：")
    if last == "化学生物" or last == "1":
        last = "化学生物"
    elif last == "化学政治" or last == "2":
        last = "化学政治"
    elif last == "化学地理" or last == "3":
        last = "化学地理"
    elif last == "政治地理" or last == "4":
        last = "政治地理"
    elif last == "政治生物" or last == "5":
        last = "政治生物"
    elif last == "地理生物" or last == "6":
        last = "地理生物"
    elif last == "返回" or last == "C" or last == "c":
        culture()
    else:
        print("您输入的内容有误，请重新输入！")
        choose2()
    print("您选择的科目为：" + first + last)
    confirm = input("请确认您要选择的科目(输入您选择的科目或 I confirm ，不确认请输入任意其他内容并回车)：")
    if confirm == first + last or confirm == "I confirm":
        print("已记录，您选择的科目是：" + first + last + "\n选课程序已完成，感谢使用！@sky_Ming")
        stop()
    else:
        print("取消确认，下面开始重新选择！")
        choose2()


def choose():
    global first
    first = input("请输入您的首选科目{物理(1)/历史(2)}：")
    if first == "物理" or first == "1":
        first = "物理"
        choose2()
    elif first == "历史" or first == "2":
        first = "历史"
        choose2()
    else:
        print("您输入的内容有误，请重新输入！")
        choose()


def culture():
    print("下面开始文化，艺术体育选择！")
    i = input("如果您希望继续学习文化，请输入1，若不，请输入2：")
    if i == "2":
        print(
            "已记录，请联系相应的专科老师进行报名！\n音乐：乔妮娜12312341234\n体育：耿晋铎32143214321\n美术：卢老师18888888888\n信息：王教练0431-89787897")
        stop()
    elif i == "1":
        print("已记录，请选择你参加高考的科目！\n")
        choose()
    else:
        print("您输入的数字有误，请重新输入！\n")
        culture()


def stop():
    os.system("pause")
    sys.exit(0)
    # 可能在你眼里这两句没用，但别删，我菜


name = input("请输入您的姓名：")
print(name + "，你好！欢迎来到东北师大附中2022级选课程序. @sky_Ming " + version + "\n")
t.sleep(0.1)
culture()
