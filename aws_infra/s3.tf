# Create an S3 Bucket
resource "aws_s3_bucket" "dev_male_female_ingestion" {
  bucket = "dev-male-female-ingestion"

  tags = {
    Name        = "Data platform bucket"
    Environment = "Dev"
    owner       = "blessing_and_leo"
    team        = "Data Platform Team"
    managed_by  = "Mayowa"
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
