from bs4 import BeautifulSoup
import requests
import csv
import xlsxwriter

url = "https://www.solutionsantesecurite.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# Create a new Excel file
workbook = xlsxwriter.Workbook('output.xlsx')

# Add a worksheet for each sheet
worksheet1 = workbook.add_worksheet('text')
worksheet2 = workbook.add_worksheet('image')
worksheet3 = workbook.add_worksheet('title')

paragraphs = soup.find_all('p')
for i, p in enumerate(paragraphs):
	worksheet1.write_column(f'A{i+1}', [p.text])

# Extract all image URLs
images = soup.find_all('img')
for i, img in enumerate(images):
  worksheet2.write_column(f'A{i+1}', [img.get('src')])

# Extract the title
title = soup.find('title').text
worksheet3.write_column('A1', [title])

workbook.close()
