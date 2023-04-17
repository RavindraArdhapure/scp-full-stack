import boto3



import json
import boto3 
import base64

def lambda_handler(event, context):
    filename = event.get('headers',{}).get('filename','NewStaticFile')
    s3 = boto3.client("s3")

    client = boto3.client('s3')
    client.delete_object(Bucket='datastoreapi5757', Key=filename)
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Data is Deleted from s3 bucket'+str(filename))
    }
