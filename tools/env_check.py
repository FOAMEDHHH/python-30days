#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""环境自检：验证 30 天学习所需环境是否就绪

用法:
    .venv/Scripts/python.exe tools/env_check.py
"""
import importlib
import os
import sys


def section(title):
    print("\n=== %s ===" % title)


def check_imports():
    section("1. 依赖检查")
    pkgs = ["numpy", "pandas", "matplotlib", "seaborn", "openpyxl", "requests", "httpx",
            "dotenv", "openai", "tiktoken", "fastapi", "uvicorn", "pydantic", "sqlalchemy",
            "bcrypt", "jwt", "pypdf", "multipart", "pytest", "black", "ruff"]
    failed = []
    for name in pkgs:
        try:
            m = importlib.import_module(name)
            print("  OK    %-12s %s" % (name, getattr(m, "__version__", "-")))
        except Exception as e:
            failed.append(name)
            print("  FAIL  %-12s %s" % (name, e))
    return failed


def check_pandas():
    section("2. pandas 冒烟测试（Day 16-18 用到的 API）")
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({
        "地区": ["华东", "华北", "华东", "华南"],
        "品类": ["A", "B", "A", "C"],
        "销售额": [100, 200, 300, 400],
        "日期": ["2026-01-05", "2026-01-06", "2026-02-05", "2026-02-06"],
    })
    print("  shape:", df.shape)
    print("  groupby+agg:\n" + df.groupby("地区")["销售额"].agg(["sum", "mean", "count"]).to_string())
    print("  pivot_table:\n" + df.pivot_table(index="地区", columns="品类",
                                          values="销售额", aggfunc="sum", fill_value=0).to_string())
    df["日期"] = pd.to_datetime(df["日期"])
    print("  resample(月):\n" + df.set_index("日期")["销售额"].resample("ME").sum().to_string())
    df["利润率"] = df["销售额"].apply(lambda x: x * 0.1)
    print("  apply:", df["利润率"].tolist())
    print("  value_counts(normalize):", df["地区"].value_counts(normalize=True).round(2).to_dict())
    print("  merge 后行数:", len(df.merge(pd.DataFrame({"地区": ["华东"]}), on="地区", how="inner")))
    df.drop(columns=["利润率"])
    print("  drop 是否返回副本（原列还在）:", "利润率" in df.columns)
    print("  df.append 是否存在:", hasattr(df, "append"), "（pandas 2.0 起已移除）")
    print("  pandas", pd.__version__, "| numpy", np.__version__)


def check_numpy():
    section("3. numpy 冒烟测试（Day 15）")
    import numpy as np
    a = np.arange(12).reshape(3, 4)
    print("  数组 shape:", a.shape)
    print("  广播 (3,1)+(1,4):\n", a[:, :1] + a[:1, :])
    print("  布尔索引 a[a>6]:", a[a > 6])
    print("  聚合 mean/std/max:", a.mean().round(2), a.std().round(2), a.max())


def check_web():
    section("4. FastAPI 冒烟测试（Day 22）")
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()

    @app.get("/ping")
    def ping():
        return {"ok": True}

    c = TestClient(app)
    r = c.get("/ping")
    print("  GET /ping ->", r.status_code, r.json())
    print("  自动文档 /docs 可用:", c.get("/docs").status_code == 200)


def check_plot():
    section("5. matplotlib 中文字体（Day 19）")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    names = {f.name for f in font_manager.fontManager.ttflist}
    print("  Microsoft YaHei 可用:", "Microsoft YaHei" in names)
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
    plt.rcParams["axes.unicode_minus"] = False
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_title("中文标题测试")
    ax.plot([1, 2, 3], [1, 4, 2])
    os.makedirs("output", exist_ok=True)
    fig.savefig("output/_env_check.png", dpi=100)
    plt.close(fig)
    print("  已生成 output/_env_check.png")


def check_db_security():
    section("6. SQLAlchemy / bcrypt（Day 23-24）")
    from sqlalchemy import Column, Integer, String, create_engine
    from sqlalchemy.orm import declarative_base, sessionmaker
    Base = declarative_base()

    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True)
        name = Column(String(50))

    eng = create_engine("sqlite://")
    Base.metadata.create_all(eng)
    with sessionmaker(bind=eng)() as s:
        s.add(User(name="张三"))
        s.commit()
        print("  SQLAlchemy 查询:", s.query(User).first().name)
    import bcrypt
    h = bcrypt.hashpw(b"123456", bcrypt.gensalt())
    print("  bcrypt 哈希校验:", bcrypt.checkpw(b"123456", h))


def main():
    print("Python:", sys.version.split()[0], "| 解释器:", sys.executable)
    failed = check_imports()
    check_pandas()
    check_numpy()
    check_web()
    check_plot()
    check_db_security()
    print("\n" + "=" * 46)
    if failed:
        print("环境不完整，缺失: %s" % ", ".join(failed))
        print("修复: .venv/Scripts/python.exe -m pip install -r requirements.txt")
        sys.exit(1)
    print("环境全部就绪，可以开始 Day 01。")


if __name__ == "__main__":
    main()
