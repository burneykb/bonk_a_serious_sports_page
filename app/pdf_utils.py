def get_pdf_list(pdf_folder):
    import os
    pdf_files = []
    for root, _, files in os.walk(pdf_folder):
        for f in files:
            if f.endswith('.pdf'):
                rel_dir = os.path.relpath(root, pdf_folder)
                rel_file = os.path.join(rel_dir, f) if rel_dir != '.' else f
                pdf_files.append(rel_file)
    return pdf_files

def search_pdfs(pdf_folder, query):
    import os
    from pypdf import PdfReader

    results = []
    pdf_files = get_pdf_list(pdf_folder)

    print(f"found {len(pdf_files)} PDFs in {pdf_folder}")
    
    for pdf_file in pdf_files:
        if query.lower() in pdf_file.lower():
            results.append(pdf_file)
            continue

        pdf_path = os.path.join(pdf_folder, pdf_file)
        reader = PdfReader(pdf_path)
        text = ''
        
        for page in reader.pages:
            text += page.extract_text() or ''
        
        if query.lower() in text.lower():
            results.append(pdf_file)
    
    return results