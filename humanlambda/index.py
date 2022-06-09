# Notify on detection of human image
#

from __future__ import print_function
import boto3
import os

def handler(event, context):

    human = "We found a human in the image copied to your bucket."

    print('Initiating image rekognition')

    found = event['found']

    if found == 'human':

        human_sns_client = boto3.client('sns')
        human_sns_client.publish(
            TopicArn = os.environ['topicARN'], 
            Message= human,
            Subject='A human was found!'
        )
    else:
        raise Exception('No human was detected')

    return