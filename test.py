import boto3

s3 = boto3.client('s3')

print('Creating bucket')
response = s3.create_bucket(Bucket='aa-coreo-test')
print('Successfully created bucket')
