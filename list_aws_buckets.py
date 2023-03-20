import boto3
import logging
import botocore
from botocore.exceptions import ClientError
import os

# Understanding imports in Python -Python 3 OOP (Dusty Phillips)
# import create_folder as cf
# from create_folder import handleRemoveReadonly as hrm
# from .HelloWorld.Classes import Point



s3 = boto3.resource('s3')
bucket = s3.Bucket('virtuallrwcardfleet')

def is_object_exists(path:str, bucket) -> bool:

    for object in bucket.objects.filter(Prefix=path):
        return True
    return False


def is_folder_empty(folder_name:str):
    count = bucket.objects.filter(Prefix= folder_name)
    print(len(list(count)))

# for bucket in s3.buckets.all():
#     print(bucket.name)
#     pass

# s3 = boto3.client('s3')
# response = s3.list_buckets()

# print("Existing buckets..")
# for bucket in response['Buckets']:
#     print(f'{bucket["Name"]}')


def download_s3_folder(bucket_name, s3_folder, local_dir=None):
    """
    Download the contents of a folder directory
    Args:
        bucket_name: the name of the s3 bucket
        s3_folder: the folder path in the s3 bucket
        local_dir: a relative or absolute directory path in the local file system
    """
    bucket = s3.Bucket(bucket_name)

    for obj in bucket.objects.filter(Prefix=s3_folder):
        target = obj.key if local_dir is None \
             else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        # if not os.path.exists(os.path.dirname(target)):
        #     os.makedirs(os.path.dirname(target))
        if obj.key[-1] == '/':
            continue
        bucket.download_file(obj.key, target)


def get_asm_certs_s3():

    print('check asm cert in s3')

    KEY =  '92/ASMCerts' # replace with your object key

    s3 = boto3.resource('s3')

    try:
        s3.Bucket(bucket).download_file(KEY, "ASMCerts/" )

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

def main():
    if is_object_exists('90/', bucket):
        print("Directory exists!")
    else:
        print("Directory not found..")

    folder = "92/ASMCerts"
    print(f"Number of items in {folder} folder: ")
    is_folder_empty(folder)

    # get_asm_certs_s3()

    # download_s3_folder("virtuallrwcardfleet",'87/IdentityCerts', '.\ID_99')



if __name__ == '__main__':
    main()