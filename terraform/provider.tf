terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}
provider "aws" {
  region = "us-east-1"
  access_key = "YOUR_AWS_ACCESS_KEY"
  secret_key = "YOUR_AWS_SECRET_KEY"
}

# provider "aws" {
#   region = "<input-aws-region-eg-us-west-1>"
#   access_key = "<input-your-aws-access-key>"
#   secret_key = "<input-your-aws-secret-key>"
# }
