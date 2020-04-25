#!/usr/local/bin/python
import os, json

# Make sure we're on my personal AWS account
os.environ["AWS_PROFILE"] = "personal"

# Get the Instance ID
SPOT_INSTANCE_ID = os.popen("terraform output spot_instance_id").read().strip()

# Get Instance Status
INSTANCE_STATUS_JSON=os.popen("aws ec2 describe-instance-status --instance-id ${SPOT_INSTANCE_ID}").read()
INSTANCE_STATUS = json.loads(INSTANCE_STATUS_JSON)

# If it's not running, don't terminate
if not INSTANCE_STATUS['InstanceStatuses']:
  exit('Instance is not running, quitting.')

# Terminate
print('Terminating instance ' + SPOT_INSTANCE_ID)
RESULT = os.popen("aws ec2 terminate-instances --instance-ids "+ SPOT_INSTANCE_ID).read()
print('Done.')
