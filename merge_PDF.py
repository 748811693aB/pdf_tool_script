

#新建文件夹，将两个要合并pdf放于其中
#无法自己设置合并顺序
import os
from PyPDF2 import PdfMerger


target_path = r'D:\pythonProject\pdf合并'  ## pdf目录文件
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]


file_merger = PdfMerger()
for pdf in pdf_lst:
    file_merger.append(pdf,import_outline=False)     # 合并pdf文件


file_merger.write(r"合并文件.pdf")

