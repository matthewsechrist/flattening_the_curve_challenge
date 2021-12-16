import boto3
import json
import random

lambda_client = boto3.client('lambda')

for document_number in range (1,101):
    delay    = random.randint(10,101)

    payload  = json.dumps({"document_number":document_number, "delay":delay})

    response = lambda_client.invoke(
        FunctionName   = 'trigger',
        InvocationType = 'Event',
        Payload        = payload
    )

    print(payload)