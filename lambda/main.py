import boto3
import json
import random

lambda_client = boto3.client('lambda')

# We will be calling the Lambda fuction 100 times sending an both the sequential document number, and 
# delay to be used in DelaySeconds in writing the message to the SQS queue.
for document_number in range (1,101):
    delay    = random.randint(10,100)

    payload  = json.dumps({"document_number":document_number, "delay":delay})

    response = lambda_client.invoke(
        FunctionName   = 'trigger',
        InvocationType = 'Event',
        Payload        = payload
    )

    print(payload)