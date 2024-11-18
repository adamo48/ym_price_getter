from bs4 import BeautifulSoup
from selenium import webdriver
import json, requests
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    url = 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2212156529-af1a-423c-9139-e6f839019f8e%22)&allFacets=variants.attributes.productDriverLicenceCategory%7Cvariants.attributes.productMotorcyclePower:range+(0+to+*)%7Cvariants.attributes.productMotorcycleLimitedPowerVersion&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=24&offset=0&text=&productType=Unit&version=caas'

    response = requests.get(url)
    data = response.json()
    name = data['results'][0]['name']
    pcm = data['results'][0]['variants'][0]['attributes'][9]['value']
    year = data['results'][0]['variants'][0]['attributes'][10]['value']

    print(year)
    # moto = pricer(src)
    # print(moto)

class pricer():
    def __init__(self, link, name = None, price = None, disclaimer = ''):
            self.link = link
            self.name = name
            self.price = price
            self.disclaimer = disclaimer
            self.response = response = requests.get(self.link)
            
        

    def get_price(self):
      self.ele = self.soup.find("p", class_ = "")

    def __repr__(self):
        return f'name: {self.name}, price: {self.price}, disclaimer: {self.disclaimer}'
    


if __name__ == '__main__':
    main()
    