#Code for Lambda Function
import os
import json
import boto3
import requests

def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    messages = event["Records"]
    for message in messages:
        messageID = message["messageId"]
        url = 'http://[INSERT IP ADDRESS HERE]'
        myobj = {"testkey":messageID}
        x = requests.post(url, data = myobj)
    print(event)
