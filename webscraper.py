from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
import time
import requests
import json

def webscraper(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
    # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the business listings in the category
        #course_links = soup.find_all('li', class_ =links)

        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(5)
        course_links = driver.find_elements(By.CSS_SELECTOR, 'li.acalog-course span a')
        listings = soup.find_all('li', class_ ='acalog-course')
        data1 = []
        
        for link in course_links:
            link.click()
            # time.sleep(1)

            #course_content = soup.find_all('li',class_ ='acalog-course acalog-course-open')
            course_content = driver.find_elements(By.CSS_SELECTOR, 'li.acalog-course.acalog-course-open')
            # print(course_content)
            
            for course in course_content:
                try:
                    name = course.find_element(By.CSS_SELECTOR,'li.acalog-course.acalog-course-open span a').text
                except:
                    name = ''

                try:
                    desc = course.find_element(By.CSS_SELECTOR,'td.coursepadding').text

                    first_newline = desc.find('(3)\n')
                    second_newline = desc.find('\n\n', first_newline)

                    if first_newline != -1:  # Check if the second newline exists
                        # Replace everything after the second newline with your desired content
                        desc = "" + desc[first_newline+4:second_newline]
                    else:
                        desc = desc

                except:
                    desc = ''
                
                try:
                    preq = course.find_element(By.CSS_SELECTOR,'td.coursepadding').text

                    preq_second_newline = preq.find('\n\n')
                    #second_newline = desc.find('\n', first_newline + 1)

                    if preq_second_newline != -1:  # Check if the second newline exists
                        # Replace everything after the second newline with your desired content
                        preq = preq[preq_second_newline:].replace('Prerequisites:' or '\n' or '\n\n','')
                        preq = preq.replace('\n\n',"")
                        preq = preq.replace('Prerequisite: ','')
                    else:
                        preq = ''

                except:
                    preq =''
            
                new_entry = {
                    'Name': f'{name}',
                    'Description': f'{desc}',
                    'Prereqesites':f'{preq}'
                }
                data1.append(new_entry)
        return data1
            

url = 'https://catalog.fullerton.edu/preview_program.php?catoid=70&poid=32659'

data = webscraper(url)
print(data)

with open("data.json", "a") as json_file:
    # Step 4: Serialize the data and write it to the file
    json.dump(data, json_file)