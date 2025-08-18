import boto3

s3 = boto3.client('s3')

bucket_name = 'djmyhambucket'

lifecycle_policy = {
    'Rules': [
        {
            'ID': 'MoveToIA',
            'Prefix': '',
            'Status': 'Enabled',
            'Transitions': [
                {
                    'Days': 30,
                    'StorageClass': 'STANDARD_IA'
                },
            ],
            'Expiration': {
                'Days': 365
            }
        }
    ]
}

s3.put_bucket_lifecycle_configuration(
    Bucket=bucket_name,
    LifecycleConfiguration=lifecycle_policy
)

print(f"Lifecycle policy applied to {bucket_name}")
