import requests
import pandas as pd

cookie = "_gcl_au=1.1.744926426.1706767839; _gid=GA1.2.1162395534.1706767841; BVBRANDID=f63dc7d7-4aa0-426a-b94a-e1efc47a7296; _fbp=fb.1.1706767841797.218183443; _pin_unauth=dWlkPVl6SXhaakF6TVRBdE1qQTNZeTAwT0RNM0xXRTFaVE10T0RNd05ETTNNek16TXpVeQ; loyaltyID=null; ajs_anonymous_id=2d1116f6-0a4d-4f99-83d3-8c1b23341876; __stripe_mid=a1b6693a-506d-4ee0-90f4-ab17fb86859a99717a; _pin_unauth=dWlkPVl6SXhaakF6TVRBdE1qQTNZeTAwT0RNM0xXRTFaVE10T0RNd05ETTNNek16TXpVeQ; ajs_anonymous_id=2d1116f6-0a4d-4f99-83d3-8c1b23341876; BVBRANDSID=1b307b75-d2ba-424a-b953-65df31877de4; __cf_bm=2UEwybqsG6_MBhno599UAGT5juhjPtV0WZc6Gyn5xgM-1706777333-1-AQ/wd5JjFJH3g1rMxsH8oQwS7yPe9M8VFmpOh6wKz7C+uleqBZSLJYSeZXVEBBC8/TuIyJ+i0eG/JhRhbJfN0OY=; UsableNetAssistive=1; __stripe_sid=2f3bd26f-92f5-43ef-b0c5-4c908475eef155a321; dotcomSearchId=7897fe26-efbb-4cc4-9420-bad673abcb19; _ga=GA1.2.110827980.1706767841; _uetsid=a1dca080c0c811ee852ffb5dab55dcc9; _uetvid=a1dcb350c0c811eeb1f4b5bdbc06d374; _ga_LPZ816BHL5=GS1.1.1706777330.2.1.1706777844.4.0.0; session-sprouts=.eJwdjsuOgjAAAP-lZ2MAFQI3JVksS2tEpMiF8Ci2CJVQUOlm_33JHuYyl5kfkNUDlQw4dd5KugJZT4cuF1SMwBmHaTGSSsmfIhufDyqAA-jss8Ir-Yn78Kqgjrlvrxepl0Y8L6jSaF9Fa_epC03YxCwlYYejsAsI0pC6j9iL2e2iM9TBTRAxjlQ5p9F-Rk34wC6UUMQqTfw6J2d-aqCGFdxhdVPYffMbCcec7P5bidE-YNNPFfnIwF2mOnuiRH9VCeInEc4VuUrYtaxaPlBUvnFTGljdNSy0tTefrdgU8ed7UKl1SPr68iWvI8vp0byb7yFsj_hQeEEx7cEKTJIOGa-AY2wtw7bMzfb3DyUya6I.GJzudg.Pb6yPT8Sf3r6R2ThF6v7J5LwtNQ; _dd_s=rum=0&expire=1706778748085"

HEADERS = {
    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie    
}

name=input("enter the name :")

abmart_df = pd.read_excel('abmart.xlsx',sheet_name='Sheet1')
for i in range(0,len(abmart_df)):
    searchitem = abmart_df.loc[i]['name']

URL = f"https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=5&offset=0&search_is_autocomplete=true&search_provider=ic&search_term={searchitem}&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false"

responses = requests.get(URL,headers=HEADERS)
data = responses.json()
# print(type(data))
# print(data['items'][0]['name'])

#for i in range (len(data['items'])) :
    #print(data['items'][i]['name'],data['items'][i]['base_price'])
    
items=data['items']

df_items=pd.DataFrame(items)
cleaned_items_df=df_items[['name','base_price','display_uom','average_uom']]
#cleaned_items_df.to_csv('cleaned_data.csv',index=False)
cleaned_items_df.to_excel('cleaned_data.xlsx',index=False)
#cleaned_items_df.to_json('cleaned_data.json',index=False)
#cleaned_items_df.to_html('cleaned_data.html',index=False)

abmart_df = pd.read_excel('abmart.xlsx',sheet_name='Sheet1')
searchitem = abmart_df.loc[0]
#print(searchitem)
print(len(abmart_df))