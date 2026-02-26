from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\serge\Downloads\geckodriver\geckodriver.exe")

options = Options()
options.profile = r"C:\Users\serge\AppData\Roaming\Mozilla\Firefox\Profiles\wgtk7pnl.default-release"

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.virginmusic.io/release?recordId=recJ5GdqzsKvmrfH2")

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
# print("     ")
# print("Details:")
# print("UPC: " + upc)
# print(listeningLink)
# print(pressShots)

print("Apple")
print("     ")
print(artistName + " - " + songName) 
print(dateOfRelease) 
print(projectDescription) 
print("     ")
print("Marketing")
print(additionalMarketingPlans) 
# print("     ")
# print("Details:")
# print("UPC: " + upc)
# print(listeningLink)
# print(pressShots)

print("Spotify")
print("     ")
print(artistName + " - " + songName) 
print(dateOfRelease) 
print(projectDescription) 
print("     ")
print("Marketing")
print(additionalMarketingPlans) 
# print("     ")
# print("Details:")
# print("UPC: " + upc)
# print(listeningLink)
# print(pressShots)