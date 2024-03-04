import requests
import pandas as pd

competitor_list = [
    {'url':"https://shop.thefreshmarket.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frequency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term=",
     'cookie':"osano_consentmanager_uuid=e595f81c-f907-43f2-95ba-26f48f9584c9; osano_consentmanager=F5T-RtiJt8pubJl2ReUQkU6QHA3g6_SlHaweHW9jMC9-cBkFm3IzuBhoXTL1xplRnGqiyNbEyNGxZ_2oB2iiuYM9Nt7Yw-1U0CLBhed_-7QOKZwcJHvFYBq3Z6WBL6pF8fyBC_rJhZM1-SZP1TcO2KbrJA2lXns09_jI5x_kXVQW3IqRyrbcohkxbTDtvcErejBVE-CblFudyZcJr_SwfgVcn8QwkJRhgYSzDvzo0PQ-wHIdIzdx3ov3e2F5Tpn7om-O-bDr27n-lqoOkNhhMfZtdzjoQZvw8Ktn7w==; _gcl_au=1.1.1461849753.1707114250; fw_se={%22value%22:%22fws2.1944e3dc-97cf-46ee-b26d-466e6413fafb.1.1707114251853%22%2C%22createTime%22:%222024-02-05T06:24:11.853Z%22}; _gid=GA1.2.2011831759.1707114254; _fbp=fb.1.1707114255537.836312339; _pin_unauth=dWlkPVl6SXhaakF6TVRBdE1qQTNZeTAwT0RNM0xXRTFaVE10T0RNd05ETTNNek16TXpVeQ; _uetsid=2eb4edd0c3ef11eea20063365b109795; _uetvid=2eb63350c3ef11eeb58e790798454c1a; fw_chid={%22value%22:%22N7A4N3b%22%2C%22createTime%22:%222024-02-05T06:34:07.709Z%22}; __cf_bm=Mf5GBzCsDLE.Gki1s6OV.7lVhSFIjaL7vf8yw_VWSYU-1707114849-1-AQDxdeRSo7/MbzJg1RcAv6c7cyBzyVaT6i1jLuBOnmat0jBAGJWLpo0H0LdZ3cWvYR1bYX7QtrEA40P3F3IwB+w=; _ga_EMDXDP2N4W=GS1.2.1707114259.1.1.1707114849.54.0.0; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-02-05T06:34:14.548Z%22}; fw_uid={%22value%22:%22080a1005-65f7-48f0-b59e-7e20045d5e1d%22%2C%22createTime%22:%222024-02-05T06:34:14.649Z%22}; __stripe_mid=0e45212f-d712-4dfa-8844-8cb05e42f960e2b8b7; __stripe_sid=ae3f3f42-6419-4f36-82a0-c0492e0ee7fa6010e0; ajs_anonymous_id=30b1fd5b-6a38-40dd-81ad-386862048c08; _ga_2NZ40CS25B=GS1.1.1707114254.1.1.1707114919.26.0.0; session-prd-tfm=.eJxNybtugzAAQNF_8RxFPAoVbFEert1gCwWTwIKAGGGCAWEIwVX_vRk73OXcH5BVI1c18Ku8VXwDsoGPMu94NwF_Gue3KK6U6Lts6h-8Az7gK64LWAoqMGIamURgb_tGs7Ti9Z0urfZZtN6Q7pGLGtwQGSwUMuccIZvC40RgXCfCFESXxjm6twEMl0BjSSy2kAtSqIt1esNVfg0FbdhKo2Qhh0Sf97hOoTkU_790zAIuCsnTXFiOU1w9s1yRe__CZnpZRH49GajpX0Tv7CA6GvTAjCrcTsMukQJZ6ev0_LbLOf28eXFt0YIdew0fyMgSqdmQjDQEGzArPmbiDnzH8lzjw7V__wBK22ji.GKITKw.XkUS02iLktOIvu1qDpa7x3Y0_BE; _ga=GA1.2.1922934719.1707114254; _dd_s=rum=0&expire=1707115824075"
     },
    
    {'url':"https://shop.sprouts.com/api/v2/store_products?limit=60&search_term=",
     'cookie':"_gcl_au=1.1.1870522609.1706678526; BVBRANDID=44bd90f1-c5b6-4f2a-b533-a2aa621c15aa; _fbp=fb.1.1706678528061.2114288924; _pin_unauth=dWlkPU9UaGhNVGswTWpFdFpHWmpPUzAwWVdOa0xUZ3dZMkl0TW1FeVpqTTFaVGM0TXpBMg; ajs_anonymous_id=7b482cc6-9dd7-4f91-806b-2206e1d21a77; _pin_unauth=dWlkPU9UaGhNVGswTWpFdFpHWmpPUzAwWVdOa0xUZ3dZMkl0TW1FeVpqTTFaVGM0TXpBMg; ajs_anonymous_id=7b482cc6-9dd7-4f91-806b-2206e1d21a77; __stripe_mid=69b2421c-f664-47b0-8ada-3194ed0b62d7f36b12; __cf_bm=lgw2xDhTdiare0ScDioqNO0EutjvCCu_wEgMWN1WBQ4-1707114788-1-AdC78VWrDbu1JkJnIl5zNIo2DRy5nedcTLoCX2xCNe0ohmOGTuiO262/cIFQVL409RbDcrOJExbpfRusqgPjlgM=; dotcomSearchId=a9d554b2-299b-493f-85c9-e3c3ee2374c3; session-sprouts=.eJwdzkFvgjAAhuH_0rMaCptGbk4ZK7ElOrDAhQAtsdgioyCC2X8f2eG7vJfveYG0bLm-ArvMpOYLkDa8VVnN6w7YXdvPRXOtxb1Ou_uN18AGfPSuuVsIX3gonBAkwtuu5ggL8zLOmwpTPnK5bZI9WiOFhyRAEFe78Rh8KhLsOuKeRvINBVbYPNKzjAMmycRuxI0tPCKN6suURF6Z0ZPwK2SQafcklTMQMYiYnruMvv9_Raa8oarpGX3q435GqW3PKXywCAu_Po-MhhopeWWzAwfFQKrY8g_hhCNjxZzZ7tCfj3aDssNGLy2Vp_uvZHmySoyd0jHvjXAOXRPEYAF6zdtUMGCbbxsDrqGx_v0Dvn1qTg.GKIS2w.x6ad_R9vBZoWwSb0SqfKYzbnbO0; _ga=GA1.2.1479835951.1706678528; _uetsid=e3542a80c41011ee8df3997928063361; _uetvid=b021a2c0bff811ee97982b12ce0f9533; _ga_LPZ816BHL5=GS1.1.1707128730.4.1.1707114843.60.0.0; _dd_s=rum=1&id=fb2edccc-bdca-4a50-bcb5-3604f16c3fb6&created=1707114774893&expire=1707115743747; _gid=GA1.2.1087611198.1707128730; _gat_UA-47434162-1=1; __stripe_sid=878306b4-2230-44e8-8901-12c006c31d9fef638e; BVBRANDSID=99cfa3cf-b854-4842-a1fc-dcc0d8bd271b; loyaltyID=undefined"
     },
    
    {'url':"https://shop.wegmans.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frequency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term=",

     'cookie':"_fbp=fb.1.1706863892752.1711026269; _pin_unauth=dWlkPU1Ua3hNR0k0TW1VdE4yWmlaaTAwWlRBM0xUbGhPV1l0TkRRMU9UQXlabUpoTldRNA; _gcl_au=1.1.2096486999.1706863893; ajs_anonymous_id=5ab5538e-b2a1-4e5b-8254-41491fe68824; _pin_unauth=dWlkPU1Ua3hNR0k0TW1VdE4yWmlaaTAwWlRBM0xUbGhPV1l0TkRRMU9UQXlabUpoTldRNA; __stripe_mid=6c025cd2-3c3b-4bcd-9bf7-9bc3d28bfcc2cae6a9; ajs_anonymous_id=5ab5538e-b2a1-4e5b-8254-41491fe68824; __cf_bm=2nYkjctxlRpIUesiCNlbnw2aE6AWL240Mgu_5zDUHiI-1707116052-1-Ae54yJJnevnKG4jv0o26FdxEZlt47EXLxsvRDCaHn3cHKU0zjmud8QkDYywnEVd3DHrBSsVrmGJKZQ88GttYs9U=; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiYwMzE5NTYzNTA4MzU0MzI1NzM5MzA3NDAyMzY4NDg5MjU3NDM5MFIRCOywkMjWMRgBKgRJTkQxMAPwAb2Cr8DXMQ==; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; wfm.tracking.sessionStart=1707116053732; wfmStoreId=16; at_check=true; inRedirectGoldPanAudience=1; AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19759%7CMCMID%7C03195635083543257393074023684892574390%7CMCAAMLH-1707720857%7C12%7CMCAAMB-1707720857%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1707123257s%7CNONE%7CMCSYNCSOP%7C411-19763%7CMCCIDH%7C0%7CvVersion%7C5.5.0; wfm.tracking.s10=1; wfm.tracking.x2p=1; lux_uid=170711615424981411; sa-user-id=s%253A0-c314a846-e95f-585a-6855-a77ea7494746.c%252Bm2vFrjOJYA1sYoLYpwpcTqmsRJa9XSFm%252FAeDCH3uA; sa-user-id-v2=s%253AwxSoRulfWFpoVad-p0lHRjEvxIg.eO161Pv2GS7ZMzG%252Faepi77Le1Nb3MhczPa4ejo7Ogrk; at_check=true; wegmans.chatbot.closed=1; s_gpv=My%20Items%20|%20Wegmans; dotcomSearchId=eb6b7be8-16ae-4f3c-a581-777acee766d9; _uetsid=5f68e6f0c3f311ee820a85c86c2cb567; _uetvid=441eb7d0c1a811ee93fb8b1fc156e199; session-prd-weg=.eJwdjsGOgjAUAP-lZ2MEQYSbUdcUeRAIWPVCEAqUFmQp6ILZf1-yh7nMZeaD4ryjskRWnghJFyhuaVcnDW16ZPXdMBtJpWTPJu6fnDbIQnS0y8cpZR6zcTRhxWW2uZylkqqXcWZKVfF6CLO97_EG1_4KDpmAylcc8sWAQO-efB1GhXnkqDvE5XDAKlRBeQ-5BiOWuLlM96udJ8RnXuWvvJCv3fCmAXuzGwn6hOj_rasqOK7aISM_0tnPU7U5UKK8siswrwnGjEQS16LM5g8I07dbFSpMhQ7r1ZIfxdkwziejiOzQJkGQgwfFO-I8jHb97vv4muSeO1vSFmiBBkm7mGXI0jTTNPTNVv39A-MYaas.GKIZQg.J8ekGy1Y58qIpnL2dslP06qRm_o; _dd_s=rum=0&expire=1707117383042; sa-user-id-v3=s%253AAQAKIFKNxEq2ttky7EgHck7mfumscKSUBmuIpSGXkEGmPYwFEAEYAyDCj4KuBjABOgSE7j3kQgRDk5Ov.DOjvV1ZvNvtvf%252FOC6f3oAiKy02jWa1lfBXY%252BLgh2PLc; mbox=session#743be30c611c4007a044c54b7b3e585c#1707118344"

     }
    
]

searchterm='organic pink lady apple'
cookie=competitor_list[2]['cookie']

HEADERS={
    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie
}

URL=competitor_list[2]['url']+'apple'
responses=requests.get(URL,headers=HEADERS)
data=responses.json()
items=data.get('items')
print(items)

for item in items:
    if (searchterm in item.get('name')):
        print(item.get('name'))