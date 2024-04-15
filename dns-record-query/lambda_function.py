import json
import requests

def lambda_handler(event, context):
    response=requests.get("https://us-central1-zeta-structure-296509.cloudfunctions.net/dns-record-query?record_name={}&record_type={}")
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }