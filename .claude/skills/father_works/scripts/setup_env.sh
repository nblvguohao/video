#!/usr/bin/env bash
# 准备解包、转换、绘图、出 docx、转 PDF 所需的全部依赖。
# 幂等，可重复运行。装好的跳过。
set -u

need() { command -v "$1" >/dev/null 2>&1; }
log()  { printf '  %-22s %s\n' "$1" "$2"; }

echo "== 检查依赖 =="

APT_PKGS=()
need unrar || need unrar-free || APT_PKGS+=(unrar-free)
need bsdtar                   || APT_PKGS+=(libarchive-tools)
need pdftotext                || APT_PKGS+=(poppler-utils)
need pandoc                   || APT_PKGS+=(pandoc)
need soffice                  || APT_PKGS+=(libreoffice-writer)
# 中文字体：缺了 LibreOffice 转 PDF 会把中文显示成方块
fc-list 2>/dev/null | grep -qi "wqy\|noto.*cjk\|zenhei" || APT_PKGS+=(fonts-wqy-zenhei fonts-wqy-microhei)

if [ ${#APT_PKGS[@]} -gt 0 ]; then
  echo "  apt 安装: ${APT_PKGS[*]}"
  apt-get update -qq 2>/dev/null | tail -1
  # libreoffice-writer 有时首次 install 会因索引过期失败，update 后重试一次
  apt-get install -y "${APT_PKGS[@]}" >/dev/null 2>&1 || {
    apt-get update -qq 2>/dev/null | tail -1
    apt-get install -y "${APT_PKGS[@]}" >/dev/null 2>&1
  }
fi

for c in unrar bsdtar pdftotext pandoc soffice; do
  need "$c" && log "$c" OK || log "$c" "缺失（该步骤需另寻替代）"
done

echo "== Python 包 =="
python3 - <<'EOF' 2>/dev/null || pip install -q numpy scipy matplotlib python-docx pdfplumber defusedxml 2>&1 | tail -1
import numpy, scipy, matplotlib, docx
EOF
python3 -c "import numpy,scipy,matplotlib,docx; print('  numpy/scipy/matplotlib/python-docx OK')" 2>/dev/null \
  || echo "  Python 包安装失败，请手动 pip install numpy scipy matplotlib python-docx"

echo "== Node 包 =="
# docx 包装在当前工作目录，供 build_docx.js require
if node -e "require('docx')" 2>/dev/null; then
  echo "  docx OK"
else
  npm install docx >/dev/null 2>&1 && echo "  docx 已安装" || echo "  docx 安装失败，请手动 npm install docx"
fi

echo
echo "提示：LibreOffice 首次转换可能因用户配置目录失败，转换时固定加上"
echo "      -env:UserInstallation=file:///tmp/lo_profile 可绕过。"
