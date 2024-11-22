# Create glue catalogue database
resource "aws_glue_catalog_database" "dev_dataplatform_database" {
  name        = "random-profile"
  description = "dev database for data platform team for random profiles"

  tags = {
    Name        = "Data platform database"
    Environment = "Dev"
    owner       = "Data Platform Team"
    managed_by  = "Terraform"
    service     = "airflow"
  }
}
