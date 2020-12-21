#Code for Lambda Function
import os
import json
import boto3
        
def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    messages = event["Records"]
    for message in messages:
        messageID = message["messageId"]
        body = message["body"]
        #POST INTO NGINX
    print(event)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Region ": json_region
        })
    }