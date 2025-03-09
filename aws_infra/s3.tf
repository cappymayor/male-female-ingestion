# Create an S3 Bucket
resource "aws_s3_bucket" "dev_male_female_ingestion" {
  bucket = "dev-male-female-ingestion"

  tags = {
    Name        = "Data Platform Bucket"
    Environment = "Dev"
    owner       = "Data Platform Team"
    managed_by  = "Terraform"
    service     = "airflow"
  }
}


# Enable bucket versioning
resource "aws_s3_bucket_versioning" "dev_male_female_ingestion_versioning" {
  bucket = aws_s3_bucket.dev_male_female_ingestion.id
  versioning_configuration {
    status = "Enabled"
  }
}
