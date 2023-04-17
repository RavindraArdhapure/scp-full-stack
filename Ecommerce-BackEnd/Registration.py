import urllib3
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
table = dynamodb.Table('registration')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):
    print("Event Check ::",str(event))
    Username = str(event['Username'])
    Email = str(event['Email'])
    Password = str(event['Password'])
    firstName = str(event['FirstName'])
    lastName = str(event['LastName'])
    
    http = urllib3.PoolManager()
    
    # Custom API for Registration
    url = "http://devlopment-env.eba-nuhmizmx.us-east-1.elasticbeanstalk.com/api/addUser"
   
    payload = json.dumps({
        "userName": Username,
        "password": Password,
        "firstName": firstName,
        "lastName": lastName,
        "email": Email
    })

   
    headers = {
        'Content-Type': 'application/json'
    }
    
    try:
        responseAPI = http.request('POST', url, headers=headers, body=payload)
        print("Status code of ClassMate API:", responseAPI.status)
    except Exception as e:
        print("Exception:", e)
        return {
            'statusCode': 200,
            'body': json.dumps('Error while calling class mate API!'+str(e))
        }

        

    
    # write result and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        Item={
            'ID': str(Email),
            'LatestGreetingTime':now
            })
    print("Status code of DB add :", response)
    
     # Public API for Registration
    url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send"
    
    http = urllib3.PoolManager()

    payload = {
	        "personalizations": [
		        {
			        "to": [{"email": str(Email)}],
			        "subject": "Registration sucessfull to Redstore!"
		        }
	        ],
	        "from": {"email": str(Email)},
	        "content": [
		        {
			        "type": "text/plain",
			        "value": "Hello, Registration sucessfull to Redstore from lambda_handler!"
		        }
	        ]
        }

    headers = {
	    "content-type": "application/json",
	    "X-RapidAPI-Key": "fa89a7fa98mshbe5061e7e3c086ep12089ejsn461ee6d1242a",
	    "X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
    }

    
    try:
        responseAPI = http.request('POST', url, headers=headers, body=bytes(json.dumps(payload), encoding='utf-8'))
        print(responseAPI.data.decode("utf-8"))
    except Exception as e:
        print("Exception:", e)
            
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Sucessfully registration done!'+str(responseAPI.status))
    }
