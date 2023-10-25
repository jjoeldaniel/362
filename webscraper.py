from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# load the page
URL = "https://catalog.fullerton.edu/preview_program.php?catoid=70&poid=32659"
driver = webdriver.Chrome()
driver.get(URL)
time.sleep(5)  # wait for the page to load

# locate all course links
course_links = driver.find_elements(By.CSS_SELECTOR, 'li.acalog-course span a')

unique_elements = []  # list to store unique texts of elements

# iterate through each course link
for index, link in enumerate(course_links):
    link.click()
    time.sleep(2)
    
    xpath_selector_all = ("//*[@id='gateway-page']/body/table/tbody/tr[3]/td[2]/"
                          "table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/"
                          "tr[2]/td/div/div/div/div/div/ul/li/span/"
                          "table/tbody/tr/td/div")
    
    elements = driver.find_elements(By.XPATH, xpath_selector_all)
    
for element in elements:
        element_text = element.text
        if element_text not in unique_elements:  # check if the text is not a duplicate
            unique_elements.append(element_text)  # add each element's text to the list

driver.quit()

# Write all unique elements to a text file
with open('elements.txt', 'w', encoding='utf-8') as file:
    for text in unique_elements:
        file.write(text + '\n')
        file.write("------------------------------------------------\n")

"""
this scrapes only lower and upper and sends to a text file
"""
