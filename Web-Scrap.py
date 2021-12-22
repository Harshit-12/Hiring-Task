# importing modules
import urllib.request
from bs4 import BeautifulSoup

# providing url
link = "https://en.wikipedia.org/wiki/H#History"

# opening the url for reading
page_content = urllib.request.urlopen(link)

# parsing the html file
html_Parser = BeautifulSoup(page_content, 'html.parser')

# getting all the paragraphs
for each_para in html_Parser.find_all("p"):
	print(each_para.get_text())
