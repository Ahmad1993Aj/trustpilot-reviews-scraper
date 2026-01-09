from playwright.sync_api import sync_playwright

URL = "https://de.trustpilot.com/review/oerag.de"


def get_html_from_existing_edge(url: str) -> str:
    """
    Verbindet sich mit einem bereits gestarteten Edge
    (Remote Debugging Port 9222) und holt HTML.
    """
    with sync_playwright() as p:
        # Verbindung zu laufendem Edge
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")

        # ersten vorhandenen Kontext nehmen
        context = browser.contexts[0]

        # neue Seite öffnen
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(1500)

        html = page.content()

        page.close()
        browser.close()
        return html


def main():
    print("Hole HTML aus bereits geöffnetem Edge ...")
    html = get_html_from_existing_edge(URL)

    # Test: nur Länge ausgeben
    print("HTML Länge:", len(html))

    # Optional: HTML speichern zum Prüfen
    with open("edge_page.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("HTML gespeichert in edge_page.html")


if __name__ == "__main__":
    main()
