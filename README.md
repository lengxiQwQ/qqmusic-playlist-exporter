## QQ音乐歌单导出工具

一个简单的命令行脚本，用于抓取 QQ音乐 歌单信息并导出为常见格式。

作者：`lengxiQwQ`

---

### 功能简述

- 支持通过歌单链接或歌单 ID 输入；

- 支持导出格式：`.xlsx`、`.csv`、`.json`、`.txt`；

- 文件名使用歌单名称，自动替换 Windows 不允许的字符；

- 导出完成后（在 Windows）会自动打开文件所在目录并选中文件；

- 交互式循环：导出完成后可继续输入新的歌单，输入 `0`  /  `q`  /  `quit`  /  `exit` 退出程序。

  ---

### 文件列表

- `qq_music_playlist_export.py` — 主脚本（交互式）
- `README.md` — 使用说明（本文件）
- `requirements.txt` — Python 依赖
- `LICENSE` — MIT 许可证
- `.gitignore` — 忽略文件

---

### 依赖

在终端中安装所有依赖：

```bash
pip install -r requirements.txt
```

或者只安装必要依赖：

```bash
# 必须
pip install requests

# 导出 xlsx 所需
pip install openpyxl
```

---

### 使用方法

下载或克隆本仓库到本地，在命令行或 Python 解释器中运行：
```bash
python qq_music_playlist_export.py
```

粘贴 y.qq.com 的歌单链接或直接输入 歌单ID 后按照提示操作。

##### 示例：
```python
============ QQ音乐歌单导出工具 ============
请输入歌单链接 或 歌单ID（输入 0 退出）：9044196528

已获取到 琴心月满 的歌单：
名称：中文民谣、流行，共 632 首歌曲
==========================================
请选择导出格式：
 1) .xlsx  - (默认) Excel 文件
 2) .csv   - 标准 CSV utf-8-sig
 3) .json  - JSON 文件，数组
 4) .txt   - 纯文本格式
==========================================
选择 (1 - 4，输入 0 退出程序)：4

已保存为: 中文民谣、流行 - 琴心月满.txt

# （Windows 会自动打开文件路径）
```

### 常见问题（FAQ / 排错）

- **导出 xlsx 时报错 `ModuleNotFoundError: No module named 'openpyxl'`**
   → 终端运行 `pip install openpyxl`。
- **抓取歌单失败或返回空列表**
   → 可能是网络问题或 QQ 音乐接口变化。尝试稍后重试或检查输入的歌单链接/ID。
- **文件名包含特殊字符导致保存失败**
   → 脚本会自动替换 Windows 不允许的字符为空格；若仍出错请检查是否有权限或路径过长问题。

------

### 贡献 & 许可

欢迎提交 issue 或 pull request。
 本仓库采用 MIT 许可证，详见 `LICENSE` 文件。作者：`lengxiQwQ`。
