import PyPDF4

# Abrir el archivo PDF original
with open("Rojas_Flores_Diana_Lidia.pdf", "rb") as file:
    pdf_reader = PyPDF4.PdfFileReader(file)
    
    # Crear un nuevo documento PDF
    pdf_writer = PyPDF4.PdfFileWriter()
    
    # Iterar sobre cada página del documento
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        
        # Determinar si la página es horizontal o vertical
        page_width = page.mediaBox.getWidth()
        page_height = page.mediaBox.getHeight()
        
        if page_width > page_height:
            # La página es horizontal, rotarla 90 grados en sentido horario
            page.rotateClockwise(270)
        
        # Agregar la página (original o rotada) al nuevo documento
        pdf_writer.addPage(page)
    
    # Copiar los bookmarks (tabla de contenidos) del documento original
    outline = pdf_reader.getOutlines()
    for bookmark in outline:
        # Obtener la referencia de página del marcador
        page_num = pdf_reader.getPageNumber(bookmark.page)
        
        # Agregar el marcador al nuevo documento
        pdf_writer.addBookmark(bookmark.title, page_num)
    
    # Guardar el nuevo documento PDF
    with open("output.pdf", "wb") as output_file:
        pdf_writer.write(output_file)