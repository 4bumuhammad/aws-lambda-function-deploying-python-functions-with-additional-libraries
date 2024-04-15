import json
import requests

def lambda_handler(event, context):
    try:
        record_name = event['queryStringParameters'].get('record_name', '')
        record_type = event['queryStringParameters'].get('record_type', '')
    
        url = "https://us-central1-zeta-structure-296509.cloudfunctions.net/dns-record-query?record_name={}&record_type={}".format(record_name, record_type)
    
        response = requests.get(url)
        data = response.json()
        print(data)
        
        return { 
            'statusCode': 200,
            'body': json.dumps(data)
        }
    except Exception as e:
        return { 
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }