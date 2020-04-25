#!/bin/bash

# Make sure we're on my personal AWS account
export AWS_PROFILE=personal
export TF_IN_AUTOMATION=TRUE

# Terraform Apply
terraform apply -auto-approve > /dev/null

instance="${terraform output spot_instance_id}"

echo "Instance ${instance} is provisioning."

export TF_IN_AUTOMATION=FALSE
