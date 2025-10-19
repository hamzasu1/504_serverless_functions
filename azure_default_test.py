import requests
import json

url = "https://serverless-ajd4gwbeczh8enbp.eastus2-01.azurewebsites.net/api/http_trigger1?code=CQRGmKmlgHbCHQzOnituSGy2v1j1UY_hWKP95QnUi0ukAzFuls5aLg=="

body = {
    "fasting_glucose_mg_dL" : 110
                    
}

try:
    response = requests.post(url, json=body)
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error during request: {e}")
