"""application to test aligning JSON datasets"""
# Align_JSON_Test/__init__.py

from flask import Flask
import boto3

s3_resource = boto3.resource("s3",
                            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
                            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"])
my_bucket = s3_resource.Bucket(os.environ["S3_BUCKET"])

def create_app():
    app = Flask(__name__)

    return  app
