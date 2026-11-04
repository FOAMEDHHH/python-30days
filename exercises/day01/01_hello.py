"""Day 01 实战产出骨架 —— 个人信息卡

需求：接收姓名、年龄、Python 学习目标，输出一张排版整齐的名片
提示：%-22s 左对齐占位；f-string 写法更直观
"""
import sys


def _fix_stdout():
    try:
        enc = (sys.stdout.encoding or "").lower().replace("-", "")
        if not sys.stdout.isatty() and enc != "utf8":
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


_fix_stdout()

WIDTH = 42


def build_card(name, age, goal):
    """根据三个信息拼出名片文本"""
    line = "=" * WIDTH
    # TODO: 用格式化输出拼出 姓名/年龄/学习目标/进度 四行
    return line


def main():
    print("=== Day 01 实战：个人信息卡 ===\n")
    # TODO: 用 input() 接收三个输入，并用 or 给空值兜底
    name = ""
    age = ""
    goal = ""
    print()
    print(build_card(name, age, goal))


if __name__ == "__main__":
    main()
