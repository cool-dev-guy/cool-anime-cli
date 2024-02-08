import cloudscraper
import re
def get(url):
    scraper = cloudscraper.create_scraper()
    resp = scraper.get(url)
    pattern = r'sources: \[\{file:"(.*?)"\}\]'
    matches = re.findall(pattern, resp.text)
    return matches[0]
