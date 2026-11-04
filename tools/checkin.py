#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""学习打卡脚本：记录每日学习时长，自动生成周报。

用法:
    python tools/checkin.py init [--start YYYY-MM-DD] [--day N]   # 初始化 + 创建目录/笔记
    python tools/checkin.py start [--force]                       # 开始计时
    python tools/checkin.py stop [--note "一句话总结"]              # 结束计时并记录
    python tools/checkin.py status                               # 当前状态
    python tools/checkin.py show [--days 7]                      # 最近 N 天
    python tools/checkin.py report [--week N] [--all]             # 生成周报
数据文件: notes/checkin.json
"""
import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timedelta


def _fix_stdout():
    """输出被重定向到管道时强制 UTF-8，避免中文乱码；真实终端保持原编码。"""
    try:
        enc = (sys.stdout.encoding or "").lower().replace("-", "")
        if not sys.stdout.isatty() and enc != "utf8":
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


_fix_stdout()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(ROOT, "notes")
EXERCISES_DIR = os.path.join(ROOT, "exercises")
LOG_PATH = os.path.join(NOTES_DIR, "checkin.json")
TEMPLATE = os.path.join(NOTES_DIR, "笔记模板.md")
TARGET = 120          # 每日目标分钟数
BAR_W = 20            # 进度条宽度


def load():
    if os.path.exists(LOG_PATH):
        try:
            with open(LOG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("! checkin.json 损坏，已重置")
    return {"version": 1, "start_date": None, "records": {}, "current": None}


def save(d):
    os.makedirs(NOTES_DIR, exist_ok=True)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)


def pdate(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


def today():
    return datetime.now().strftime("%Y-%m-%d")


def day_no(d, date_obj):
    if not d.get("start_date"):
        return None
    n = (date_obj - pdate(d["start_date"])).days + 1
    return n if n >= 1 else None      # 起始日之前不显示 Day 编号


def label(n):
    return "Day %02d" % n if n else "-"


def code_exists(n):
    p = os.path.join(EXERCISES_DIR, "day%02d" % n)
    if not n or not os.path.isdir(p):
        return False
    for _, _, fs in os.walk(p):
        if any(f.endswith(".py") for f in fs):
            return True
    return False


def note_exists(n):
    p = os.path.join(NOTES_DIR, "day%02d.md" % n)
    return bool(n) and os.path.exists(p) and os.path.getsize(p) > 300


def bar(minutes):
    """终端进度条（纯 ASCII，避免 GBK 控制台无法输出方块字符）"""
    ratio = min(1.0, minutes / TARGET)
    fill = int(round(ratio * BAR_W))
    return "[%s%s]%4d%%" % ("#" * fill, "-" * (BAR_W - fill), int(ratio * 100))


def cmd_init(a):
    d = load()
    dirty = False
    if a.start:
        d["start_date"] = a.start
        dirty = True
        print("[i] 起始日 = %s" % a.start)
    elif not d.get("start_date"):
        d["start_date"] = today()
        dirty = True
        print("[i] 起始日 = 今天 %s（Day 1）" % d["start_date"])
    n = a.day or day_no(d, datetime.now().date()) or 1
    dd = os.path.join(EXERCISES_DIR, "day%02d" % n)
    os.makedirs(dd, exist_ok=True)
    gk = os.path.join(dd, ".gitkeep")
    if not os.path.exists(gk):
        open(gk, "w", encoding="utf-8").close()
    np = os.path.join(NOTES_DIR, "day%02d.md" % n)
    if not os.path.exists(np) and os.path.exists(TEMPLATE):
        shutil.copyfile(TEMPLATE, np)
    if dirty:
        save(d)
    print("[√] %s -> %s" % (label(n), dd.replace(ROOT + os.sep, "")))
    print("[√] 笔记 -> %s" % np.replace(ROOT + os.sep, ""))
    print("    下一步: python tools/checkin.py start")


def cmd_start(a):
    d = load()
    if d.get("current") and not a.force:
        print("[!] 已有计时（%s 开始），先 stop 或加 --force" % d["current"]["start"])
        return
    now = datetime.now()
    d["current"] = {"start": now.isoformat(timespec="seconds"), "date": now.strftime("%Y-%m-%d")}
    save(d)
    print("[√] 开始计时 %s，结束后运行 stop" % now.strftime("%H:%M:%S"))


def cmd_stop(a):
    d = load()
    cur = d.get("current")
    if not cur:
        print("[!] 没有进行中的计时，先运行 start")
        return
    now = datetime.now()
    mins = max(1, int(round((now - datetime.fromisoformat(cur["start"])).total_seconds() / 60)))
    rec = d["records"].setdefault(cur["date"], {"minutes": 0, "sessions": [], "note": ""})
    rec["minutes"] += mins
    rec["sessions"].append({"start": cur["start"], "end": now.isoformat(timespec="seconds"), "minutes": mins})
    if a.note:
        rec["note"] = a.note
    d["current"] = None
    save(d)
    print("[√] 本次 %d 分钟，当日累计 %d 分钟" % (mins, rec["minutes"]))
    print("    建议: python tools/checkin.py report")


def cmd_status(a):
    d = load()
    rec = d["records"].get(today(), {"minutes": 0, "note": ""})
    print("起始日 %s ｜ 今天 %s" % (d.get("start_date") or "未设置", label(day_no(d, datetime.now().date()))))
    if d.get("current"):
        p = int((datetime.now() - datetime.fromisoformat(d["current"]["start"])).total_seconds() // 60)
        print("计时中：已 %d 分钟" % p)
    else:
        print("计时中：无")
    print("今日累计：%d 分钟 / 目标 %d 分钟 %s" % (rec["minutes"], TARGET, bar(rec["minutes"])))
    if rec.get("note"):
        print("今日备注：%s" % rec["note"])


def cmd_show(a):
    d = load()
    print("%-9s %-11s %9s  %s" % ("Day", "日期", "时长", "进度"))
    print("-" * 60)
    for i in range(a.days):
        dt = datetime.now().date() - timedelta(days=a.days - 1 - i)
        rec = d["records"].get(dt.strftime("%Y-%m-%d"), {"minutes": 0})
        print("%-9s %-11s %5dh%02dm  %s" % (label(day_no(d, dt)), dt.strftime("%m-%d"),
                                            rec["minutes"] // 60, rec["minutes"] % 60, bar(rec["minutes"])))
    tot = sum(d["records"].get((datetime.now().date() - timedelta(days=i)).strftime("%Y-%m-%d"),
                                {}).get("minutes", 0) for i in range(a.days))
    print("-" * 60)
    print("最近 %d 天累计：%d 小时 %d 分钟" % (a.days, tot // 60, tot % 60))


def week_of(dt):
    mon = dt - timedelta(days=dt.weekday())
    return mon, mon + timedelta(days=6)


def rel_week(d, mon):
    if not d.get("start_date"):
        return 1
    sm, _ = week_of(pdate(d["start_date"]))
    return (mon - sm).days // 7 + 1


def build_report(d, mon, sun, idx):
    L = []
    L.append("# 学习周报 · 第 %d 周" % idx)
    L.append("")
    L.append("> 生成时间 %s ｜ 起始日 %s（Day 1）｜ 每日目标 2 小时"
             % (datetime.now().strftime("%Y-%m-%d %H:%M"), d.get("start_date") or "未设置"))
    L.append("")
    L.append("## 一、总览")
    L.append("")
    L.append("| 指标 | 数值 |")
    L.append("|---|---|")
    total = days = codes = notes = 0
    rows = []
    for i in range(7):
        dt = mon + timedelta(days=i)
        rec = d["records"].get(dt.strftime("%Y-%m-%d"), {"minutes": 0, "note": ""})
        m = rec.get("minutes", 0)
        n = day_no(d, dt)
        c, nt = code_exists(n), note_exists(n)
        total += m
        days += 1 if m > 0 else 0
        codes += 1 if c else 0
        notes += 1 if nt else 0
        rows.append((n, dt, m, c, nt, rec.get("note", "")))
    tgt = TARGET * 7
    L.append("| 累计学习时长 | %d 小时 %d 分钟 |" % (total // 60, total % 60))
    L.append("| 本周目标 | %d 小时 |" % (tgt // 60))
    L.append("| 完成率 | %d%% |" % (int(round(total / tgt * 100)) if tgt else 0))
    L.append("| 有效学习天数 | %d / 7 |" % days)
    L.append("| 有代码产出 | %d / 7 |" % codes)
    L.append("| 有笔记 | %d / 7 |" % notes)
    L.append("")
    L.append("## 二、每日明细")
    L.append("")
    L.append("| Day | 日期 | 时长 | 完成度 | 代码 | 笔记 | 备注 |")
    L.append("|---|---|---|---|---|---|---|")
    for n, dt, m, c, nt, note in rows:
        L.append("| %s | %s | %dh%02dm | %d%% | %s | %s | %s |"
                 % (label(n), dt.strftime("%m-%d"), m // 60, m % 60,
                    int(round(m / TARGET * 100)), "有" if c else "-", "有" if nt else "-",
                    (note or "").replace("|", "/")[:40]))
    L.append("")
    L.append("## 三、时长分布")
    L.append("")
    for n, dt, m, c, nt, _ in rows:
        if m or c or nt:
            b = "█" * int(m / TARGET * BAR_W)
            L.append("- %s (%s)：%s %dh%02dm" % (label(n), dt.strftime("%m-%d"), b.ljust(BAR_W), m // 60, m % 60))
    L.append("")
    L.append("## 四、本周问题与改进")
    L.append("")
    L.append("- 卡住超过 15 分钟才查资料的问题：")
    L.append("- 计划未完成的原因：")
    L.append("- 下周要改的一个动作：")
    L.append("")
    L.append("## 五、下周目标")
    L.append("")
    L.append("- [ ] 达成 14 小时总量")
    L.append("- [ ] 每天笔记当天写完（不补）")
    L.append("- [ ] 完成上周未完成的实战产出")
    L.append("")
    return "\n".join(L)


def cmd_report(a):
    d = load()
    if not d.get("start_date"):
        print("[!] 请先运行: python tools/checkin.py init")
        return
    if a.all:
        mons = {week_of(pdate(k))[0] for k in d["records"]}
        for mon in sorted(mons):
            idx = rel_week(d, mon)
            p = os.path.join(NOTES_DIR, "周报-W%02d.md" % idx)
            with open(p, "w", encoding="utf-8") as f:
                f.write(build_report(d, mon, mon + timedelta(days=6), idx))
            print("[√] %s" % p.replace(ROOT + os.sep, ""))
        return
    if a.week:
        sm, _ = week_of(pdate(d["start_date"]))
        mon = sm + timedelta(days=7 * (a.week - 1))
    else:
        mon, _ = week_of(datetime.now().date())
    idx = rel_week(d, mon)
    p = os.path.join(NOTES_DIR, "周报-W%02d.md" % idx)
    with open(p, "w", encoding="utf-8") as f:
        f.write(build_report(d, mon, mon + timedelta(days=6), idx))
    print("[√] 周报: %s" % p.replace(ROOT + os.sep, ""))
    print("    区间: %s ~ %s" % (mon, mon + timedelta(days=6)))


def main():
    ap = argparse.ArgumentParser(description="学习打卡与周报生成器", epilog=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("init", help="初始化")
    p.add_argument("--start"); p.add_argument("--day", type=int); p.set_defaults(f=cmd_init)
    p = sub.add_parser("start", help="开始计时")
    p.add_argument("--force", action="store_true"); p.set_defaults(f=cmd_start)
    p = sub.add_parser("stop", help="结束计时")
    p.add_argument("--note"); p.set_defaults(f=cmd_stop)
    sub.add_parser("status", help="查看状态").set_defaults(f=cmd_status)
    p = sub.add_parser("show", help="最近 N 天")
    p.add_argument("--days", type=int, default=7); p.set_defaults(f=cmd_show)
    p = sub.add_parser("report", help="生成周报")
    p.add_argument("--week", type=int); p.add_argument("--all", action="store_true")
    p.set_defaults(f=cmd_report)
    a = ap.parse_args()
    if not getattr(a, "f", None):
        ap.print_help()
        return
    a.f(a)


if __name__ == "__main__":
    main()
