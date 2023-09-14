import boto3
import json
import logging
from custom_encoder import CustomEncoder

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodbTable = 'products'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTable)


def build_response(statusCode, body=None):
    response = {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    if body is not None:
        response['body'] = json.dumps(body, cls=CustomEncoder)

    return response


def lambda_handler(event, context):
    logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']

    if httpMethod == 'GET' and path == '/health':
        response = build_response(200, 'Checking API')

    elif httpMethod == 'GET' and path == '/product':
        response = get_product(event['queryStringParameters']['productid'])

    elif httpMethod == 'GET' and path == '/products':
        response = get_products()

    elif httpMethod == 'POST' and path == '/product':
        response = add_product(json.loads(event['body']))

    elif httpMethod == 'PATCH' and path == '/product':
        requestBody = json.loads(event['body'])
        response = update_product(requestBody['productid'], requestBody['updateKey'], requestBody['updateValue'])

    elif httpMethod == 'DELETE' and path == '/product':
        requestBody = json.loads(event['body'])
        response = delete_product(requestBody['productid'])

    else:
        response = build_response(404, 'Not Found')

    return response


def get_product(productId):
    try:
        response = table.get_item(

            Key={
                'productid': productId
            }
        )

        if 'Item' in response:
            return build_response(200, response['Item'])

        else:
            return build_response(404, {'Message': 'ProductId %s not found ' % productId})

    except:
        logger.exception('Something Error Occurred')


def get_products():
    try:
        response = table.scan()
        result = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            result.extend(response['Items'])

            body = {

                'allproducts': result
            }

            return build_response(200, body)

    except:
        logger.exception('Something Error Occurred in viewing All Products')


def add_product(requestBody):
    try:
        table.put_item(Item=requestBody)
        body = {
            'Operation': 'SAVE',
            'Message': 'SUCCESS',
            'Item': requestBody
        }

        return build_response(200, body)

    except:
        logger.exception('Something Error Occurred in Adding Product')


def update_product(productid, updateKey, updateValue):
    try:
        response = table.update_item(

            Key={
                'productid': productid
            },
            UpdateExpression='set %s = :value' % updateKey,
            ExpressionAttributeValues={
                ':value': updateValue
            },
            ReturnValues='UPDATED_NEW'
        )

        body = {
            'Operation': 'UPDATE',
            'Message': 'SUCCESS',
            'UpdatedAttributes': response
        }

        return build_response(200, body)

    except:
        logger.exception('Something Error Occurred in Updating Product')


def delete_product(productId):
    try:
        response = table.delete_item(

            Key={
                'productid': productId
            },
            ReturnValues='ALL_OLD'
        )

        body = {
            'Operation': 'DELETE',
            'Message': 'SUCCESS',
            'deletedItem': response
        }

        return build_response(200, body)

    except:
        logger.exception('Something Error Occurred in Deleting Product')













