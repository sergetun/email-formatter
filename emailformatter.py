from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ── Constants ────────────────────────────────────────────────────────────────

WAIT_TIMEOUT = 20

XPATHS = {
    "project_description": "//p[.//strong[contains(text(),'PROJECT DESCRIPTION')]/following-sibling::text()[1]]",
    "additional_marketing": "//p[.//strong[contains(text(),'ADDITIONAL MARKETING PLANS')]]",
    "artist_name":          "//h1/span",
    "h1":                   "//h1",
}


# ── Driver setup ─────────────────────────────────────────────────────────────

def create_driver() -> webdriver.Chrome:
    options = Options()
    # options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # options.add_argument(r"--user-data-dir=C:\Users\Serge\AppData\Local\Google\Chrome\User Data")
    # options.add_argument("--profile-directory=Default")
    return webdriver.Chrome(options=options)


# ── Data extraction ───────────────────────────────────────────────────────────

def extract_data(driver: webdriver.Chrome, wait: WebDriverWait) -> dict:
    h1_text    = driver.find_element(By.XPATH, XPATHS["h1"]).text.split("\n")
    span_text  = driver.find_element(By.XPATH, XPATHS["artist_name"]).text.split("\n")

    song_name   = h1_text[0]
    artist_name = span_text[0]
    date        = span_text[1] if len(span_text) > 1 else "N/A"

    project_description = wait.until(
        EC.presence_of_element_located((By.XPATH, XPATHS["project_description"]))
    ).text

    additional_marketing = wait.until(
        EC.presence_of_element_located((By.XPATH, XPATHS["additional_marketing"]))
    ).text

    driver.execute_script("window.location.hash = 'internal-details';")

    return {
        "artist_name":           artist_name,
        "song_name":             song_name,
        "date_of_release":       date,
        "project_description":   project_description,
        "additional_marketing":  additional_marketing,
    }


# ── Output formatting ─────────────────────────────────────────────────────────

def print_section(platform: str, data: dict, extra_fields: list[str]) -> None:
    """Print a formatted pitch block for a given platform."""
    sep = " "

    print(platform)
    print(sep)
    print(f"{data['artist_name']} - {data['song_name']}")
    print(data["date_of_release"])
    print(data["project_description"])
    print(sep)
    print("Marketing")
    print(data["additional_marketing"])
    print(sep)
    print("Details:")
    print(f"UPC: ")
    for field in extra_fields:
        print(f"{field}: ")
    print("Listening link")
    print("Press shots")
    print(sep)


def print_all_sections(data: dict) -> None:
    print_section("Other",   data, [])
    print_section("Apple",   data, ["Apple ID"])
    print_section("Spotify", data, ["URI"])


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    url = input("Enter the URL for Selenium to open: ").strip()
    if not url:
        raise ValueError("No URL provided.")

    driver = create_driver()
    try:
        driver.get(url)
        wait   = WebDriverWait(driver, WAIT_TIMEOUT)
        data   = extract_data(driver, wait)
        print_all_sections(data)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()