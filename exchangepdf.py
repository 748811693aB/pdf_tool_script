import PyPDF2

def replace_pdf_page(original_pdf_path, replacement_pdf_path, page_number, output_pdf_path):
    original_pdf = PyPDF2.PdfReader(open(original_pdf_path, 'rb'))
    replacement_pdf = PyPDF2.PdfReader(open(replacement_pdf_path, 'rb'))
    output_pdf = PyPDF2.PdfWriter()

    # for i in range(original_pdf.getNumPages()):
    for i in range(len(original_pdf.pages)):
        if i + 1 == page_number:
            # output_pdf.addPage(replacement_pdf.getPage(0))
            output_pdf.add_page(replacement_pdf.pages[0])
        else:
            # output_pdf.addPage(original_pdf.getPage(i))
            output_pdf.add_page(original_pdf.pages[i])
    with open(output_pdf_path, 'wb') as output_file:
        output_pdf.write(output_file)

# 替换操作示例
original_pdf_path = r'C:\Users\hxb971002\Desktop\tool_scripts\2023-08-14_112544.pdf'
replacement_pdf_path = r'C:\Users\hxb971002\Desktop\tool_scripts\single.pdf'
page_number_to_replace = 7  # 要替换的页面编号
output_pdf_path = 'output.pdf'

replace_pdf_page(original_pdf_path, replacement_pdf_path, page_number_to_replace, output_pdf_path)
