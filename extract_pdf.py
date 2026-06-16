import sys
try:
    import PyPDF2
    reader = PyPDF2.PdfReader('Funeral Service Programme- Nambaya Mulwanda Mwelwa (17.06.26).pdf')
    for page in reader.pages:
        text = page.extract_text()
        if text:
            print(text)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
