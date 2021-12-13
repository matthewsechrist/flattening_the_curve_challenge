import boto3, json

lambda_client = boto3.client('lambda')


for document_number in range (1,101):
    payload = json.dumps({"document_number":document_number})

    response = lambda_client.invoke(
        FunctionName='trigger',
        InvocationType='Event',
        Payload=payload,
    )
    print(document_number)
    print(payload)

print(response['Payload'])
print(response['Payload'].read().decode("utf-8"))