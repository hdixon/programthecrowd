import boto3

region_name = 'us-east-1'
aws_access_key_id = 'AKIAI2MQSUNCDFGQCXMQ'
aws_secret_access_key = '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'

endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

# Uncomment this line to use in production
# endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'

client = boto3.client(
    'mturk',
    endpoint_url=endpoint_url,
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# This will return $10,000.00 in the MTurk Developer Sandbox
print(client.get_account_balance()['AvailableBalance'])
