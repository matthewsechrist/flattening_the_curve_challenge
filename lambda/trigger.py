import json
import logging
import boto3

from botocore.exceptions import ClientError

# This function takes in the SQS queue name, the message body and the delay as 
# an Integer in seconds
def send_sqs_message(QueueName, msg_body, delay):
    
    # This section creates the SQS client using the queue's URL by queue name
    sqs_client    = boto3.client('sqs')
    sqs_queue_url = sqs_client.get_queue_url(QueueName=QueueName)['QueueUrl']
    
    # This try-catch block attempts to send the message to the SQS queue
    # and will write an error message to the log if it fails
    try:
        msg = sqs_client.send_message(QueueUrl     = sqs_queue_url,
                                      MessageBody  = json.dumps(msg_body)
                                     ,DelaySeconds = delay)
    except ClientError as e:
        logging.error(e)
        return None
    
    # Returns the message if it suceeds    
    return msg

# This function sets the queue name and recieves the delay through the event
# parameter. It then calls the send_sqs_message function. 
def lambda_handler(event, context):

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # This section sets the queue name and delay value to be used 
    # for DelaySeconds when sending the SQS message
    QueueName = 'my_queue'
    delay     = event['delay']
    
    msg       = send_sqs_message(QueueName,event,delay)
    
    # If sending the SQS message suceeds, it writes the MessageID
    # to the log
    if msg is not None:
        logging.info(f'Sent SQS message ID: {msg["MessageId"]}')
        
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
