import json

def handler(event, context):
    print(f"Received event: {json.dumps(event)}")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from your Terraform-managed Lambda!')
    }