import os
import requests

from dataclasses import dataclass

AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = os.environ.get("AIRTABLE_TABLE_NAME")

@dataclass()
class Airtable:
    base_id:str
    api_key:str
    table_name:str
    
    def create_records(self, data={}):
        if len(data.keys()) == 0:
            return False
        
        endpoint = f"https://api.airtable.com/v0/{self.base_id}/{self.table_name}"
        # endpoint = f"https://api.airtable.com/v0/appGeZqmkCDe7z07j/fastapi-to-airtable"
        # endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            # "Authorization": f"Bearer keyAMMabTuP34PVzA",
            # "Authorization": f"Bearer {AIRTABLE_API_KEY}",
            "Content-Type": "application/json" 
        }
        data = {
            "records": [
                {
                    "fields": data
                },
            ]
        }
        r = requests.post(endpoint, headers=headers, json=data )
        print(endpoint, r.json())
        return r.status_code == 200 or r.status_code == 201
