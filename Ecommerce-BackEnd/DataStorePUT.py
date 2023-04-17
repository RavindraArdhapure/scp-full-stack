import json
import boto3 
import base64

def lambda_handler(event, context):
    filename = event.get('headers',{}).get('filename','NewStaticFile')
    data = event["body"]
    decoded_file = base64.b64decode(data)
    s3 = boto3.client("s3")

    s3_upload = s3.upload_file(data, 'datastoreapi5757', filename)

    print("S3_upload",s3_upload)
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Data is stored in the s3 bucket')
    }
