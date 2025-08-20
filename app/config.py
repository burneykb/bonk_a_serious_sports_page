import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PDF_FOLDER = os.path.join(BASE_DIR, 'static', 'pdfs')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit upload size to 16 MB
    ALLOWED_EXTENSIONS = {'pdf'}