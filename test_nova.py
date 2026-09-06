import os

import boto3

os.environ.setdefault("AWS_DEFAULT_REGION", "ap-south-1")

from agents.jan_sahayak import create_agent

def test_nova():
    print("Testing Nova 2 Lite model on Bedrock...")
    try:
        credentials = boto3.Session().get_credentials()
    except Exception as error:
        raise RuntimeError(f"AWS credentials could not be loaded: {error}") from error

    if credentials is None:
        raise RuntimeError(
            "No AWS credentials found. Set AWS_BEARER_TOKEN_BEDROCK or "
            "configure AWS CLI credentials or an AWS profile."
        )

    agent = create_agent()
    response = agent("Hi, I want to report a broken streetlight on Main Street.")
    print("Success! Agent responded:")
    print(response)

if __name__ == "__main__":
    test_nova()
