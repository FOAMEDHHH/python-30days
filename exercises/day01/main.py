"""Day 01 练习骨架 —— 自己先写，别看 solutions/

完成标准：7 个练习全部实现，运行时无报错
任务清单：每日任务清单-Day01-15.md -> Day 01
写不出来超过 15 分钟再看 solutions/day01_reference.py 对应函数
"""


# ---------- 练习 1：打印姓名、城市、目标 ----------
def ex1_print():
    # TODO: 用三条 print 分别输出你的姓名、城市、学习目标
    pass


# ---------- 练习 2：用 type() 查看类型 ----------
def ex2_types():
    # TODO: 打印 100 / 100.0 / "100" / True 的类型
    # 进阶：验证 True == 1、True + True 的结果
    pass


# ---------- 练习 3：声明 5 个变量并打印 ----------
def ex3_variables():
    # TODO: 姓名(str)、年龄(int)、身高(float)、是否学生(bool)、爱好(str)，全部打印
    pass


# ---------- 练习 4：input() 接收姓名和年龄 ----------
def ex4_input():
    # TODO: 用 input() 接收姓名和年龄，输出「你好XX，你今年X岁」
    # 坑：input() 返回字符串，做算术要先 int() 转换
    pass


# ---------- 练习 5：输入两个数字，输出四则运算 ----------
def ex5_calc():
    # TODO: 输出 和、差、积、商(/)、整除(//)、余数(%)、幂(**)
    pass


# ---------- 练习 6：不借助中间变量交换 a 和 b ----------
def ex6_swap():
    # TODO: 用元组解包交换 a、b 的值
    pass


# ---------- 练习 7：个人名片 ----------
def ex7_card():
    # TODO: 用格式化输出打印对齐的名片（姓名/职业/电话/邮箱）
    # 提示：%-10s 左对齐占 10 位，或用 f-string 的 :<10
    pass


def main():
    for fn in (ex1_print, ex2_types, ex3_variables, ex4_input, ex5_calc, ex6_swap, ex7_card):
        print("-" * 40)
        fn()
    print("-" * 40)
    print("Day 01 练习完成！别忘了实战产出 01_hello.py 和 notes/day01.md")


if __name__ == "__main__":
    main()
