import pypdf
import sys

fname = 'EVALUACIÓN MODULAR 6.pdf'
try:
    reader = pypdf.PdfReader(fname)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

for i, page in enumerate(reader.pages):
    print(f'--- PÁGINA {i+1} ---')
    text = page.extract_text()
    print(text)
    print()
