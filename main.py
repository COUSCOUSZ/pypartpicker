from pypartpicker import Scraper
from time import sleep


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up headless mode
options = Options()
# options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional: Disable GPU for better compatibility
options.add_argument('--window-size=1920,1080')  # Set window size to mimic a visible browser

# Start the browser
driver = webdriver.Chrome(options=options)

# Navigate to the target page
url = "https://pcpartpicker.com/products/video-card/#c=436,514,446,425,447,427,448,424,572,518,546,499,497,513,494,508,506,492,507,516,505,493,520,552,553,550,565,549,566,542,567,539&sort=-chipset&page=1"
driver.get(url)

# Wait for the content to load
driver.implicitly_wait(5)

# Locate the desired element
try:
    # Assuming "main-content" is a class, use CLASS_NAME
    body = driver.find_element(By.CLASS_NAME, "main-content")
    print(body.text)  # Extract and print the text content
except Exception as e:
    print(f"Error: {e}")

# Close the browser
driver.quit()


# creates the scraper object
# pcpp = Scraper()
# returns a list of Part objects we can iterate through
# parts = pcpp.part_search("intel i9",limit=1000)
# i=1

# # iterates through every part object
# for part in parts:
#     print(i)
#     i += 1
#     # prints the name of the part
#     print(part.name)
#     sleep(i)
#     product = pcpp.fetch_product(part.url)
#     print("🚨🚨🚨product url")
#     print(product.url)
#     print(product.specs)
    



# prod = pcpp.fetch_products("https://pcpartpicker.com/products/video-card/#c=436,514,446,425,447,427,448,424,572,518,546,499,497,513,494,508,506,492,507,516,505,493,520,552,553,550,565,549,566,542,567,539&sort=-chipset&page=1")