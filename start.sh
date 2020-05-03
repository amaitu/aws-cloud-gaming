#!/bin/bash

export TF_IN_AUTOMATION=TRUE

# Terraform Apply
terraform apply -auto-approve > /dev/null

export TF_IN_AUTOMATION=FALSE
