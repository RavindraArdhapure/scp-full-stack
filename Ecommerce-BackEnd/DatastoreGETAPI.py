import json
import base64
import boto3
import io
import botocore
client=boto3.client('s3')

def lambda_handler(event, context):
    filename = event.get('headers',{}).get('filename','NewStaticFile')
    s3 = boto3.client('s3')
    
    # client = boto3.client('s3')
    # bytes_buffer = io.BytesIO()
    # client.download_fileobj(Bucket="datastoreapi5757", Key=filename, Fileobj=bytes_buffer)
    # byte_value = bytes_buffer.getvalue()
    # str_value = byte_value.decode()
    

    # This is just an example, parameters should be fine tuned according to:
    # 1. The size of the object that is being read (bigger the file, bigger the chunks)
    # 2. The number of threads available on the machine that runs this code

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(u'datastoreapi5757')
    obj = bucket.Object(key = filename)      #pass your image Name to key
    response = obj.get()     #get Response
    img = response[u'Body'].read()        # Read the respone, you can also print it.
    #print(type(img))                      # Just getting type.
    myObj = [base64.b64encode(img)]          # Encoded the image to base64
    #print(type(myObj))            # Printing the values
    #print(myObj[0])               # get the base64 format of the image
    #print('type(myObj[0]) ================>',type(myObj[0]))
    return_json = str(myObj[0])           # Assing to return_json variable to return.
    #print('return_json ========================>',return_json)
    return_json = return_json.replace("b'","")          # replace this 'b'' is must to get absoulate image.
    encoded_image = return_json.replace("'","")
    
    

    response = client.get_object(
    Bucket='datastoreapi5757',
    Key=filename,
)
    print("Response from s3 : ",response)
    image_file_to_be_downloaded=response['Body'].read()
    return {
        'statusCode': 200,
        'headers':{
            'Content-Type':'application/pdf',
            'Content-Disposition':'attachment;filename={}'.format(filename)
        },
        'body':base64.b64encode(image_file_to_be_downloaded) ,
        'isBase64Encoded': True
    }
    
