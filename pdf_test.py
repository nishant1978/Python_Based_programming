import PyPDF2

with open('prestige.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    print(page)
    page.rotate(90)
    print(page)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open('prestige.pdf', 'wb') as writefile:
        writer.write(writefile)
        new_page = writer.pages[0]
        print(new_page)