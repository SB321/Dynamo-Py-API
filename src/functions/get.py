import json
import boto3


def lambda_handler(event, context):
    try:
     
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('EmployeesDB')

        response = table.scan()
        data = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
                "X-Requested-With": "*"
            },
            'body': json.dumps(data)
        }
    except Exception as e:
        
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
                "X-Requested-With": "*"
            },
            'body': json.dumps({'error': str(e)})
        }
