import os
import time
from datetime import datetime

# 遍历当前目录及子目录下的所有 .md 文件
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            # 获取文件名（不含后缀）作为 title
            title = os.path.splitext(file)[0].replace("-", " ").title()
            # 获取文件创建时间（Windows 用 st_ctime，Linux/macOS 用 st_birthtime）
            try:
                # 适用于 Linux/macOS
                create_time = os.stat(file_path).st_birthtime
            except AttributeError:
                # 适用于 Windows
                create_time = os.stat(file_path).st_ctime
            # 格式化时间为 Hugo 支持的格式（如 2024-08-20T15:30:00+08:00）
            date_str = datetime.fromtimestamp(create_time).strftime("%Y-%m-%dT%H:%M:%S%z")

            # 读取原文件内容
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 检查是否已有 Front Matter，避免重复添加
            if not content.startswith("---"):
                # 构建 Front Matter
                front_matter = f"---\ntitle: \"{title}\"\ndate: {date_str}\ndraft: false\n---\n\n"
                # 写入新内容（Front Matter + 原内容）
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(front_matter + content)
                print(f"已处理：{file_path}")
            else:
                print(f"已存在 Front Matter，跳过：{file_path}")