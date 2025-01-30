import requests
import json

URL ="http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data =json_data)    
    data = r.json()
    print(data)
        
#get_data()    #for read 

def post_data():
    data ={
        'name': 'suraj',
        'roll': 10,
        'city': 'itahari'
    }
    
    json_data = json.dumps(data)
    r = requests.post(url = URL, data =json_data)    
    data = r.json()
    print(data)
    
post_data() #for write


def update_data():
    data ={
        'id': 4,
        'name': 'karki',
        'city': 'jhapa'
    }
    
    json_data = json.dumps(data)
    r = requests.put(url = URL, data =json_data)    
    data = r.json()
    print(data)
    
#update_data() #for update

def delete_data():
    data ={
        'id': 2
    }
    
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data =json_data)    
    data = r.json()
    print(data)
#delete_data()
    
         