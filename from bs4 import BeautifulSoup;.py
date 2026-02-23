from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\serge\Downloads\geckodriver\geckodriver.exe")
driver = webdriver.Firefox(service=service)

driver.get("https://www.virginmusic.io/release?recordId=recwDl5vkuBqUJ6JY")

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

driver.get("https://www.virginmusic.io/release?recordId=recwDl5vkuBqUJ6JY#internal-details")

p = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//p[contains(text(),'Delivered')]")
        )
    )

text = p.text
upc = text.split(" - ")[1]
print(upc)

# print("Other")
# print("     ")
# print(artistName + " - " + songName) done
# print(dateOfRelease) done
# print(projectDescription) done
# print("     ")
# print("Marketing")
# print(additionalMarketingPlans) done
# print("     ")
# print("Details:")
# print("UPC: " + upc)
# print(listeningLink)
# print(pressShots)