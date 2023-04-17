import json
import base64
import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    data = event["body"]
    filename = event.get('headers',{}).get('filename','NewStaticFile')
    
    # encoded_file = data['uploaded_file']
    
    decoded_file = base64.b64decode(data)
    s3_upload = s3.put_object(Bucket="datastoreapi5757", Key=filename, Body=decoded_file)
    
    print("s3 upload",s3_upload)
    return {
        'statusCode': 200,
        'body': json.dumps('Data is stored in the s3 bucket '+filename)
    }