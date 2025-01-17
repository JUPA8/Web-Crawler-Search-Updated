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


---

## **Key Components**

### 1. **`app.py`**
This is the main file containing the Flask application logic. It:
- Sets up the Whoosh search engine index.
- Executes the web crawler to fetch and index data.
- Provides routes for:
  - `/app`: Displays the search page.
  - `/search`: Displays search results.
  - `/analytics`: Displays analytics on searched terms.

### 2. **`crawler.py`**
Implements the web crawler that:
- Fetches pages starting from a given URL.
- Extracts data such as title, URL, content, domain, and date.
- Saves the extracted data to the Whoosh index.

### 3. **`templates/`**
Contains the frontend templates rendered by Flask:
- `index.html`: Search form.
- `results.html`: Displays search results.
- `analytics.html`: Displays search analytics.

### 4. **`static/`**
Stores static assets like CSS and JavaScript files.

### 5. **`requirements.txt`**
Specifies the Python dependencies for the project.

### 6. **Deployment Scripts**
- `app.wsgi`: WSGI script for deployment.
- `reverse.wsgi`: WSGI script for a standalone reverse string app.
- `test.wsgi`: Testing script for the server.

---

## **How It Works**

### **1. Web Crawling**
The `crawler.py` script crawls the specified domain, extracts data, and stores it in the Whoosh index.

### **2. Search Functionality**
Users can:
1. Enter a query on the `/app` page.
2. View search results on `/search`.
3. Filter results by date or domain.

### **3. Analytics**
Tracks and displays frequently searched terms on the `/analytics` page.

---


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
   ```

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
├── indexdir              # Directory for storing Whoosh search engine index.
├── reverse.wsgi          # WSGI script for the standalone reverse application.
├── app.wsgi              # Main WSGI script for deploying the primary Flask application.
├── reverse.py            # A standalone Flask application for reversing strings.
├── test.wsgi             # Test WSGI script for debugging server configurations.
├── wsgi.py               # Alternate WSGI script for deploying the Flask application.
├── __pycache__           # Directory for Python’s compiled bytecode.              
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


## Web Crawler Search Interface

### Search Page
![Search Page](images/screenshot_search_page.png)

### Search Results
![Search Results](images/screenshot_search_results.png)


## Server information and also how to use it through terminal:

- Firstly open the vpn and access to server university.
- enter in the terminal ssh u001@vm146.rz.uni-osnabrueck.de.
- Enter Password to enter the server.
- go to file directory public_html.
- check files by instructions that provided above..
- you can see the webpage under this link: http://vm146.rz.uni-osnabrueck.de/u001/app.wsgi/



 ## **I ALSO ADDED Zip File which corrected and maintained. you can download and start with the project if you face some bugs or error. Called (sea1.zip)**
