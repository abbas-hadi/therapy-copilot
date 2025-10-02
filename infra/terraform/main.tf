# Terraform skeleton - replace with real resources
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

# Add resources: s3, rds, ecs/eks, secrets manager
