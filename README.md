# DataSpider

轻量级爬虫框架 / 工具集，不限于爬取图书，目标是提供可扩展的抓取、解析、存储与调度能力，便于快速搭建各类爬虫工程并共享组件。

主要内容

- 核心爬取模块（可替换 HTTP 客户端/异步实现）
- 插件式解析器与持久化适配器（文件、数据库等）
- 简单调度与重试策略
- 示例/模板用于快速上手

快速开始

1. 推荐创建虚拟环境并安装依赖（若有 requirements.txt）：
   python -m venv .venv
   source .venv/bin/activate  # 或 Windows 下 .venv\Scripts\activate
   pip install -r requirements.txt

## 项目结构（已重构）

- src/ — 源代码
  - `src/web_insert.py` — 主爬虫模块（入口通过运行根目录的 `main.py`）
- data/ — 原始输入与抓取的数据（books.txt, douban.txt）
- output/ — 处理后的输出（如果有）
- requirements.txt — Python 依赖
- main.py — 项目新的命令行入口

运行示例（Windows PowerShell）:

1. 创建并激活虚拟环境：
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
2. 安装依赖：
   .\.venv\Scripts\pip install -r requirements.txt
3. 运行脚本：
   .\.venv\Scripts\python main.py --both

Unix/macOS 示例：

1. 创建并激活虚拟环境：
   python -m venv .venv
   source .venv/bin/activate
2. 安装依赖：
   pip install -r requirements.txt
3. 运行脚本：
   python main.py --both

使用示例

- 查看 examples/ 或 docs/ 下的示例脚本。
- 若项目中尚无示例，请参阅 docs/usage.md（可后续添加）。

贡献

- 欢迎提交 issue/PR。请先阅读 CONTRIBUTING.md 和 CODE_OF_CONDUCT.md。
- 代码风格、测试与文档优先。

许可

- 本项目默认 MIT 许可，详见 LICENSE 文件。

联系方式

- 在仓库 issue 中打开讨论，或在 CONTRIBUTING.md 中的联系邮箱报告问题。
