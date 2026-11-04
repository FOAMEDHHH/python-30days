# Python 30 天学习计划（每日 2 小时）

> 总投入 60 小时 ｜ 起点：零基础 ｜ 目标：AI 应用开发工程师方向

## 文件导航

| 文件 | 内容 |
|---|---|
| `学习计划.md` | 总目标、30 天总览表、每周验收、三个项目、纪律清单 |
| `每日任务清单-Day01-15.md` | 前 15 天逐日任务：知识点 / 练习 / 实战产出 / 验收 / 坑 |
| `每日任务清单-Day16-30.md` | 后 15 天逐日任务 + 项目三落地 + 30 道面试题 + 错误速查 |
| `requirements.txt` | 全程需要的依赖 |
| `notes/` | 每天一个学习笔记（用 `notes/笔记模板.md` 起头） |

## 快速开始（Day 0）

```powershell
cd d:/代码库/python-30days
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## 目录规划（按需手动创建）

```
python-30days/
├── notes/          # 每日笔记 notes/day01.md ...
├── exercises/      # 每日练习 exercises/day01/main.py ...
├── projects/
│   ├── p1_cli_assistant/    # Day 07
│   ├── p2_data_analysis/    # Day 19
│   └── p3_rag_chatbot/      # Day 25-29（主打项目）
├── output/         # 图表输出
├── .env            # API Key（不要提交 Git）
├── .venv/
└── 学习计划.md
```

## 每天怎么用

1. 打开 `学习计划.md` 找到当天的 Day 编号
2. 打开对应的 `每日任务清单-*.md`，按「知识点 → 练习 → 实战产出 → 验收」执行
3. 代码写进 `exercises/dayXX/`，笔记写进 `notes/dayXX.md`
4. 每天结束：`git add . && git commit -m "dayXX: 完成 XXX"`

## 学习纪律

- 看教程 ≤ 25 分钟，敲代码 ≥ 60 分钟
- 每天必须 git commit（错代码也提交）
- 卡住超 15 分钟就查资料，不死磕
- 每个知识点当天必须用一次

## 30 天后

产出：3 个项目（1 个已上线）+ 30 篇笔记 + 技能自评 + 90 天进阶路线图（见 Day 30 任务清单）
