import boto3
import logging
import botocore
from botocore.exceptions import ClientError
import os

# Understanding imports in Python -Python 3 OOP (Dusty Phillips)
# import create_folder as cf
# from create_folder import handleRemoveReadonly as hrm
from HelloWorld.Classes import Point


s3 = boto3.resource("s3")
bucket = s3.Bucket("")


def is_object_exists(path: str, bucket) -> bool:

    for object in bucket.objects.filter(Prefix=path):
        return True
    return False


def is_folder_empty(folder_name: str):
    count = bucket.objects.filter(Prefix=folder_name)
    print(len(list(count)))


# for bucket in s3.buckets.all():
#     print(bucket.name)
#     pass


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
        target = (
            obj.key
            if local_dir is None
            else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        )
        # if not os.path.exists(os.path.dirname(target)):
        #     os.makedirs(os.path.dirname(target))
        if obj.key[-1] == "":
            continue
        bucket.download_file(obj.key, target)


def get_asm_certs_s3():

    print("check asm cert in s3")

    KEY = ""  # replace with your object key

    s3 = boto3.resource("s3")

    try:
        s3.Bucket(bucket).download_file(KEY, "")

    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "404":
            print("The object does not exist.")
        else:
            raise


def check_bucket(bucketer):
    try:
        s3.meta.client.head_bucket(Bucket=bucketer)
        print("Bucket Exists!")
        return True
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = int(e.response["Error"]["Code"])
        if error_code == 403:
            print("Private Bucket. Forbidden Access!")
            return True
        elif error_code == 404:
            print("Bucket Does Not Exist!")
            return False


def main():
    # if is_object_exists('90/', bucket):
    #     print("Directory exists!")
    # else:
    #     print("Directory not found..")

    # s3 = boto3.client('s3')
    # response = s3.list_buckets()

    # print("Existing buckets..")
    # for bucket in response['Buckets']:
    #     print(f'{bucket["Name"]}')

    s3 = boto3.resource("s3")
    bucket = s3.Bucket("")

    check_bucket("")

    # if bucket.creation_date:
    #     print("The bucket exists")
    # else:
    #     print("The bucket does not exist")

    # folder = ""
    # print(f"Number of items in {folder} folder: ")
    # is_folder_empty(folder)

    # get_asm_certs_s3()

    # download_s3_folder("",'', '')

    # try:
    #     data_chunk_bucket.validate_bucket_name('')
    # except Exception as e:
    #     print(f"The following exception occurred: {e}\n")

    # print(data_chunk_bucket._generate_physical_name())
    # print(data_chunk_bucket._get_resource_name_attribute(data_chunk_bucket._physical_name))


if __name__ == "__main__":
    main()
