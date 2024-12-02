# PDF Uploader

## Project Overview 
This project is a web application that allows users to upload, search, and view PDF documents. The backend handles file uploads and searches using Elasticsearch, while the frontend provides an interface for users to interact with the system.

## Features
- Upload PDF files.
- Search PDFs by content and titles.
- View search results with highlights.

## Prerequisites
**Backend**:
- Python 
- Django 
- Elasticsearch 

**Frontend**:
- React 
- Axios (for making API calls)
- Tailwind CSS

## Installation and Setup

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/parykhan-jameel/pdf-project.git

2. Create a virtual environment and activate it:
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the backend dependencies:
   ```bash
   pip install -r requirements.txt

4. Apply database migrations:
   ```bash
   python manage.py migrate

5. run the server
   ```bash
   python manage.py runserver


### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend

2. Install the frontend dependencies:
    ```bash
   npm install

3. Start the development server:
   ```bash
   npm start

##Usage
1. Open a web browser and navigate to `http://localhost:3000/` to access the frontend
2. Use the upload button to upload a PDF file.
3. Use the search bar to search for content or a title in the PDFs.
4. View the search results displayed on the page.

##API endpoints
* URL: http://127.0.0.1:8000/search/
* Method: GET
* Parameters:
    * query (string): The search term to find within PDF content.
    * title (string): The title of the PDF.
### Example:
    ```bash
    http://127.0.0.1:8000/search/?query=test&title=Test%20Title


