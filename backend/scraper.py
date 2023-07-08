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
            print(self.html_content)
        else:
            print("HTML portion not found in the text file.")

    def parseNonHtml(self):
        pattern = re.compile(r'<!DOCTYPE HTML.*?</html>', re.DOTALL)
        html_section = re.search(pattern, self.content)
        html_start_index = html_section.start()
        self.nonhtml_content = self.content[:html_start_index]

