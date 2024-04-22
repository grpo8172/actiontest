import requests
import json

url = "https://tower.dna.iplab.au.singtelgroup.net/api/v2/job_templates/932/launch/"

payload = json.dumps({
  "extra_vars": {
    "additionalText": "Card Missing",
    "cardNumber": "26"
  }
})
headers = {
  'Authorization': 'Bearer T3RxeTcNaGYWdHKf6Ild22tzAlyFBv',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
