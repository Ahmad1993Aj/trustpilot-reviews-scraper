import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
from playwright.sync_api import sync_playwright

BASE_URL = "https://de.trustpilot.com"
URL = "https://de.trustpilot.com/review/oerag.de"


def get_html_from_existing_edge(url: str) -> str:
    """
    Holt HTML aus einem bereits geöffneten Edge,
    der mit Remote Debugging läuft (Port 9222).
    Edge muss offen bleiben.
    """
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        context = browser.contexts[0]
        page = context.new_page()

        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(1500)

        html = page.content()

        page.close()
        browser.close()
        return html


def scrape_page(page: int = 1):
    if page == 1:
        url = URL
    else:
        url = f"{URL}?page={page}"

    html = get_html_from_existing_edge(url)
    soup = BeautifulSoup(html, "lxml")

    rows = []
    for article in soup.find_all("article"):
        # Name (stabiler als Hash-Klassen)
        name_el = article.find(attrs={"class": lambda c: c and "consumerName" in c})
        name = name_el.get_text(strip=True) if name_el else None

        # Rating (beste Quelle)
        rating_el = article.find("div", attrs={"data-service-review-rating": True})
        rating = int(rating_el["data-service-review-rating"]) if rating_el else None

        # Content block
        content = article.find("div", attrs={"data-review-content": "true"})
        if not content:
            continue

        # Title + Text
        title_el = content.find(attrs={"data-service-review-title-typography": "true"})
        text_el = content.find(attrs={"data-service-review-text-typography": "true"})
        title = title_el.get_text(strip=True) if title_el else None
        text = text_el.get_text(strip=True) if text_el else None

        # Date (Badge)
        date_el = article.find(attrs={"data-testid": "review-badge-date"})
        date_text = date_el.get_text(strip=True) if date_el else None

        # Review URL (für eindeutige ID / Dedup)
        a = content.find("a", href=True)
        review_url = urljoin(BASE_URL, a["href"]) if a else None

        rows.append({
            "name": name,
            "rating": rating,
            "title": title,
            "text": text,
            "date": date_text,
            "review_url": review_url,
        })

    return rows


def scrape_all(sleep_seconds: float = 1.5):
    all_rows = []
    seen = set()
    page = 1

    while True:
        print("Scraping page", page)
        rows = scrape_page(page)

        if not rows:
            print(f"Seite {page}: keine Reviews -> Stop.")
            break

        new_count = 0
        for r in rows:
            key = r.get("review_url")
            if key and key not in seen:
                seen.add(key)
                all_rows.append(r)
                new_count += 1

        print(f"Seite {page}: {new_count} neue Reviews gefunden.")

        if new_count == 0:
            print("Keine neuen Reviews mehr -> Stop.")
            break

        page += 1
        time.sleep(sleep_seconds)

    return all_rows


if __name__ == "__main__":
    try:
        all_rows = scrape_all(sleep_seconds=1.5)

        df = pd.DataFrame(all_rows)
        print(f"Gesamtanzahl Reviews: {len(df)}")

        df.to_csv("oerag_trustpilot_reviews_v2.csv", index=False, encoding="utf-8-sig")
        print("Daten gespeichert in 'oerag_trustpilot_reviews.csv'")

    except Exception as e:
        print(f"Fehler: {e}")
