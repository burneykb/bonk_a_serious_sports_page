from flask import Blueprint, render_template, send_from_directory, request, current_app
import os
from natsort import natsorted
from collections import defaultdict
from .pdf_utils import get_pdf_list, search_pdfs

main = Blueprint('main', __name__)

def group_pdfs_by_directory(pdfs):
    grouped = defaultdict(list)
    for pdf in pdfs:
        parts = pdf.split('/', 1)
        if len(parts) == 2:
            grouped[parts[0]].append(parts[1])
        else:
            grouped[''].append(parts[0])
    return dict(grouped)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/ass')
def ass():
    # A Serious Sports (ASS)
    pdfs = get_pdf_list(current_app.config['PDF_FOLDER'])
    natsorted_pdfs = natsorted(pdfs)
    grouped_pdfs = group_pdfs_by_directory(natsorted_pdfs)
    return render_template('ass.html', grouped_pdfs=grouped_pdfs)

@main.route('/pdf/<path:filename>')
def view_pdf(filename):
    return send_from_directory(current_app.config['PDF_FOLDER'], filename)

@main.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = search_pdfs(current_app.config['PDF_FOLDER'], query)
    grouped_results = group_pdfs_by_directory(results)
    return render_template('ass.html', grouped_pdfs=grouped_results, query=query)