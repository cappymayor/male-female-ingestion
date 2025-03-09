# Create a backend state file
terraform {
  backend "s3" {
    bucket  = "random-profile-terraform-state-bucket"
    key     = "terraform.tfstate"
    region  = "eu-north-1"
    encrypt = true
  }
}
