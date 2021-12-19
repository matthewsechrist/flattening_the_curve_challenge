import json
import boto3
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    # Simulate process runtime as if the job was uploading a document
    time.sleep(2)

    # Prints event information to the log
    logger.info(event)
    
    return