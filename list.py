#!/bin/python
import boto3
import os
from time import sleep
from botocore.exceptions import ClientError 
import logging



s3 = boto3.resource('s3')
regionName = 'us-west-2'
s3_client = boto3.client('s3', region_name=regionName)

def listBucket():
    print("Here are your already existing Buckets: ")
    for bucket in s3.buckets.all():
        print(bucket.name)


def listingFiles():
    while True:
        listBucket()
        bucketName = input("Enter your bucket name to list all files inside: ")
        try:
            s3 = boto3.client('s3')
            response = s3.list_objects(Bucket=bucketName)
            if 'Contents' in response:
                for item in response['Contents']:
                    print(item['Key'])
        except Exception as e:
            print(f"Error: {e}")
            c = input("Try Again okay? y/n") 
            if c == "n":
                break


def createBucket(region):
    while True:
        listBucket()
        bucketName = input("Enter your bucket name to create it ")
        try:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucketName,
                                    CreateBucketConfiguration=location)
        except ClientError as e:
            logging.error(e)
            return False
        return True

def deleteBucket():
    while True:
        listBucket()
        bucketName = input("Enter your bucket name to delete: ")
        try:
            s3.meta.client.head_bucket(Bucket=bucketName)
            s3.Bucket(bucketName).delete()
            print(f"The bucket name '{bucketName}' is deleted successfully!!")
        except:
            print(f"The bucket name '{bucketName}' Doesnt exists!!")
            break

def uploadFile():
    while True:
        listBucket()
        bucketName = input("Enter your bucket name to upload to it: ")
        try:
            s3.meta.client.head_bucket(Bucket=bucketName)
            break
        except:
            print(f"The bucket {bucketName} doesnt exists")
    file_path = input("Enter the filenames separated by commas - , :").split(",")
    file_path = [path.strip() for path in file_path]
    for File in file_path:
        if not os.path.exists(File):
            print(f"File with name: '{File}' doesnt exists, skipping next...")
            continue
        fileName = os.path.basename(File)
        s3.meta.client.upload_file(File, bucketName, fileName)
        print(f"File with name: '{fileName}' Uploaded successfully!!!")


def downFile():
    while True:
        listBucket()
        bucketName = input("Enter your bucket name to download from it: ")
        fileName = input("Enter your file name to download from it: ")
    #     # try:
    #     #     s3.meta.client.head_bucket(Bucket=bucketName)
    #     #     break
    #     # except:
    #         # print(f"The bucket {bucketName} doesnt exists")
    # file_path = input("Enter the filenames separated by commas - , :").split(",")
    # file_path = [path.strip() for path in file_path]
    # for File in file_path:
    #     if not File:
    #         continue
        # fileName = File.split("/")[-1]
        s3c = boto3.client('s3')
        s3c.download_file(bucketName, fileName, fileName)
        print(f"File with name: '{fileName}' Downloaded successfully!!!")


def menu ():
    while(True):
        choice=input("Menu:\n1. List all buckets\n2. Create new bucket\n3. Upload to bucket\n4. Download from bucket\n5. list all files in bucket\n6. Delete Bucket\n")
        if(choice=="1"):
            print("Now you will see your buckets:....\n")
            sleep(3)
            listBucket()
        elif(choice=="2"):
            print("Create your bucket:....\n")
            sleep(3)
            res = createBucket("us-west-2")
        elif(choice=="3"):
            print("Upload new files to bucket:....\n")
            sleep(3)
            uploadFile()
        elif(choice=="4"):
            print("download files to your bucket:....\n")
            sleep(3)
            downFile()
        elif(choice=="5"):
            print("List all files in your bucket:....\n")
            sleep(3)
            listingFiles()
        elif(choice=="6"):
            print("delete your bucket:....\n")
            sleep(3)
            deleteBucket()
        else:
            print("Enter 1-6 ONLY!!!!\n")
            continue
        exit=input("Do you wanna to exit? yes/no\n")
        if(exit=="yes"):
            print("Bye....")
            break
            
            
######MAIN SCRIPT###########

menu()





