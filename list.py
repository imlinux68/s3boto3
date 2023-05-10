#!/bin/python
import boto3


s3 = boto3.resource('s3')

while True:
    bucketName = input("Enter your bucket name to list all files inside: ")
    try:
        s3.meta.client.head_bucket(Bucket=bucketName)
        bucket = s3.Bucket(bucketName)
        print(f"Files are in '{bucketName}' bucket are: ")
        for file in bucket.object.all():
            print(obj.key)
        break
    except Exception as e:
        print(f"Error: {e}")
        c = input("Try Again okay? y/n") 
        if c == "n":
            break