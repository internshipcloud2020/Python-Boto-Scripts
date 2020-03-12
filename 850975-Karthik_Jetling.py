# To list all the IAM users in AWS.

import boto                                          #Python package
from boto import iam                          #Importing IAM module from boto.

connect=iam.IAMConnection()
iam_profile=connect.get_all_users()

for user in iam_profile.users:
    print(user.user_name)                       # Lists all the available IAM users. 