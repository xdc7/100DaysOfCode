"""
Write a script to print/ write all the access control information of S3 buckets in an AWS account. Optionally write the output to a JSON file

"""

# Importing boto3 to interact with AWS CLI in Python
import boto3, json 

# Establishing a session/ connection with AWS. Very important that you have the ~/.aws/credentials file present on your workstation
s = boto3.Session(profile_name='default')

# Creating an S3 resource from the boto3 session object
s3 = s.resource('s3')


# Opening a file to write the ACL results 
s3_acl_file = open('./s3_acl_file.json','a')

# Looping through all the accessible S3 buckets
for bucket in s3.buckets.all():
  # Getting the Acl object on each bucket
  acl = bucket.Acl()
  # Printing the grants dict in the acl object for this bucket
  print (acl.grants)
  # Wrting the results to a JSON file with indent to make it pretty
  json.dump(acl.grants, s3_acl_file, indent=4)
  
# Closing the file      
s3_acl_file.close()