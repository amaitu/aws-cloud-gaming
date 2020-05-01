#!/bin/bash

export TF_IN_AUTOMATION=TRUE

# Terraform Apply
terraform apply -auto-approve > /dev/null

instance="${terraform output spot_instance_id}"

export TF_IN_AUTOMATION=FALSE
