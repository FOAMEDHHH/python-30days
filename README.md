# Python 30 天学习计划（每日 2 小时）

> 总投入 60 小时 | 起点：零基础 | 目标：AI 应用开发工程师方向
> Day 1 = 2026-11-04

## 文件导航

| 文件 | 内容 |
|---|---|
| 学习计划.md | 总目标、30 天总览表、每周验收、三个项目、纪律清单 |
| 每日任务清单-Day01-15.md | 前 15 天逐日任务与验收 |
| 每日任务清单-Day16-30.md | 后 15 天任务 + 30 道面试题 + 错误速查 |
| tools/checkin.py | 打卡计时 + 自动生成周报 |
| solutions/ | 参考实现（Day 01 已提供） |
| exercises/day01..30/ | 每天的练习目录，骨架已生成 |
| notes/dayXX.md | 每日笔记（由 笔记模板.md 生成） |

## 环境状态

- Python 3.14.8 已就绪
- Git 2.56.0 已就绪（用户目录 AppData/Local/Programs/Git/cmd）
- 虚拟环境 `.venv` 已创建，依赖已全部安装
- 环境自检：`.venv/Scripts/python.exe tools/env_check.py`
- Git 身份已设置：FOAMEDHHH

## GitHub 仓库（已连接）

- 仓库地址：https://github.com/FOAMEDHHH/python-30days
- 本地 `origin` 已绑定，每天 `git push` 即同步
- 30 天后这就是你的**作品集首页**，HR 会点开看 commit 密度与代码风格

## 首次配置（已完成，仅供复现）

```
cd d:/代码库/python-30days
python -m venv .venv
pip install -r requirements.txt
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

激活虚拟环境：Git Bash 用 `source .venv/Scripts/activate`；
PowerShell 用 `cd .venv/Scripts` 再执行 `./activate`。

## 打卡工具

```
python tools/checkin.py init      # 初始化（已执行，Day 1 = 2026-11-04）
python tools/checkin.py start     # 开始计时
python tools/checkin.py stop      # 结束并记录，可加 --note "今日总结"
python tools/checkin.py status    # 当前状态与今日累计
python tools/checkin.py show      # 最近 7 天时长
python tools/checkin.py report    # 生成本周周报 notes/周报-W01.md
```

## 每日流程（2 小时）

1. `python tools/checkin.py start`
2. 打开 每日任务清单 找到当天的 Day
3. 在 `exercises/dayXX/` 写代码（先自己写，卡住超 15 分钟再看 solutions/）
4. 实战产出 + `notes/dayXX.md` 写笔记
5. `python tools/checkin.py stop --note "..."`
6. `git add -A` 然后 `git commit -m "dayXX: 完成 XXX"`

## Git 常用命令

```
git status
git add .
git commit -m "day01: 完成语法基础"
git log --oneline
git diff
```

## 学习纪律

- 看教程不超过 25 分钟，敲代码不少于 60 分钟
- 每天必须 commit（错代码也提交）
- 卡住超 15 分钟就查资料，不死磕
- 每个知识点当天必须用一次

## 30 天后

3 个项目（1 个已上线）+ 30 篇笔记 + 技能自评 + 90 天进阶路线（见 Day 30 任务清单）
