"""
init_summary_repo.py — 初始化总结库
当总结库目录不存在或索引文件缺失时运行。
"""
import os
import sys
from datetime import datetime

def init_summary_repo(base_dir: str = None):
    """初始化总结库目录结构和索引文件。"""
    if base_dir is None:
        # 默认路径
        base_dir = os.path.join(
            os.path.expanduser("~"),
            "project mangers",
            "Summary Skill"
        )

    summaries_dir = os.path.join(base_dir, "summaries")
    references_dir = os.path.join(base_dir, "references")
    index_file = os.path.join(references_dir, "file-index.md")
    template_file = os.path.join(references_dir, "summary-template.md")

    # 创建目录
    os.makedirs(summaries_dir, exist_ok=True)
    os.makedirs(references_dir, exist_ok=True)

    # 创建索引文件（如果不存在）
    if not os.path.exists(index_file):
        now = datetime.now().strftime("%Y-%m-%d")
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(f"""# ?? 工作总结库索引

> 此文件用于记录所有历史总结的元数据，便于检索和浏览。
> 每次新增总结后，请在下方追加一条记录。

---

| 序号 | 文件名 | 创建日期 | 关键词标签 | 关联项目简述 |
|------|--------|----------|------------|--------------|
| 1 |    |    |    |    |

---

*最后更新：{now}*
""")
        print(f"[OK] 索引文件已创建: {index_file}")

    # 创建模板文件（如果不存在）
    if not os.path.exists(template_file):
        with open(template_file, "w", encoding="utf-8") as f:
            f.write("# 工作经验总结模板\n\n> 使用说明：AI助手在生成总结时，请参照以下结构填写内容。\n\n")
        print(f"[OK] 模板文件已创建: {template_file}")

    print(f"[OK] 总结库初始化完成，目录: {summaries_dir}")
    return summaries_dir


if __name__ == "__main__":
    custom_path = sys.argv[1] if len(sys.argv) > 1 else None
    result = init_summary_repo(custom_path)
    print(f"总结库路径: {result}")
