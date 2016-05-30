# Concise Boto3 samples for common AWS services
This is a collection of concise python samples for instantiating and managing AWS compute infrastructure. Enjoy !

#### IAM
1. [Create New User](#create-new-user)
2. [Attach Access Policy to User](#attach-access-policy-to-user)

#### EC2
3. [Start EC2 Instance](#start-ec2-instance)
4. [Terminate EC2 Instance](#terminate-ec2-instance)

#### S3
1. [Create S3 Bucket](#create-s3-bucket)
2. [Attach Access Policy to User](#attach-access-policy-to-user)
3. [Put file in S3 Bucket](#put-file-in-s3-bucket)
4. [Delete Bucket](#delete-bucket)

#### DynamoDB
1. [Create DynamoDB User Policy](#create-dynamodb-user-policy)
2. [Create Table](#create-table)
3. [Update Table](#update-table)

## IAM
If you want to run and manage all your AWS infrastructure via python scripts then Amazon's Identity Access Management (IAM) service is the first component of the AWS infrastructure you should be aware of. Each time you start, update or end a service the boto3 call to do so _must_ be made by a user with the appropriate IAM permissions. To do this go to the AWS web console and create a new user with permission to create further IAM users and permissions. Since on AWS permissions are enocded in _policies_ I have done this by creating a new user called `root` and I've attached the `IAMFullAccess` policy to this user:

```
{
  "Version": "2012-10-17",
  "Statement": {
    "Effect": "Allow",
    "Action": "iam:*",
    "Resource": "*"
  }
}
```

Calling the user root here is not glib; by creating a user with full access to all IAM resources you really are creating a user with imperial authority to manage your AWS resources! Here this comes with all the usual caveats and warnings omitted but you can read about them elsewhere.
After creating a root user you can kiss the web UI goodbye and use boto3 and python for all subsequent tasks (hoorah!).

### Create New User
```python
code
```
(explanation)

### Attach Access Policy to User
```python

```
(explanation)


## EC2

### Start EC2 Instance
```python

```
(explanation)

### Terminate EC2 Instance
```python

```
(explanation)


## S3
### Create S3 Bucket
```python

```
(explanation)

### Attach Access Policy to User
```python

```
(explanation)

### Put file in S3 Bucket
```python

```
(explanation)

### Delete Bucket
```python

```
(explanation)


## DynamoDB
### Create DynamoDB User Policy
```python

```
(explanation)

### Create Table
```python

```
(explanation)

### Update Table
```python

```
(explanation)

