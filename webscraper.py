import requests
from bs4 import BeautifulSoup

url = 'https://catalog.fullerton.edu/preview_program.php?catoid=70&poid=32659'  # Replace with the URL you want to test.

# Test the connection using requests
response = requests.get(url)

if response.status_code == 200:
    print("Connection successful!")
    # Parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Now you can work with the parsed HTML content
    # For example, you can find a specific element by its tag or class:
    element = soup.find('div', class_='acalog-core')
    # print(element.text)
    courses = element.find_all('li',class_='acalog-course')
    print(courses[0])
    # for i in range(len(element.text)):
    #     print(element.text) 
else:
    print("Connection failed. Status code:", response.status_code)
