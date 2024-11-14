from bs4 import BeautifulSoup
import requests

def main():
    moto = pricer('https://www.yamaha-motor.eu/pl/pl/motorcycles/')

class pricer():
    def __init__(self, link, name = None, price = None, disclaimer = ''):
        self.link = link
        self.name = name
        self.price = price
        self.disclaimer = disclaimer
        self.response = response = requests.get(self.link)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')    

    def get_price(self):
      self.ele = self.soup.find("p", class_ = "")

    def __repr__(self):
        return f'name: {self.name}, price: {self.price}, disclaimer: {self.disclaimer}'
if __name__ == '__main__':
    main()
    