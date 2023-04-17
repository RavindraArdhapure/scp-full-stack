# import the JSON utility package
import json
# import the Python math library
import math

# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('powerofmath')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):
    Username = str(event['Username'])
    Password = str(event['Password'])
    
            
    response = table.get_item(
        Key={
            'ID': Username
        })
        
    print(response)
            
    # TODO implement
    return {
        'statusCode': 200,
        'body': response
    }
