import boto3

client = boto3.client(
    "bedrock",
    region_name="ap-south-1"
)

response = client.list_foundation_models()

for model in response["modelSummaries"]:
    print(model["modelId"])