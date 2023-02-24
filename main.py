import PyPDF2

# PDF 파일 열기
pdf_file = open('example.pdf', 'rb')

# PyPDF2 라이브러리를 사용하여 PDF 파일 객체 생성
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# 페이지 수
num_pages = pdf_reader.numPages

# 각 페이지에서 텍스트 추출
for page in range(num_pages):
    page_obj = pdf_reader.getPage(page)
    print(page_obj.extractText())

# PDF 파일 닫기
pdf_file.close()
