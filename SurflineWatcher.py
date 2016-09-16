from bs4 import BeautifulSoup
import urllib2

class SurflineWatcher:
    def __init__(self, url):
        self.url = url
        self.refresh()

    def get_conditions(self):
        self.refresh()
        return self.soup.find("div", {"id": "observed-spot-conditions"}).contents

    def refresh(self):
        self.html_content = urllib2.urlopen(self.url).read()
        self.soup = BeautifulSoup(self.html_content, "html.parser")
