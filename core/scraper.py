import requests
from bs4 import BeautifulSoup
import re
from core.text_to_speech import speak

# get a working full URL from a domain
def get_working_url(domain):
    prefixes = ["https://", "http://", "https://www.", "http://www."]
    for prefix in prefixes:
        url = prefix + domain
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return url
        except:
            continue
    return None

# scrape content from the homepage
def scrape_homepage(domain):
    full_url = get_working_url(domain)
    if not full_url:
        return f"Could not connect to {domain}."

    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        speak(f"Scraping {full_url}")
        response = requests.get(full_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        titles = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        links = [a['href'] for a in soup.find_all('a', href=True)]

        email_matches = re.findall(r'mailto:([\w\.-]+@[\w\.-]+\.\w+)', " ".join(links))
        phone_matches = re.findall(r'phone=(\d{10,})', " ".join(links))
        combined_text = " ".join(titles + paragraphs)
        ceo_lines = re.findall(r"[^.]*\b(?:ceo|founder|co-founder)\b[^.]*\.", combined_text, re.IGNORECASE)

        return {
            "url": full_url,
            "titles": titles,
            "paragraphs": paragraphs,
            "links": links,
            "ceo": ", ".join(set(ceo_lines)),
            "email": ", ".join(set(email_matches)),
            "phone": ", ".join(set(phone_matches))
        }

    except Exception as e:
        return f"Error during scraping: {e}"
