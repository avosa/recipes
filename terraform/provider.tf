terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}
provider "aws" {
  region = "us-east-1"
  access_key = "AKIAQYRUJUK4APYVZLG4"
  secret_key = "xH7fPmxF2yHEw5TkkMxTCRRKRJ91OQ4i16H9Dx5J"
}

# provider "aws" {
#   region = "<input-aws-region-eg-us-west-1>"
#   access_key = "<input-your-aws-access-key>"
#   secret_key = "<input-your-aws-secret-key>"
# }