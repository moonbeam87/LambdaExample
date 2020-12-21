#Code for Lambda Function
import os
import json
import boto3
        
def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
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