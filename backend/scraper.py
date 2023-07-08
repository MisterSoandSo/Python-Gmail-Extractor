from bs4 import BeautifulSoup
import re

class EmailReader():
    def __init__(self) -> None:
        self.content = None
        self.html_content = None
        self.nonhtml_content = None

    def readFile(self, filename):
        with open(filename, 'r') as file:
            self.content = file.read()

    def passContent(self, package):
        self.content = package

    def parseHtml(self):
        pattern = re.compile(r'<!DOCTYPE HTML.*?</html>', re.DOTALL)
        html_section = re.search(pattern, self.content)
        
        if html_section:
            # Extracted HTML portion
            self.html_content = html_section.group()
            #print(self.html_content)
        else:
            print("HTML portion not found in the text file.")

    def parseNonHtml(self):
        pattern = re.compile(r'<!DOCTYPE HTML.*?</html>', re.DOTALL)
        html_section = re.search(pattern, self.content)
        html_start_index = html_section.start()
        self.nonhtml_content = self.content[:html_start_index]


class SoupStrainer():
    def __init__(self,content = None,filename = None) -> None:
        if content:
            html_content = EmailReader().passContent(content)
        if filename:
            html_content = EmailReader().readFile(filename)
        self.soup = BeautifulSoup(html_content, 'html.parser')    
        
    #Extract Tags
    def find_table(self):
        tables = self.soup.find_all("table")
        tab_list = []
        for table in tables:
            row_list = []
            for row in table.find_all("tr"):
                col_list = []
                for cell in row.find_all("td"):
                    col_list.append(cell.text)
                row_list.append(col_list)
            tab_list.append(row_list)
        return tab_list
    
    def find_atags(self):
        a_tags = self.soup.find_all('a')
        for a in a_tags:
            print("Text:", a.text)
            print("Href:", a.get('href'))
            print() 

    def find_ptags(self):
        p_tags = self.soup.find_all('p')
        for p in p_tags:
            print(p.text)
            print() 

    def find_imgs(self):
        images = self.soup.find_all("img")
        for image in images:
            image_url = image["src"]
            print(image_url)