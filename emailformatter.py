from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# adjust the path to your ChromeDriver executable

options = Options()
# you can add Chrome-specific options if needed, for example:
# options.add_argument("--user-data-dir=C:\Users\serge\AppData\Local\Google\Chrome\User Data")

# initialize the Chrome driver
driver = webdriver.Chrome(options=options)

# ask the user for the target URL to navigate to
url = input("Enter the URL for selenium to open: ")
if not url.strip():
    raise ValueError("No URL provided")

driver.get(url)

wait = WebDriverWait(driver, 20)

projectDescription = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//p[.//strong[contains(text(),'PROJECT DESCRIPTION')]/following-sibling::text()[1]]")
        )
    ).text 

artistName = driver.find_element(
    By.XPATH, 
    "//h1/span"
).text.split("\n")[0]

h1 = driver.find_element(By.XPATH, "//h1")
songName = h1.text.split("\n")[0]

span = driver.find_element(By.XPATH, "//h1/span")
dateOfRelease = span.text.split("\n")[1]

additionalMarketingPlans = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//p[.//strong[contains(text(),'ADDITIONAL MARKETING PLANS')]]")
        )
    ).text

driver.execute_script("window.location.hash = 'internal-details';") # navigate to internal details section to load the content


# p = wait.until(
#     EC.presence_of_element_located(
#         (
#             By.XPATH, "//p[contains(text(),'Delivered')]"
#             )
#         )
#     )

# text = p.text
# upc = text.split(" - ")[1]
# print(upc)

print("Other")
print("     ")
print(artistName + " - " + songName) 
print(dateOfRelease) 
print(projectDescription) 
print("     ")
print("Marketing")
print(additionalMarketingPlans) 
print("     ")
print("Details:")
print("UPC: ")
print("Listening link")
print("Press shots")
print("     ")

print("Apple")
print("     ")
print(artistName + " - " + songName) 
print(dateOfRelease) 
print(projectDescription) 
print("     ")
print("Marketing")
print(additionalMarketingPlans) 
print("     ")
print("Details:")
print("UPC: ")
print("Apple ID: ")
print("Listening link")
print("Press shots")
print("     ")

print("Spotify")
print("     ")
print(artistName + " - " + songName) 
print(dateOfRelease) 
print(projectDescription) 
print("     ")
print("Marketing")
print(additionalMarketingPlans) 
print("     ")
print("Details:")
print("UPC: ")
print("URI: ")
print("Listening link")
print("Press shots")