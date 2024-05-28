import os
import json
from datetime import date, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, black
from reportlab.pdfgen import canvas
import boto3
    
def s3save(file_path, bucket_name, object_name):
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_path, bucket_name, object_name)
    