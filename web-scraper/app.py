from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import validators
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

app = Flask(__name__)

def is_scraping_allowed(url):
    try:
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        robots_url = f"{base}/robots.txt"
        rp = RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        return rp.can_fetch("*", url)
    except:
        return False

def extract_info(url):
    try:
        parsed = urlparse(url)
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        word_count = len(text.split())
        page_size_kb = round(len(response.content) / 1024, 2)

        # Extract Title
        title = soup.title.string if soup.title else "No Title Found"

        # Headers
        headers = []
        for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
            headers.append(h.get_text(strip=True))
        #Links
        links = []
        for a in soup.find_all('a', href=True):
            if a['href'].startswith("http"):
                links.append(a['href'])
        meta_desc= ""
        meta_tag = soup.find("meta", attrs={"name": "description"})
        meta_desc = meta_tag.get("content") if meta_tag else "No description found"
        #images
        images = []
        for img in soup.find_all('img', src=True):
            src = img.get("src")
            if src and src.startswith("http"):
                images.append(src)
        

        return {
            "domain": parsed.netloc,
            "word_count": word_count,
            "page_size_kb": page_size_kb,
            "title" : title,
            "headers" : headers,
            "links" : links,
            "meta_description": meta_desc,
            "images" : images
        }

    except Exception as e:
        return {"error" : str(e)}

@app.route("/", methods=['POST', "GET"])
def index():
    info = {}
    url = None
    allowed = False

    if request.method == "POST":
        url = request.form.get("url")
        
        if validators.url(url):
            allowed = is_scraping_allowed(url)
            if allowed:
                info = extract_info(url)
            else:
                info = {"error": "Scrapping not allowed by robots.txt"}
        else:
            info = {"error" : "Invalid URL. Please enter a proper address."}
    return render_template("index.html", info= info, url= url, allowed= allowed)

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")
    if validators.url(url):
        data = extract_info(url)
        return jsonify(data)
    return jsonify({"error": "Invalid URL"})


if __name__ == "__main__":
    app.run(debug=True)