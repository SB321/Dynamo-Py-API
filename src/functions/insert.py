import json
import boto3


dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('EmployeesDB')


def lambda_handler(event, context):
    if 'name' in event and 'employeeId' in event and 'email' in event and 'address' in event and 'phone' in event:
        
        name = event['name']
        employeeId = event['employeeId']
        email = event['email']
        address = event['address']
        phone = event['phone']
        
        response = table.put_item(
            Item={
                'employeeId': employeeId,
                'name': name,
                'email': email,
                'address': address,
                'phone': phone
            })
       
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
                "X-Requested-With": "*"
            },
            'body': json.dumps('Hello from Lambda, ' + name)
        }
    else:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
                "X-Requested-With": "*"
            },
            'body': json.dumps({'error': 'Missing required fields'})
        }
