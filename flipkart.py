from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY '
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class" : "_3O0U0u"})
#print(len(containers))
#print(soup.prettify(containers[0]))
container = containers[0]
name = container.findAll("div",{"class":"_3wU53n"})
#print(name[0].text)
#print(container.div.img("alt"))
#print(container)
price = container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
#print(price[0].text)
rating = container.findAll("div",{"class":"hGSR34"})
#print(rating[0].text)
filename = "products.csv"
f = open(filename,"w",encoding="utf-8")
headers = "Product_Name,Pricing,Ratings\n"
f.write(headers)
for container in containers:
    product_name = container.div.img["alt"]
    price_container = container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
    price = price_container[0].text.strip()
    rating_container = container.findAll("div",{"class":"hGSR34"})
    rating = rating_container[0].text
    #print(product_name+","+price.replace("₹","Rs")+","+rating)
    f.write(product_name+","+price+","+rating+"\n")
f.close()
