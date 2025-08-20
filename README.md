# flask-pdf-collection
This project is a Flask web application that hosts a collection of PDF documents. It allows users to view PDFs in their web browser and provides functionality for searching and enumerating through a structured folder of PDF files.

## Project Structure
```
flask-pdf-collection
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── pdf_utils.py
│   ├── static
│   │   └── style.css
│   ├── templates
│   │   ├── index.html
│   │   └── view_pdf.html
│   └── pdfs
├── requirements.txt
├── config.py
└── README.md
```

## Features
- List all available PDF documents.
- View individual PDF documents in the browser.
- Search through the PDFs based on metadata.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd flask-pdf-collection
   ```
3. (If not already done) Activate your virtual environment.
   ```
   python -m venv ./venv
   source ./venv/bin/activate
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration
- Update the `config.py` file to set the appropriate paths and settings for your environment.

## Running the Application
To run the application, use the following command:
```
flask run
```
Make sure to set the `FLASK_APP` environment variable to `app` before running the command.

## Usage
- Open your web browser and go to `http://127.0.0.1:5000` to access the application.
- Use the search functionality to find specific PDFs or browse through the list of available documents.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.