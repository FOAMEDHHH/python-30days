#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Day 01 参考实现 —— 先自己写，再对照这里

对应: 每日任务清单-Day01-15.md -> Day 01
用法: python solutions/day01_reference.py

对照方法：
  1. 先自己在 exercises/day01/main.py 写 7 个练习（不查这里）
  2. 写不出来的再看对应函数
  3. 对比差异，把「你没想到的写法」抄进 notes/day01.md
"""


import sys


def _fix_stdout():
    """输出被重定向到管道时用 UTF-8，避免中文乱码；真实终端保持原编码。"""
    try:
        enc = (sys.stdout.encoding or "").lower().replace("-", "")
        if not sys.stdout.isatty() and enc != "utf8":
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


_fix_stdout()


# ---------- 练习 1：打印姓名、城市、目标 ----------
def ex1_print():
    print("姓名：张三")
    print("城市：杭州")
    print("目标：成为 AI 应用开发工程师")


# ---------- 练习 2：type() 查看类型 ----------
def ex2_types():
    print(type(100))      # <class 'int'>
    print(type(100.0))    # <class 'float'>
    print(type("100"))    # <class 'str'>
    print(type(True))     # <class 'bool'>
    print("True == 1 ?", True == 1)      # True（bool 是 int 的子类）
    print("True + True =", True + True)  # 2


# ---------- 练习 3：声明 5 个变量并打印 ----------
def ex3_variables():
    name = "张三"          # str
    age = 20               # int
    height = 1.78          # float
    is_student = True      # bool
    hobby = "编程"          # str

    print(name, age, height, is_student, hobby)
    print("类型:", type(name), type(age), type(height), type(is_student), type(hobby))
    Name = "张三"           # 与 name 是两个变量（Python 区分大小写）
    print("name =", name, "| Name =", Name)


# ---------- 练习 4：input() 接收姓名和年龄 ----------
def ex4_input(name=None, age=None):
    # 实际交互时用 input()；这里给默认值方便自动化运行
    if name is None:
        name = input("请输入你的姓名：")
    if age is None:
        age = input("请输入你的年龄：")
    print("你好，%s，你今年 %s 岁了" % (name, age))
    print("明年你就 %d 岁了" % (int(age) + 1))   # input 得到的必须转 int


# ---------- 练习 5：输入两个数字，输出四则运算 ----------
def ex5_calc(a=None, b=None):
    if a is None:
        a = int(input("第一个数："))
    if b is None:
        b = int(input("第二个数："))
    print("和 =", a + b)
    print("差 =", a - b)
    print("积 =", a * b)
    print("商 (/ 永远返回 float) =", a / b)
    print("整除 (// 去掉小数) =", a // b)
    print("余数 (%) =", a % b)
    print("幂 (**) =", a ** b)


# ---------- 练习 6：不借助中间变量交换 a 和 b ----------
def ex6_swap():
    a, b = 1, 2
    print("交换前: a =", a, "b =", b)
    a, b = b, a          # Python 元组解包交换
    print("交换后: a =", a, "b =", b)
    c, d = 3, 4          # 对比 C/Java 风格需要中间变量
    tmp = c
    c, d = d, tmp
    print("对比写法: c =", c, "d =", d)


# ---------- 练习 7：个人名片 ----------
def ex7_card():
    name = "张三"
    job = "AI 应用开发工程师"
    phone = "138-0000-0000"
    email = "zhangsan@example.com"

    print("=" * 40)
    print("| 姓名：%-10s|" % name)     # %-10s 左对齐占 10 位
    print("| 职业：%-10s|" % job)
    print("| 电话：%-10s|" % phone)
    print("| 邮箱：%-10s|" % email)
    print("=" * 40)
    print(f"| 姓名：{name:<10}|")        # f-string 等价写法（推荐）
    print(f"| 职业：{job:<10}|")


def main():
    print("=" * 50)
    print("Day 01 参考实现")
    print("=" * 50)
    demos = [
        ("练习 1：打印姓名、城市、目标", ex1_print),
        ("练习 2：type() 查看类型", ex2_types),
        ("练习 3：声明 5 个变量并打印", ex3_variables),
    ]
    for title, fn in demos:
        print("\n" + "-" * 50)
        print(">>> %s" % title)
        print("-" * 50)
        fn()
    # 练习 4、5 涉及 input()，此处传固定值演示；自己写时请用 input()
    print("\n" + "-" * 50)
    print(">>> 练习 4：input() 接收姓名和年龄")
    print("-" * 50)
    ex4_input("张三", 20)
    print("\n" + "-" * 50)
    print(">>> 练习 5：四则运算")
    print("-" * 50)
    ex5_calc(17, 5)
    print("\n" + "-" * 50)
    print(">>> 练习 6：变量交换")
    print("-" * 50)
    ex6_swap()
    print("\n" + "-" * 50)
    print(">>> 练习 7：个人名片")
    print("-" * 50)
    ex7_card()


if __name__ == "__main__":
    main()
