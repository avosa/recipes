terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}
provider "aws" {
  region = "<input-aws-region-eg-us-west-1>"
  access_key = "<input-your-aws-access-key>"
  secret_key = "<input-your-aws-secret-key>"
}
