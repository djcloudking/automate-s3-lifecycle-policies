# AWS S3 Lifecycle Policy Project

This repository contains a **Python script that applies a lifecycle policy to an Amazon S3 bucket** using the **Boto3 SDK**.

The lifecycle policy automatically transitions objects to a lower-cost storage class (**STANDARD\_IA**) after 30 days and deletes them after 365 days. This project demonstrates how to use Python for **cloud cost optimization and storage management**.

---

## What You’ll Learn

* Using **Boto3** to interact with Amazon S3
* Defining and applying **lifecycle policies** to buckets
* Automating storage cost optimization strategies:

  * Move objects to **Infrequent Access (STANDARD\_IA)** after 30 days
  * Expire/delete objects after 365 days
* Writing Python scripts that integrate with AWS services

---

## Folder Structure

```
s3-lifecycle-policy/
├── s3_lifecycle.py
└── README.md
```

---

## Code Implementation

```python
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
```

---

## 🖥️ Example Output

When executed, the script confirms the policy:

```bash
Lifecycle policy applied to djmyhambucket
```

---

## Getting Started

### Prerequisites

* AWS account with **S3** access
* IAM user/role with permissions for:

  * `s3:PutLifecycleConfiguration`
  * `s3:GetLifecycleConfiguration`
* AWS CLI configured (`aws configure`)
* Python 3.8+ installed
* Boto3 installed:

  ```bash
  pip install boto3
  ```

### Clone the repo

```bash
git clone https://github.com/djcloudking/s3-lifecycle-policy.git
cd s3-lifecycle-policy
```

### Run the script

```bash
python3 s3_lifecycle.py
```

---

## Outcome

With this script, you:

* Automatically transition objects to **lower-cost storage classes** after a set number of days
* Ensure old/unused objects are automatically **deleted** after a year
* Reduce manual intervention in S3 data management
* Apply a **cost optimization best practice** in AWS

---

## Who This Is For

* Cloud engineers learning **S3 lifecycle rules**
* DevOps engineers implementing **cost optimization** strategies
* Developers practicing AWS automation with Python

---

## Related Projects

## Related Repos

This is part of a larger series of focused programming repositories.
Check out the [main hub](https://github.com/djcloudking/python-projects) for more.