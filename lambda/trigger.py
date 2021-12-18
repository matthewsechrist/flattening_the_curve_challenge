import json
import logging
import boto3

from botocore.exceptions import ClientError

def send_sqs_message(QueueName, msg_body, delay):
    
    sqs_client    = boto3.client('sqs')
    sqs_queue_url = sqs_client.get_queue_url(QueueName=QueueName)['QueueUrl']
    
    try:
        msg = sqs_client.send_message(QueueUrl     = sqs_queue_url,
                                      #MessageBody  = json.dumps(msg_body),DelaySeconds=delay)
                                      MessageBody = json.dumps(msg_body))

    except ClientError as e:
        logging.error(e)
        return None
    return msg

def lambda_handler(event, context):

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    QueueName = 'my_queue'
    msg       = send_sqs_message(QueueName,event,delay)
    delay     = event['delay']
    
    if msg is not None:
        logging.info(f'Sent SQS message ID: {msg["MessageId"]}')
        
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
