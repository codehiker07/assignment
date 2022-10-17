

mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'}
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here

import random

# six mobile name
mobile1_name=mobile_data['data'][0].get('name')
mobile2_name=mobile_data['data'][1].get('name')
mobile3_name=mobile_data['data'][2].get('name')
mobile4_name=mobile_data['data'][3].get('name')
mobile5_name=mobile_data['data'][4].get('name')
mobile6_name=mobile_data['data'][5].get('name')

# six mobile price USD
usd_price1=mobile_data['data'][0].get('price')
usd_price2=mobile_data['data'][1].get('price')
usd_price3=mobile_data['data'][2].get('price')
usd_price4=mobile_data['data'][3].get('price')
usd_price5=mobile_data['data'][4].get('price')
usd_price6=mobile_data['data'][5].get('price')

# exchange rate
exchange_rate=mobile_data['exchnage_rate']

# six mobile price Converting BDT
bdt_price1= ((float(usd_price1.split()[0])) * (exchange_rate))
bdt_price2= (float(usd_price2.split()[0])) * (exchange_rate)
bdt_price3= (float(usd_price3.split()[0])) * (exchange_rate)
bdt_price4= (float(usd_price4.split()[0])) * (exchange_rate)
bdt_price5= (float(usd_price5.split()[0])) * (exchange_rate)
bdt_price6= (float(usd_price6.split()[0])) * (exchange_rate)

# six mobile made
mobile1_made=mobile_data['data'][0].get('made')
mobile2_made=mobile_data['data'][1].get('made')
mobile3_made=mobile_data['data'][2].get('made')
mobile4_made=mobile_data['data'][3].get('made')
mobile5_made=mobile_data['data'][4].get('made')
mobile6_made=mobile_data['data'][5].get('made')

for mobile in mobile_data:
  sentense= [
    f'{mobile1_name} is made in {mobile1_made}. The price is {usd_price1} USD which is almost equal to {bdt_price1} BDT',
    f'{mobile2_name} is made in {mobile2_made}. The price is {usd_price2} USD which is almost equal to {bdt_price2} BDT',
    f'{mobile3_name} is made in {mobile3_made}. The price is {usd_price3} USD which is almost equal to {bdt_price3} BDT',
    f'{mobile4_name} is made in {mobile4_made}. The price is {usd_price4} USD which is almost equal to {bdt_price4} BDT',
    f'{mobile5_name} is made in {mobile5_made}. The price is {usd_price5} USD which is almost equal to {bdt_price5} BDT',
    f'{mobile6_name} is made in {mobile6_made}. The price is {usd_price6} USD which is almost equal to {bdt_price6} BDT',
  ]

print(random.choice(sentense))






