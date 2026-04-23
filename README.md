# Virgin Music Skeleton Generator
**Internal tool for Tomorrowland Music Label**

A Selenium-based web scraper that pulls key release data from the Virgin Music Group portal and outputs a pre-formatted "skeleton" ready to be sent to DSPs (Apple Music, Spotify, and others).

---

## Overview

When a new release is submitted on the Virgin Music portal, this tool automates the process of copying key metadata into a standardised format. Instead of manually copying artist names, release dates, project descriptions, and marketing plans across multiple platform templates, you paste in the URL and the skeleton is generated instantly.

---

## Requirements

- Python 3
- Google Chrome (latest)
- ChromeDriver (matching your Chrome version)

Install dependencies:

```bash
pip install selenium
```

> **Note:** ChromeDriver must be on your system `PATH`, or placed in the same directory as the script. Download it from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads).

---

## Usage

1. Run the script:

```bash
python emailformatter.py
```

2. When prompted, paste in the full URL of the release page from the Virgin Music Group portal:

```
Enter the URL for Selenium to open: https://www.virginmusic.io/release?recordId=recKe5LcaiExB7C3V
```

3. The script will open Chrome, scrape the page, and print the formatted skeleton directly to your terminal.

---

Output Format

The script outputs three platform blocks — **Other**, **Apple**, and **Spotify** — each pre-filled with scraped data and placeholder fields for details that need to be added manually:

```
Other

Artist Name - Song Title
DD/MM/YYYY
[Project Description]

Marketing
[Additional Marketing Plans]

Details:
UPC: 
Listening link
Press shots


Apple

Artist Name - Song Title
DD/MM/YYYY
[Project Description]
...
Apple ID: 
...


Spotify

Artist Name - Song Title
...
URI: 
...
```

---

## What Gets Scraped

| Field | Source on Page |
|---|---|
| Artist Name | `<h1><span>` element |
| Song Title | `<h1>` element |
| Date of Release | Second line of `<h1><span>` |
| Project Description | Paragraph containing `PROJECT DESCRIPTION` |
| Additional Marketing Plans | Paragraph containing `ADDITIONAL MARKETING PLANS` |

---

## Known Limitations & Planned Improvements

### Internal Details Access
The "Internal Details" section (UPC, ISRC, etc.) requires navigating to a separate anchor (`#internal-details`) and may need authentication or an extra wait. Currently the UPC and other internal fields are left as blank placeholders.

**Planned fix:** Implement authenticated session support using Chrome's existing user profile, and add targeted XPath/JS extraction for the internal details panel after it loads.

### Unwanted Words in Output
Scraped text sometimes includes label names, boilerplate headers (e.g. `"PROJECT DESCRIPTION"`), or other unwanted strings that bleed into the output.

**Planned fix:** Add a configurable blocklist of strings to strip from scraped fields before printing, using a simple `clean_text()` helper.

### Multi-Paragraph & Bullet Point Project Descriptions
When a project description contains line breaks, blank lines, or is formatted as a bullet list on the portal, the current XPath only captures the first paragraph node.

**Planned fix:** Switch to a parent-container XPath that captures all sibling `<p>`, `<li>`, and `<ul>` nodes under the `PROJECT DESCRIPTION` header, then join them into a single cleaned string.

---

## 👤 Author

Serge Thurain Bolduc Tun

Internal tool — Tomorrowland Music Label
