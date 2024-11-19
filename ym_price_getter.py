from bs4 import BeautifulSoup
import json, requests


def main():
    url = 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2212156529-af1a-423c-9139-e6f839019f8e%22)&allFacets=variants.attributes.productDriverLicenceCategory%7Cvariants.attributes.productMotorcyclePower:range+(0+to+*)%7Cvariants.attributes.productMotorcycleLimitedPowerVersion&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=24&offset=0&text=&productType=Unit&version=caas'

    response = requests.get(url)
    data = response.json()
    for moto in data['results']:
        name = moto['name']
        try:
            price = moto['variants'][0]['prices'][0]['amount']
        except:
            price = 0

        disclaimer = 'brak disclaimera'
       
        for attr in moto['variants'][0]['attributes']:
            if attr['name'] == 'pricingDisclaimer':
                disclaimer = attr['value']
                break

        year, pcm = None, None
        for attr in moto['variants'][0]['attributes']:
            
            if attr['name'] == 'productYear':
                year = attr['value']
            elif attr['name'] == 'productPCMCode':
                pcm = attr['value']
               
        print(name,'\n', year,'\n',pcm,'\n', price, '\n', disclaimer, '\n','\n')


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
    