import os
import boto3
from moto import mock_aws
from moto_s3 import MyModel
import pytest

# os.environ["MOTO_ALLOW_NONEXISTENT_REGION"] = "True"


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    # os.environ["AWS_DEFAULT_REGION"] = "us-east-3"


@mock_aws
def test_my_model_save(aws_credentials):
    conn = boto3.client("s3")
    # We need to create the bucket since this is all in Moto's 'virtual' AWS account
    conn.create_bucket(Bucket="mybucket")

    model_instance = MyModel("steve", "is awesome")
    model_instance.save()

    # body = conn.Object("mybucket", "steve").get()["Body"].read().decode("utf-8")
    body = conn.get_object(Bucket="mybucket", Key="steve")
    body = body["Body"].read().decode()

    assert body == "is awesome"


# ******************** Testing other examples **********************************


@pytest.fixture
def aws(aws_credentials):
    with mock_aws():
        yield boto3.client("s3", region_name="us-east-1")


@pytest.fixture
def create_bucket1(aws):
    boto3.client("s3").create_bucket(Bucket="bb1")


@pytest.fixture
def create_bucket2(aws):
    boto3.client("s3").create_bucket(Bucket="bb2")


def test_s3_directly(aws):
    aws.create_bucket(Bucket="somebucket")

    result = aws.list_buckets()
    assert len(result["Buckets"]) == 1


def test_bucket_creation(create_bucket1, create_bucket2):
    result = boto3.client("s3").list_buckets()
    assert len(result["Buckets"]) == 2
