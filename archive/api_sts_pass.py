
api_url='https://api.sts.pl/web/v1/offer/prematch?to=2024-06-01T01:00&lang=pl'
import requests
import pandas as pd
import json

def sts_scraper(api_url):
    headers = {

         

            'Cookie': 'registration_version=B.1; _ga=GA1.1.330358495.1702340486; _gcl_au=1.1.1514346333.1702340486; _tt_enable_cookie=1; _ttp=rgQGi3rTi92EIBLwiQ1iBeXW71f; ea_uuid=202312110024423603201602; _scid=b64efccd-8a7b-486f-9d65-1b7d2e6aef22; _fbp=fb.1.1702340488224.895471189; _hjSessionUser_1597449=eyJpZCI6ImNmMmM5ZTA5LTZjNzktNWMxMy05ZWE1LWVmNjg1OWRiYjhiOCIsImNyZWF0ZWQiOjE3MDIzNDA0ODcwNjIsImV4aXN0aW5nIjp0cnVlfQ==; __cfruid=607fb3ddee974851faab73699d9a410733dea651-1702710793; cpws_at=ARgIcHEViTAbLardOrmICUrA; cf_clearance=9YOsWIRCiA_roX6xd1fyWLl7QlntSGHkiyyzDFgsKVA-1702710796-0-1-4447d596.226beaf.2052b9b0-0.2.1702710796; entry_url=https%3A%2F%2Fwww.sts.pl%2F; welcome_screen=0.0.3-yes; _hjIncludedInSessionSample_1597449=1; _hjSession_1597449=eyJpZCI6Ijk1NTQwZTM5LWUyOWMtNDI0MS1hNjFhLWE5OGI4NGM4ZDc5MCIsImMiOjE3MDI3MTA4MDE1MjUsInMiOjEsInIiOjAsInNiIjowfQ==; cto_bundle=gxFoSF9aS2d6YVY1aCUyRnE4UW04JTJCeXBFYTNxZ2lHRjlFVWpoMWRCc0VVZnd0aE1LbFNHRGwySEVOS2dGanNWZVolMkJWcFMlMkYyd2ElMkZpR2Y5bmhvMnozJTJCekFCYmR5UFBoRVlhd3hNTm4lMkZsNm8lMkJkMmxYVnZRN3h4M1NaN2NuejZqNFhUczJvb3kzbjZiaWpHdFFMWUpBM25SZ1NST1B3JTNEJTNE; _scid_r=b64efccd-8a7b-486f-9d65-1b7d2e6aef22; _ga_WZNLBL055Q=GS1.1.1702710799.2.1.1702710834.25.0.0; promoCode=PewnyBonusSTS; campaign=PewneSTS; marketing_attribution_history=%5B%7B%22timestamp%22%3A1702710835659%2C%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22attributes%22%3A%5B%5D%7D%2C%7B%22timestamp%22%3A1702710796771%2C%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22attributes%22%3A%5B%5D%7D%2C%7B%22timestamp%22%3A1702341235098%2C%22referrer%22%3A%22https%3A%2F%2Fwww.sts.pl%2Frejestracja%3Fbtag%3DaY7JMtX_VkuHCtz6uPBSnWNd7Zgq%22%2C%22attributes%22%3A%5B%5D%7D%2C%7B%22timestamp%22%3A1702340493159%2C%22referrer%22%3A%22https%3A%2F%2Fwww.sts.pl%2Frejestracja%3Fbtag%3DaY7JMtX_VkuHCtz6uPBSnWNd7Zgq%22%2C%22attributes%22%3A%5B%5D%7D%2C%7B%22timestamp%22%3A1702340483493%2C%22referrer%22%3A%22https%3A%2F%2Fwww.goal.pl%2F%22%2C%22attributes%22%3A%5B%7B%22key%22%3A%22btag%22%2C%22value%22%3A%22aY7JMtX_VkuHCtz6uPBSnWNd7ZgqdRLk%22%7D%2C%7B%22key%22%3A%22aff%22%2C%22value%22%3A%22126%22%7D%2C%7B%22key%22%3A%22promoCode%22%2C%22value%22%3A%22GOAL%22%7D%2C%7B%22key%22%3A%22campaign%22%2C%22value%22%3A%22GOAL%22%7D%2C%7B%22key%22%3A%22utm_campaign%22%2C%22value%22%3A%22GOAL%22%7D%2C%7B%22key%22%3A%22utm_medium%22%2C%22value%22%3A%22BC%22%7D%2C%7B%22key%22%3A%22utm_source%22%2C%22value%22%3A%22aff%22%7D%2C%7B%22key%22%3A%22utm_content%22%2C%22value%22%3A%22text%22%7D%5D%7D%5D'

            }

    response = requests.get(api_url,)
    if response.status_code == 200:
        response=response.json() 
    else:
        print(f"Error: {response.status_code}")

    print(response)
    return response

