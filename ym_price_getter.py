from bs4 import BeautifulSoup
import json, requests, csv

segments = {
    'Motocykle': {
        'Supersport': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2212156529-af1a-423c-9139-e6f839019f8e%22)&allFacets=variants.attributes.productDriverLicenceCategory%7Cvariants.attributes.productMotorcyclePower:range+(0+to+*)%7Cvariants.attributes.productMotorcycleLimitedPowerVersion&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=24&offset=0&text=&productType=Unit&version=caas',
        'Hyper Naked': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%22eac477ad-ba76-4849-ba18-69918db1afec%22)&allFacets=variants.attributes.productDriverLicenceCategory%7Cvariants.attributes.productMotorcyclePower:range+(0+to+*)%7Cvariants.attributes.productMotorcycleLimitedPowerVersion&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Sport Heritage': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2238eae1fa-21fb-4bb1-b02a-b2738f3360f9%22)&allFacets=variants.attributes.productDriverLicenceCategory%7Cvariants.attributes.productMotorcyclePower:range+(0+to+*)%7Cvariants.attributes.productMotorcycleLimitedPowerVersion&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Sport Touring': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%223ead3011-edc7-4407-9eb6-5413b85f9d1e%22)&allFacets=variants.attributes.productDriverLicenceCategory%7Cvariants.attributes.productMotorcyclePower:range+(0+to+*)%7Cvariants.attributes.productMotorcycleLimitedPowerVersion&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Adventure': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%22f4dc4cbe-29b3-48cd-8e8f-6b6fa01714df%22)&allFacets=variants.attributes.productDriverLicenceCategory%7Cvariants.attributes.productMotorcyclePower:range+(0+to+*)%7Cvariants.attributes.productMotorcycleLimitedPowerVersion&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Off Road Competition': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%22dc7b6208-ce0c-4fec-9d87-06756d3b38c8%22)&allFacets=variants.attributes.productDriverLicenceCategory%7Cvariants.attributes.productMotorcyclePower:range+(0+to+*)%7Cvariants.attributes.productMotorcycleLimitedPowerVersion&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas'
    },
    'Skutery': {
        'Skutery Sport': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2271eaed22-9731-4565-9482-ae38487452d4%22)&allFacets=variants.attributes.productScooterStorage%7Cvariants.attributes.productScooterPower:range+(0+to+*)%7Cvariants.attributes.productScooterEngine:range+(0+to+*)%7Cvariants.attributes.productDriverLicenceCategory&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Urban Mobility': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2230519b9a-c8ab-478d-8ffb-36a64a817886%22)&allFacets=variants.attributes.productScooterStorage%7Cvariants.attributes.productScooterPower:range+(0+to+*)%7Cvariants.attributes.productScooterEngine:range+(0+to+*)%7Cvariants.attributes.productDriverLicenceCategory&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas'
        
    },
    'E-Bikes': {
        'Mountain': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%22564d194b-1155-4cb3-9e28-92787472c987%22)&allFacets=variants.attributes.productEBikeRidingType%7Cvariants.attributes.productEBikeWheelSize&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Urban': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%22f7154c1b-9083-44a8-ae5c-5381922512d7%22)&allFacets=variants.attributes.productEBikeRidingType%7Cvariants.attributes.productEBikeWheelSize&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Gravel': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%22bc7035cb-d7eb-4fd6-b56d-2f1a2e58d841%22)&allFacets=variants.attributes.productEBikeRidingType%7Cvariants.attributes.productEBikeWheelSize&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas'
    },
    'Silniki Zaburtowe': {
        'Elektryczne': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2215ae197d-db6a-4cf4-a0df-3bbc121eb370%22)&allFacets=&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas'
    },
    'Skutery Wodne': {
        'Sportowe': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%228491eef8-c165-4f9a-8f7b-4e2f2b46cc22%22)&allFacets=variants.attributes.productWaveRunnersEngineSize:range+(0+to+*)%7Cvariants.attributes.productWaveRunnersSupercharger%7Cvariants.attributes.productWaveRunnersDryWeight:range+(0+to+*)&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Cruising': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2270ea6ace-29d3-42e4-842b-026a6aaf127f%22)&allFacets=variants.attributes.productWaveRunnersEngineSize:range+(0+to+*)%7Cvariants.attributes.productWaveRunnersSupercharger%7Cvariants.attributes.productWaveRunnersDryWeight:range+(0+to+*)&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Rekreacja': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%227b5148f0-41c9-4410-97bb-027008a42c58%22)&allFacets=variants.attributes.productWaveRunnersEngineSize:range+(0+to+*)%7Cvariants.attributes.productWaveRunnersSupercharger%7Cvariants.attributes.productWaveRunnersDryWeight:range+(0+to+*)&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas'
    },
    'Lodzie': {
        'Lodzie otwarte': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2285247593-4f97-41ab-9dd0-f5d4286a430c%22)&allFacets=variants.attributes.productBoatLength:range+(0+to+*)%7Cvariants.attributes.productBoatType%7Cvariants.attributes.productBoatBrand%7Cvariants.attributes.productBoatHorsepowerMinRange:range+(0+to+*)%7Cvariants.attributes.productBoatHorsepowerMaxRange:range+(0+to+*)&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Bowrider': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%223baad1a9-f9e4-4a66-a8cf-40a0852ffe07%22)&allFacets=variants.attributes.productBoatLength:range+(0+to+*)%7Cvariants.attributes.productBoatType%7Cvariants.attributes.productBoatBrand%7Cvariants.attributes.productBoatHorsepowerMinRange:range+(0+to+*)%7Cvariants.attributes.productBoatHorsepowerMaxRange:range+(0+to+*)&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Day Cruiser': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2274bfee4c-e59e-4571-8f6b-ba1ffcf44cde%22)&allFacets=variants.attributes.productBoatLength:range+(0+to+*)%7Cvariants.attributes.productBoatType%7Cvariants.attributes.productBoatBrand%7Cvariants.attributes.productBoatHorsepowerMinRange:range+(0+to+*)%7Cvariants.attributes.productBoatHorsepowerMaxRange:range+(0+to+*)&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Kabinowe': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2228a496c4-7e74-4aa0-81d2-89e20751f22b%22)&allFacets=variants.attributes.productBoatLength:range+(0+to+*)%7Cvariants.attributes.productBoatType%7Cvariants.attributes.productBoatBrand%7Cvariants.attributes.productBoatHorsepowerMinRange:range+(0+to+*)%7Cvariants.attributes.productBoatHorsepowerMaxRange:range+(0+to+*)&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Pontony': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2268be793e-39cd-4169-94d5-46ae1d8fd363%22)&allFacets=variants.attributes.productBoatLength:range+(0+to+*)%7Cvariants.attributes.productBoatType%7Cvariants.attributes.productBoatBrand%7Cvariants.attributes.productBoatHorsepowerMinRange:range+(0+to+*)%7Cvariants.attributes.productBoatHorsepowerMaxRange:range+(0+to+*)&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas'
    },
    'ATV & Side by Side': {
        'Utility': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%225b3e6a35-a7b6-48be-9be9-4edd977273f3%22)&allFacets=&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Rekreacyjne': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%22501b27c3-d547-4a8a-a9a4-12780e763e16%22)&allFacets=&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Sport': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%229af81869-cbe0-4038-99c0-214bb08e748e%22)&allFacets=&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas'
    },
    'Lekkie Pojazdy': {
        'Flota Golfowa': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%22463c70bc-bc87-4649-a516-f2d262d8d83b%22)&allFacets=&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Pojazdy Uzytkowe': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%225874724a-5cea-43a3-9eac-3291a70ab205%22)&allFacets=&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Wozki Transportowe': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%22b8c2b6b3-b2ce-4004-81ed-eb9cc743ab1f%22)&allFacets=&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas'
    },
    'Power Products': {
        'Generatory': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%2218bf2ef7-fd80-4b3a-b4af-4b23fab502ff%22)&allFacets=&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas',
        'Odsniezarki': 'https://hyperdrive.yamaha-motor.eu/products/yme-prod-pl?projectKey=yme-prod-pl&locale=pl-PL&query=categories.id:subtree(%22f9517cb0-d0eb-412e-9a1a-178496edf0ac%22)&allFacets=&selectedFacets=&sort=variants.attributes.productIndex.asc%7Cvariants.attributes.productABBProductNameLocalized.asc%7Cvariants.attributes.productYear.desc&limit=72&offset=0&text=&productType=Unit&version=caas'
    }
}

def main():
   
    
    motour = Pricer(segments['Motocykle']['Off Road Competition'])
    motour.get_products()
    print(motour)
    


class Pricer():
    def __init__(self, url):
            self.url = url
            self.repreza = []
    
    def get_products(self):
        response = requests.get(self.url)
        data = response.json()
        with open('products.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
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
                    
                self.repreza.append((name,year,pcm, price,disclaimer))
                #self.repreza.append(name)
                writer.writerow((name,year,pcm,price,disclaimer))
            

    def __str__(self):
        rul = ''
        for i in self.repreza:
            rul = rul + f'{i}\n'
        return rul
    


if __name__ == '__main__':
    main()
    