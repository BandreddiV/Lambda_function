print('Loading function')
import urllib2
import boto3
client = boto3.client('ses')
email_from = 'venkata.bandreddi@reancloud.com'
email_to = 'venkata.bandreddi@reancloud.com'
emaiL_subject = 'Internet_Connectivity_Email sent by the Lambda function using SES'
email_body = 'Unable to Connect to the INTERNET'

def lambda_handler(event, context):
    try:
        response=urllib2.urlopen('http://172.217.65.46',timeout=20)
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
