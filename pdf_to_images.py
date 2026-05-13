"""
将 PDF 文件的每一页拆分为 PNG 图片。

使用方法:
    python pdf_to_images.py /absolute/path/to/file.pdf
    python pdf_to_images.py /absolute/path/to/file.pdf --dpi 200

依赖:
    pip install PyMuPDF
"""

import argparse
import os
import sys
from pathlib import Path

import fitz  # PyMuPDF


def pdf_to_images(pdf_path: str, dpi: int = 400) -> Path:
    """
    将 PDF 的每一页转为 PNG 图片。

    参数:
        pdf_path: PDF 文件的绝对路径。
        dpi: 输出图片的 DPI（分辨率），默认 150。

    返回:
        保存图片的文件夹路径。
    """
    # 1. 校验输入路径
    pdf_path = os.path.abspath(pdf_path)
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"未找到 PDF 文件: {pdf_path}")
    if not pdf_path.lower().endswith(".pdf"):
        raise ValueError(f"不是 PDF 文件: {pdf_path}")

    # 2. 解析文件名（不带扩展名）和输出目录
    pdf_stem = Path(pdf_path).stem  # 去掉 .pdf 的文件名
    output_dir = Path.cwd() / pdf_stem  # 工作目录下的同名文件夹
    output_dir.mkdir(parents=True, exist_ok=True)

    # 3. 打开 PDF 并逐页导出为 PNG
    # PyMuPDF 默认 72 DPI,通过 zoom 矩阵提高分辨率
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)

    doc = fitz.open(pdf_path)
    try:
        total_pages = len(doc)
        print(f"PDF 共 {total_pages} 页,开始转换 (DPI={dpi})...")

        for page_index in range(total_pages):
            page = doc.load_page(page_index)
            pixmap = page.get_pixmap(matrix=matrix, alpha=False)

            # 命名规则: 页码_pdf文件名.png (页码从 1 开始)
            page_number = page_index + 1
            image_name = f"{page_number}_{pdf_stem}.png"
            image_path = output_dir / image_name

            pixmap.save(str(image_path))
            print(f"  [{page_number}/{total_pages}] 已保存: {image_name}")
    finally:
        doc.close()

    print(f"\n完成! 所有图片已保存至: {output_dir}")
    return output_dir


def main():
    parser = argparse.ArgumentParser(
        description="将 PDF 的每一页拆分为 PNG 图片,保存到工作目录下的同名文件夹中。"
    )
    parser.add_argument("pdf_path", help="PDF 文件的绝对路径")
    parser.add_argument(
        "--dpi",
        type=int,
        default=150,
        help="输出图片的 DPI (分辨率),默认 150。数值越大图片越清晰、文件越大。",
    )
    args = parser.parse_args()

    try:
        pdf_to_images(args.pdf_path, dpi=args.dpi)
    except (FileNotFoundError, ValueError) as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"处理失败: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
