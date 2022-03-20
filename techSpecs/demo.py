import requests
import json


def search_product(product = 'iPhone 13', category = 'smartphone'):
    if product!= '' and category!= '':
        url = "https://apis.dashboard.techspecs.io/cs6vk2qrkhg626ia/api/product/search?query="+product
        payload = {"category": category}
        headers = {
            "Accept": "application/json",
            "x-blobr-key": "EAJIGl4C5ZQTkohu8DNlQoXCYCWGNP42",
            "Content-Type": "application/json"
        }
        
        response = requests.request("POST", url, json=payload, headers=headers)
        
        while response.status_code != 200:
            response = requests.request("POST", url, json=payload, headers=headers)
        
        result = json.loads(response.text)
        
        return result["data"]['results']
    else:
        return str('product or category is not valid!')

def product_details(prod_id):
    if prod_id != '':
        url = "https://apis.dashboard.techspecs.io/cs6vk2qrkhg626ia/api/product/get/"+prod_id
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "x-blobr-key": "EAJIGl4C5ZQTkohu8DNlQoXCYCWGNP42"
        }
        response = requests.request("GET", url, headers=headers)
        while response.status_code != 200:
            response = requests.request("GET", url, headers=headers)
        result = json.loads(response.text)
        return result["data"]['product']
    else:
        return str('product id is not valid!')

def all_brands():
    url = "https://apis.dashboard.techspecs.io/cs6vk2qrkhg626ia/api/product/brands"
    
    headers = {
        "Accept": "application/json",
        "x-blobr-key": "EAJIGl4C5ZQTkohu8DNlQoXCYCWGNP42"
    }
    
    response = requests.request("GET", url, headers=headers)
    while response.status_code != 200:
        response = requests.request("GET", url, headers=headers)
    result = json.loads(response.text)
    
    return result["data"]['brands']

def all_categories():
    url = "https://apis.dashboard.techspecs.io/cs6vk2qrkhg626ia/api/category/getAll"

    headers = {
        "Accept": "application/json",
        "x-blobr-key": "EAJIGl4C5ZQTkohu8DNlQoXCYCWGNP42"
    }
    
    response = requests.request("GET", url, headers=headers)
    while response.status_code != 200:
        response = requests.request("GET", url, headers=headers)
    result = json.loads(response.text)
    
    return result['data']['Category'][1]['source_engines']


def prod_by_brand_category(brand, category):
    url = "https://apis.dashboard.techspecs.io/19p7u0rsguq0qed0/api/product/getAll?page=1"

    if brand in all_brands() and category in all_categories():
        payload = {
            "brand": [brand],
            "category": [category]
        }
        headers = {
            "Accept": "application/json",
            "X-BLOBR-KEY": "EAJIGl4C5ZQTkohu8DNlQoXCYCWGNP42",
            "Content-Type": "application/json"
        }
        
        response = requests.request("POST", url, json=payload, headers=headers)
        while response.status_code != 200:
            response = requests.request("POST", url, json=payload, headers=headers)
        result = json.loads(response.text)
        
        if result['data']["product"] != []:
            return result['data']["product"]
        else:
            return str('brand and category does not match')
        
