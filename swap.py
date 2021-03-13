import PyPDF2

all_page_count = 148
swap_start_page = 2
swap_end_page = 147

file_path = 'example.pde'

source_pdf = open(file_path, 'rb')
source = PyPDF2.PdfFileReader(source_pdf, strict=False)

output = PyPDF2.PdfFileWriter()

for i in range(0, swap_start_page-1):
  output.addPage(source.getPage(i))

for i in range(swap_start_page-1, swap_end_page, 2):
  p1 = source.getPage(i)
  p2 = source.getPage(i+1)
  output.addPage(p2)
  output.addPage(p1)

for i in range(swap_end_page, all_page_count):
  output.addPage(source.getPage(i))

output_pdf = open('./swap.pdf', 'wb')
output.write(output_pdf)
output_pdf.close()