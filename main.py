from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

url = 'https://www.scrapingcourse.com/button-click'
driver.get(url)

# Click on the load more button 3 times
try:
    for i in range(3):
        # Locate the load more button on the web page using its ID.
        load_more_button = driver.find_element(By.ID, 'load-more-btn')

        # Scroll to bring the 'Load more' button into view.
        driver.execute_script(
            "arguments[0].scrollIntoView(true);", load_more_button)

        # Click on the Load more button.
        load_more_button.click()

        # Wait for 2 seconds for the page to load more content.
        time.sleep(2)
    
    # Logic to parse the HTML content. Executes after load more is clicked thrice.
    # Get the page source which contains the HTML of the page.
    page_source = driver.page_source

    # Parse the page using beautifulSoup
    parsed_page = BeautifulSoup(page_source, 'lxml')

    # Find all the product items
    product_items = parsed_page.find_all('div', class_='product-item')

    # Extract and print product details
    for item in product_items:
        # product name
        name = item.find('span', class_='product-name').string.strip()
        
        # link to product
        link = item.find('img', class_='product-image')['src'].strip()

        # product price
        price = item.find('span', class_='product-price').text.strip()

        # product page url
        product_url = item.find('a')['href'].strip()

        print(f'Name: {name}')
        print(f'Link: {link}')
        print(f'Price: {price}')
        print(f'URL: {url}')
        print('\n') # print empty line

finally:
    # End the webdriver session
    driver.quit()
