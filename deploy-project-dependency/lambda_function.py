import requests
import json

def lambda_handler(event, context):   
    response = requests.get("https://www.example.com/")
    confirmation_message = "GET request to 'https://www.example.com/' was successful."
    data = {
        'confirmation_message': confirmation_message,
        'page_content': response.text
    }
    print(data)
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
