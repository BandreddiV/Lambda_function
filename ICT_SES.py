print('Loading function')
import urllib2
import boto3
import os
client = boto3.client('ses')
email_from = os.environ['From_Address']
email_to = os.environ['To_Address']
emaiL_subject = 'Internet_Connectivity_Email sent by the Lambda function using SES'
email_body = 'Unable to Connect to the INTERNET'

def lambda_handler(event, context):
    try:
        response=urllib2.urlopen('http://172.217.6.46',timeout=20)
        return True
    except Exception as e:
        print(e)
        response = client.send_email(
            Source = email_from,
            Destination={
                'ToAddresses': [
                    email_to,
                ]
            },
            Message={
                'Subject': {
                    'Data': emaiL_subject
                },
                'Body': {
                    'Text': {
                        'Data': email_body
                    }
                }
            }
        )
        return response
        print('Error in connecting to the internet and SES email was sent')
        raise(e)
