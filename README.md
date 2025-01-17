# Web Crawler Search Engine

## Overview
This project is a web crawler and search engine that crawls a website, indexes its content, and provides a user-friendly search interface. The system uses the Whoosh library for indexing and Flask for the web interface.


- **Crawler**: Independently crawls and indexes web pages starting from a given URL.
- **Index**: Stores crawled content using the Whoosh library.
- **Query Parser**: Processes user queries to provide relevant search results.
- **User Interface**: Provides a professional, responsive frontend for searching and displaying results.
- **Analytics Dashboard**: Tracks and displays search term frequencies.

## Features
- **Search Filters**: Filter results by date and domain.
- **Pagination**: View results page by page.
- **Dark Mode**: Toggle between light and dark themes for better accessibility.
- **Analytics Dashboard**: Visualizes the frequency of search terms.
- **Responsive Design**: Optimized for both desktop and mobile devices.

- Crawls and parses all HTML pages from a starting URL.
- Builds an index with Whoosh for fast and efficient search.
- Supports search queries with filters (date range, domain).
- Pagination for large result sets.
- Dark mode and a modern, responsive user interface.

## Prerequisites
Before running the application, ensure you have the following installed:

## Requirements

- Python 3.x
- Flask
- Whoosh
- BeautifulSoup4
- Requests
- gunicorn

## Hints:
1- Use eduVPN to access of the server of the university to see the webpage


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/JUPA8/Web-Crawler-Search-Updated.git

   2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Setup
1. **Run the Crawler**:
   The crawler will index content from the specified URL in `crawler.py`.
   ```bash
   python crawler.py
   ```

2. **Start the Flask Application**:
   Launch the web server to interact with the search engine.
   ```bash
   python app.py
   ```

3. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:5000/`.

## Project Structure
```
├── app.py                # Backend logic for the Flask app
├── crawler.py            # Web crawler implementation
├── templates/            # HTML files for UI
│   ├── index.html        # Home page with search form
│   ├── results.html      # Search results display
│   ├── analytics.html    # Analytics dashboard
│   └── search.html       # Search interface
├── static/               # Static assets (CSS, JS)
├── README.md             # Project documentation
├── requirements.txt      # Dependencies
├── indexdir
├── reverse.wsgi
├── app.wsgi 
├── reverse.py
├── test.wsgi 
├── wsgi.py
├── __pycache__                        
```

## Testing
1. Test the following functionalities:
   - Search queries with and without filters.
   - Analytics dashboard for search term frequency.
   - Pagination and dark mode.
2. Verify that the application works across multiple devices and screen sizes.


## Code Structure
- `crawler.py`: Contains the logic for crawling and indexing.
- `app.py`: Implements the Flask application, indexing, and search functionality.
- `index.html`: Frontend template for the home page (search form).
- `results.html`: Frontend template for displaying search results.
- `search.html`: Template for handling search inputs and displaying output.
- `wsgi.app`: We run through it in the server to view our page.

The link that you can search with it in the server of the university: http://vm146.rz.uni-osnabrueck.de/u001/app.wsgi/

## Files: 
- All files are served in the public_html of the server which can have a virtual environment and is already activated. 

## Recommendation commands can use it through the terminal:

- ls: to see all files in the file directory.
- nano (file name): to see what is inside the file and you can write, read, and make any maintain through the file.



