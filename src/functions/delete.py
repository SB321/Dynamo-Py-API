import json
import boto3


dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('EmployeesDB')


def lambda_handler(event, context):
    
    employeeId = event['employeeId']
    
   
    response = table.delete_item(
        Key={
            'employeeId': employeeId
        }
    )
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Employee deleted successfully')
    }
