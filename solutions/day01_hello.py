#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Day 01 实战产出：个人信息卡（参考实现）
自己的版本请写到 exercises/day01/01_hello.py
"""

import sys


def _fix_stdout():
    """输出被重定向到管道时用 UTF-8，避免中文乱码。"""
    try:
        enc = (sys.stdout.encoding or "").lower().replace("-", "")
        if not sys.stdout.isatty() and enc != "utf8":
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


_fix_stdout()

WIDTH = 42


def build_card(name, age, goal):
    line = "=" * WIDTH
    lines = [
        line,
        "| 姓名     : %-22s|" % name,
        "| 年龄     : %-22s|" % age,
        "| 学习目标 : %-22s|" % goal,
        "| 进度     : %-22s|" % "Day 01 / 30",
        line,
    ]
    return "\n".join(lines)


def main():
    print("=== Day 01 实战：个人信息卡 ===\n")
    name = input("请输入你的姓名：").strip() or "未填写"
    age = input("请输入你的年龄：").strip() or "未填写"
    goal = input("请输入你的 Python 学习目标：").strip() or "成为 AI 应用开发工程师"
    print()
    print(build_card(name, age, goal))


if __name__ == "__main__":
    main()
