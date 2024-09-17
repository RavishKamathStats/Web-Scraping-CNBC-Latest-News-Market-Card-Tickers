import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to chromedriver in the 'drivers' directory
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
chrome_driver_path = os.path.join(parent_directory, "drivers/chromedriver")
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service,
                          options=chrome_options)


print("Getting url using chrome driver...")
url = "https://www.cnbc.com/world/?region=world"
driver.get(url)
print("Successfully pulled url using chrome driver!")
# result = requests.get(url)

# doc = BeautifulSoup(result.text, 'html.parser')

# Total wait time in seconds
wait_time = 8

print(f"Operation will complete in {wait_time} seconds. Please wait...")

for remaining in range(wait_time, 0, -1):
    print(f"Time remaining: {remaining} seconds", end='\r')
    time.sleep(1)

print("\nOperation completed!")

# time.sleep(8)


current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
raw_data_directory = os.path.join(parent_directory, "data/raw_data")

# Check if the directory exists, if not, create it
if not os.path.exists(raw_data_directory):
    os.makedirs(raw_data_directory)

raw_data_path = os.path.join(raw_data_directory, "web_data.html")

print("Writing as web_data.html \nPlease wait...")
with open(raw_data_path, 
          'w',
          encoding='utf-8'
          ) as file:

    file.write(driver.page_source)

relative_path = os.path.relpath(raw_data_directory)
print("HTML data successfully saved to:  {}/{}".format(
    relative_path, "web_data.html"))

driver.quit()
