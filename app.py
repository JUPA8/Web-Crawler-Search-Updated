from flask import Flask, render_template, request, redirect, url_for
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os
import shutil
from datetime import datetime
from collections import Counter
from math import ceil
from crawler import Crawler

app = Flask(__name__)
app.static_folder = 'static'

# Setup Whoosh schema and index
def setup_index():
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True), domain=TEXT(stored=True), date=TEXT(stored=True))
    index_dir = "indexdir"

    if os.path.exists(index_dir):
        shutil.rmtree(index_dir)
    os.mkdir(index_dir)

    idx = create_in(index_dir, schema)
    return idx

index = setup_index()

# Initialize crawler
crawler = Crawler('https://vm009.rz.uos.de/crawl/index.html')
crawler.crawl()

# Index crawled data
def index_data():
    writer = index.writer()
    for word, data in crawler.index.items():
        for entry in data:
            if isinstance(entry, dict) and all(key in entry for key in ['title', 'url', 'snippet', 'domain', 'date']):
                writer.add_document(
                    title=entry['title'],
                    path=entry['url'],
                    content=entry['snippet'],
                    domain=entry['domain'],
                    date=entry['date']
                )
            else:
                print(f"Skipping entry due to missing keys or incorrect format: {entry}")
    writer.commit()

index_data()

# Store search history and analytics
search_history = []
search_analytics = Counter()

# Search frequency tracker
search_frequency = Counter()

@app.route('/')
def home():
    return render_template('index.html', history=search_history)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    date_from = request.args.get('date_from', '')
    date_to = request.args.get('date_to', '')
    domain = request.args.get('domain', '')
    page = int(request.args.get('page', 1))  # Pagination

    if not query:
        return redirect(url_for('home'))

    # Record search query
    search_history.append(query)
    search_analytics[query] += 1
    search_frequency[query] += 1  # Increment search frequency

    # Perform the search
    searcher = index.searcher()
    query_parser = QueryParser("content", index.schema)
    parsed_query = query_parser.parse(query)
    results = searcher.search(parsed_query, limit=None)

    # Apply filters
    filtered_results = []
    for hit in results:
        if domain and domain not in hit.get('domain', ''):
            continue
        if date_from and datetime.strptime(hit.get('date', '2000-01-01'), '%Y-%m-%d') < datetime.strptime(date_from, '%Y-%m-%d'):
            continue
        if date_to and datetime.strptime(hit.get('date', '2100-01-01'), '%Y-%m-%d') > datetime.strptime(date_to, '%Y-%m-%d'):
            continue
        filtered_results.append({
            "url": hit.get('path', 'No URL'),
            "title": hit.get('title', 'No Title'),
            "snippet": highlight_terms(hit.get('content', 'No content available'), query),
            "domain": hit.get('domain', 'Unknown Domain'),
            "date": hit.get('date', 'Unknown Date')
        })

    # Pagination
    results_per_page = 10
    total_results = len(filtered_results)
    total_pages = ceil(total_results / results_per_page)
    start = (page - 1) * results_per_page
    end = start + results_per_page
    paginated_results = filtered_results[start:end]

    return render_template(
        'results.html',
        results=paginated_results,
        query=query,
        total_results=total_results,
        page=page,
        total_pages=total_pages,
        frequency=search_frequency
    )

@app.route('/analytics')
def analytics():
    # Display search analytics as a list of terms and their counts
    sorted_frequency = dict(sorted(search_frequency.items(), key=lambda x: x[1], reverse=True))
    return render_template('analytics.html', frequency=sorted_frequency)

def highlight_terms(text, query):
    """Highlight search terms in the snippet."""
    terms = query.split()
    for term in terms:
        text = text.replace(term, f"<mark>{term}</mark>")
    return text

if __name__ == '__main__':
    app.run(debug=True)
