#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""concept-unpacker 自检脚本：生成/修改学习资料 HTML 后运行。

检查四项：
  1. 标签闭合与嵌套是否正确（html.parser）
  2. 目录锚点 href="#sN" 是否都有对应的 id
  3. 页面内的本地链接（相对文件名）是否存在
  4. 代码标识符是否混入中文（skill 强制：标识符一律英文）

用法：
    python lint_html.py <文件或目录> [<文件或目录> ...]
    # 目录会递归检查其中的 *.html

退出码：0 = 全部通过；1 = 有问题（详情打印在 stdout）。
"""
import os
import re
import sys
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}

# Windows 控制台默认 GBK，中文输出会乱码；这里强制 UTF-8
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


class HtmlLint(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.ids = set()
        self.hrefs = []
        self.img_srcs = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.add(d["id"])
        if tag == "a" and d.get("href"):
            self.hrefs.append(d["href"])
        if tag == "img":
            self.img_srcs.append(d.get("src", ""))
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append("多余的 </%s> 于第 %s 行" % (tag, self.getpos()[0]))
            return
        top, pos = self.stack.pop()
        if top != tag:
            self.errors.append(
                "标签错配：<%s>（第 %s 行）被 </%s>（第 %s 行）关闭"
                % (top, pos[0], tag, self.getpos()[0])
            )


def collect(targets):
    files = []
    for t in targets:
        if os.path.isdir(t):
            for root, _dirs, names in os.walk(t):
                for n in sorted(names):
                    if n.endswith((".html", ".htm")):
                        files.append(os.path.join(root, n))
        elif os.path.isfile(t):
            files.append(t)
        else:
            print("[跳过] 路径不存在：%s" % t)
    return files


def check(path):
    with open(path, encoding="utf-8") as f:
        src = f.read()
    p = HtmlLint()
    p.feed(src)
    p.close()

    problems = []
    pending = ["<%s> 第 %s 行" % (t, pos[0]) for t, pos in p.stack]
    if pending:
        problems.append("未闭合标签：%s" % ", ".join(pending))
    if p.errors:
        problems.append("闭合错误：%s" % "; ".join(p.errors))

    refs = set(re.findall(r'href="#([\w-]+)"', src))
    missing_anchor = sorted(refs - p.ids)
    if missing_anchor:
        problems.append("锚点缺失：%s" % ", ".join("#" + a for a in missing_anchor))

    base = os.path.dirname(os.path.abspath(path))
    local = []
    for h in p.hrefs:
        if h.startswith(("http://", "https://", "#", "mailto:", "tel:")):
            continue
        fname = h.split("#")[0]
        if fname and not os.path.exists(os.path.join(base, fname)):
            local.append(h)
    if local:
        problems.append("本地链接失效：%s" % ", ".join(sorted(set(local))))

    # 代码标识符混入中文：def/class 名、以及行首赋值的中文变量名
    cn_def = re.findall(
        r"\b(?:def|class)\s+([\w\u4e00-\u9fff]*[\u4e00-\u9fff][\w\u4e00-\u9fff]*)", src)
    cn_var = []
    for line in src.splitlines():
        m = re.match(r"^\s*([\u4e00-\u9fff][\w\u4e00-\u9fff]*)\s*=(.*)$", line)
        if not m:
            continue
        rest = m.group(2).strip()
        # 例外：pandas 命名聚合的列别名，形如 条数=("内容", "size")，属合法惯用法
        if re.match(r"^\(\s*[\"']", rest):
            continue
        cn_var.append(m.group(1))
    if cn_def or cn_var:
        problems.append("代码标识符含中文：def/class=%s 变量=%s"
                        % (cn_def or "无", cn_var or "无"))

    if p.img_srcs:
        problems.append("提示：本页有 %d 个 <img>，确认路径可用（否则会出现 404 图）"
                        % len(p.img_srcs))

    status = "OK" if not problems else "有问题"
    print("[%s] %s  （%d 行）" % (status, path, len(src.splitlines())))
    for x in problems:
        print("      - %s" % x)
    return not problems


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    files = collect(args)
    if not files:
        print("没有找到可检查的 HTML 文件")
        return 2
    ok = all(check(f) for f in files)
    print("\n结论：%s（共 %d 个文件）" % ("全部通过" if ok else "存在待修问题", len(files)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
