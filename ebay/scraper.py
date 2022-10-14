from bs4 import BeautifulSoup
import requests

def get_data():
    url  = "https://www.ebay.com.au/sch/i.html?_from=R40&_nkw=apple+watch&_sacat=0&LH_Auction=1&_sop=1"

    # Get the HTML from the URL
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find_all('div', class_="s-item__wrapper clearfix")

    list_items = []
    for item in items[1:]:
        title = item.find('div', class_="s-item__title")
        if title:
            title = title.text
        else:
            continue

        condition = item.find('span', class_="SECONDARY_INFO")
        if condition:
            condition = condition.text
        else:
            continue

        price = item.find('span', class_="s-item__price")
        if price:
            price = price.text
        else:
            continue

        timeleft = item.find('span', class_="s-item__time-left")
        if timeleft:
            timeleft = timeleft.text
        else:
            continue

        shippingcost = item.find('span', class_="s-item__logisticsCost")
        if shippingcost:
            shippingcost = shippingcost.text
        else:
            continue

        # print(title, condition, price, timeleft, shippingcost)
        if condition == "Parts only":
            continue
        dict_item = {'title': title, 'condition': condition, 'price': price, 'timeleft': timeleft, 'shippingcost': shippingcost}
        list_items.append(dict_item)
    
    return list_items

