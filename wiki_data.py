""" Extracting the name of 500 companies from wikipedia

"""
import urllib.request
import certifi
from bs4 import BeautifulSoup

WIKI = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
PAGE = urllib.request.urlopen(WIKI, cafile=certifi.where())
SOUP = BeautifulSoup(PAGE, "html.parser")
TABLE = SOUP.find('table', {"class" : "wikitable sortable"})
ROWS = TABLE.findAll("tr")
FILE_COMPANIES = open('companies_name.txt', 'w')
for row in ROWS[1:]:
    cells = row.findAll("td")
    company_name = cells[1].get_text()
    FILE_COMPANIES.write(company_name)
    FILE_COMPANIES.write("\n")
