# Smart Web Scraper with Flask

A simple yet powerful web scraping tool built with Flask, Bootstrap, and BeautifulSoup. Enter any valid URL, and it will display the page's title, headings, meta description, top links, top images, word count, page size, and more — with an option to download the data as JSON.
## Features

- Scrapes title, headings, and meta description
- Extracts  links
- Displays  images
- Word count and page size in KB
- Checks robots.txt for scraping permission
- Export scraped data as downloadable JSON
- Responsive UI using Bootstrap 5


## Tech Stack

- Python 3.9+
- Flask
- BeautifulSoup (bs4)
- Bootstrap 5

- Requests


## Installation

```bash
git clone https://github.com/Selvam-DG/Python-Projects.git
cd smart-web-scraper

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


```
    
## Run Locally



```bash
  python app.py
```
Then open your browser and go to:


```bash
  http://127.0.0.1:5000
```



## License

[MIT](https://choosealicense.com/licenses/mit/)

