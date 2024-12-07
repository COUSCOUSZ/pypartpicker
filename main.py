from pypartpicker import Scraper


# creates the scraper object
pcpp = Scraper()
# returns a list of Part objects we can iterate through
parts = pcpp.part_search("intel i9",limit=1000)

# iterates through every part object
for part in parts:
    # prints the name of the part
    print(part.name)
    product = pcpp.fetch_product(part.url)
    print("🚨🚨🚨product url")
    print(product.url)
    print(product.specs)



# prod = pcpp.fetch_product("https://pcpartpicker.com/product/4r4Zxr/amd-ryzen-5-9600x-39-ghz-6-core-processor-100-100001405wof")
# print(prod.specs)