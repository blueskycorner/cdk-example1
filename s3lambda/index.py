# Lambda function to execute Step Function based on s3 event 
#

import boto3
import json
import os

def handler(event, context):

    print('Initiating image rekognition')

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

    print('Detected the following image in S3')
    print('Bucket: ' + bucket + ' key name: ' + key)
    
    ourObject = {
        "ourBucket": bucket,
        "ourKey": key
        }

    # Replace Step Function ARN

    stepARN = os.environ['STEP_ARN']

    client = boto3.client('stepfunctions')

    print(json.dumps(ourObject))

    response = client.start_execution(
        stateMachineArn=stepARN,
        input = json.dumps(ourObject)
    )

    return