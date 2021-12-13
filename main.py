import boto3, json

lambda_client = boto3.client('lambda')


for document_number in range (1,101):
    response = lambda_client.invoke(
        FunctionName='trigger',
        InvocationType='Event',
        Payload=json.dumps({"document_number":document_number}),
    )

print(response['Payload'])
print(response['Payload'].read().decode("utf-8"))