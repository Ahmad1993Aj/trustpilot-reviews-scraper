# 🏢 Trustpilot Business Reviews Scraper | ÖRAG Bewertungsanalyse

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green.svg)](https://pandas.pydata.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Web%20Scraping-orange.svg)](https://playwright.dev/)

> 🇩🇪 **[Deutsche Version](#-deutsche-version)** | 🇺🇸 **[English Version](#-english-version)** | ⚙️ **[Setup Guide](#-setup-guide)**

---

## 🇩🇪 Deutsche Version

Eine umfassende Web-Scraping- und Datenverarbeitungs-Pipeline zum Extrahieren und Analysieren von Unternehmensbewertungen von Trustpilot.de. Dieses Projekt demonstriert fortgeschrittene Web-Scraping-Techniken, Datenbereinigung und ETL-Prozesse für Business Intelligence.

### 🎯 Projektübersicht

Dieses Projekt scrapt **373 Kundenbewertungen** für **ÖRAG Rechtsschutzversicherung** von Trustpilot.de und verarbeitet die Daten für die Analyse:

- 🤖 **Automatisiertes Web-Scraping** mit Playwright und Browser-State-Management
- 🧹 **Umfassende Datenvorverarbeitung** inkl. Textnormalisierung und Emoji-Behandlung  
- 📊 **ETL-Pipeline** zur Bereinigung und Transformation von Bewertungsdaten
- 💾 **Export-Funktionen** für weitere Analysen (CSV, JSON)

### 🚀 Features

#### Web Scraping
- 🔄 **Multi-Seiten-Scraping** mit automatischer Paginierung (373 Bewertungen)
- 🌐 **Browser-State-Management** über Edge Remote Debugging
- 🛡️ **Anti-Detection-Maßnahmen** mit realistischen Wartezeiten
- ⚡ **Duplikaterkennung** über URL-Tracking
- 🔗 **Eindeutige Bewertungs-IDs** für Datenintegrität

#### Datenverarbeitung
- 🧹 **Textnormalisierung** (ä→ae, ö→oe, ü→ue, ß→ss)
- 😊 **Emoji-Verarbeitung** (💩→"schlecht", ➕→"positiv")
- 📅 **Deutsche Datumsanalyse** ("7. Januar 2026" → datetime)
- 🔐 **Anonymisierung** (Namen → numerische IDs)
- 🧽 **Whitespace-Bereinigung** und Sonderzeichen-Behandlung

### 📊 Datenschema

| Spalte | Typ | Beschreibung | Beispiel |
|--------|-----|--------------|----------|
| `reviewer_id` | integer | Anonyme ID | 1, 2, 3... |
| `rating` | integer | Sternbewertung | 1-5 |
| `title` | string | Bewertungstitel | "Schnelle Bearbeitung" |
| `text` | string | Bewertungstext | "Sehr guter Service..." |
| `date` | datetime | Standardisiertes Datum | 2026-01-07 |
| `review_url` | string | Trustpilot-URL | https://de.trustpilot.com/reviews/... |

### 📈 Dateneinblicke

- **373 Bewertungen** erfolgreich gescrapt
- **Zeitraum**: Oktober 2025 - Januar 2026
- **Bewertungsverteilung**: 1-5 Sterne
- **Deutsche Textverarbeitung** mit Emoji-Normalisierung

---

## 🇺🇸 English Version

A comprehensive web scraping and data processing pipeline for extracting and analyzing business reviews from Trustpilot.de. This project demonstrates advanced web scraping techniques, data cleaning, and ETL processes for business intelligence.

### 🎯 Project Overview

This project scrapes **373 customer reviews** for **ÖRAG Rechtsschutzversicherung** (German legal insurance) from Trustpilot.de:

- 🤖 **Automated web scraping** using Playwright with browser state management
- 🧹 **Comprehensive data preprocessing** including text normalization and emoji handling  
- 📊 **ETL pipeline** for cleaning and transforming review data
- 💾 **Export capabilities** for further analysis (CSV, JSON)

### 🚀 Features

#### Web Scraping
- 🔄 **Multi-page scraping** with automatic pagination (373 reviews extracted)
- 🌐 **Browser state management** using Edge remote debugging
- 🛡️ **Anti-detection measures** with realistic delays
- ⚡ **Duplicate detection** via URL tracking
- 🔗 **Unique review IDs** for data integrity

#### Data Processing
- 🧹 **Text normalization** (German umlauts: ä→ae, ö→oe, ü→ue)
- 😊 **Emoji processing** (💩→"bad", ➕→"positive") 
- 📅 **German date parsing** ("7. Januar 2026" → datetime)
- 🔐 **Anonymization** (names → numeric IDs)
- 🧽 **Whitespace cleaning** and special character handling

### 📊 Data Schema

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `reviewer_id` | integer | Anonymous ID | 1, 2, 3... |
| `rating` | integer | Star rating | 1-5 |
| `title` | string | Review title | "Fast processing" |
| `text` | string | Review content | "Very good service..." |
| `date` | datetime | Standardized date | 2026-01-07 |
| `review_url` | string | Trustpilot URL | https://de.trustpilot.com/reviews/... |

### 📈 Data Insights

- **373 reviews** successfully scraped
- **Time period**: October 2025 - January 2026  
- **Rating distribution**: 1-5 stars
- **German text processing** with emoji normalization

---

## ⚙️ Setup Guide

### 📋 Prerequisites
- Python 3.8+
- Microsoft Edge browser
- Git

### 🛠️ Installation

1. **Clone Repository**
```bash
git clone https://github.com/Ahmad1993Aj/trustpilot-reviews-scraper.git
cd trustpilot-reviews-scraper
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Install Playwright**
```bash
playwright install chromium
```

### 🚀 Usage

#### 1. Web Scraping

**Start Edge with Remote Debugging:**
```bash
# Windows
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222
```

**Run Scraper:**
```bash
python main.py
```

#### 2. Data Processing

**Open ETL Notebook:**
```bash
jupyter notebook ETL.ipynb
```

### 📁 Project Structure

```
trustpilot_webscraping/
├── main.py                           # Main scraping script
├── save_login_state.py               # Browser state utility
├── ETL.ipynb                         # Data preprocessing notebook  
├── requirements.txt                  # Python dependencies
├── oerag_trustpilot_reviews_v2.csv   # Raw scraped data (373 reviews)
├── oerag_trustpilot_reviews_cleaned.csv  # Processed clean data
├── .gitignore                        # Git ignore rules
└── README.md                         # This file
```

### 🔧 Technical Architecture

#### Web Scraping Stack
- **Playwright**: Browser automation & control
- **BeautifulSoup**: HTML parsing & extraction
- **Pandas**: Data manipulation & export
- **Remote Debugging**: Session persistence

#### Data Processing Pipeline
- **German Text Normalization**: Umlauts & special characters
- **Emoji Processing**: Semantic conversion to text
- **Date Parsing**: Custom German format handling
- **Data Validation**: Quality checks & error handling

### 🚀 GitHub Repository Setup

**Repository URL**: `https://github.com/Ahmad1993Aj/trustpilot-reviews-scraper`

```bash
# Initialize and upload
git init
git add .
git commit -m "Initial commit: Trustpilot scraper with ETL pipeline"
git branch -M main
git remote add origin https://github.com/Ahmad1993Aj/trustpilot-reviews-scraper.git
git push -u origin main
```

#### 🏷️ Recommended Topics
```
web-scraping, data-engineering, trustpilot, pandas, playwright, 
etl-pipeline, sentiment-analysis, german-nlp, business-intelligence
```

### 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Browser connection fails | Ensure Edge runs with `--remote-debugging-port=9222` |
| Empty results | Check if Trustpilot page structure changed |
| Date parsing errors | Verify German locale settings |
| Emoji processing issues | Install: `pip install emoji` |

### 💼 Portfolio Highlights

**Skills Demonstrated:**
- 🕸️ Advanced Web Scraping & Browser Automation
- 🔧 Data Engineering & ETL Pipeline Development  
- 🧹 Text Processing & German NLP
- 📊 Data Analysis with Pandas
- 🌐 International Localization (German/English)

**Use Cases:**
- **Business Intelligence**: Customer sentiment analysis
- **Market Research**: Competitor review analysis
- **Data Science**: ML training data preparation
- **Academic Research**: Review pattern studies

### 📝 License & Ethics

This project is for **educational and research purposes**. Users must:
- ✅ Respect website terms of service
- ✅ Follow data protection laws (GDPR)
- ✅ Implement appropriate rate limiting
- ✅ Use data ethically and responsibly

### 📞 Contact

**Ahmad** - [@Ahmad1993Aj](https://github.com/Ahmad1993Aj)

**Project**: [trustpilot-reviews-scraper](https://github.com/Ahmad1993Aj/trustpilot-reviews-scraper)

---

⭐ **Star this repository if it helped you!** ⭐
