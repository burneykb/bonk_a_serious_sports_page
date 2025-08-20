import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PDF_FOLDER = os.path.join(BASE_DIR, 'app', 'static', 'pdfs')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit upload size to 16 MB
    ALLOWED_EXTENSIONS = {'pdf'}