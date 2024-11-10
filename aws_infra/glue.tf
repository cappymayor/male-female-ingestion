# Create glue catalogue database
resource "aws_glue_catalog_database" "dev_dataplatform_database" {
  name        = "dev-male-female-ingestion"
  description = "dev database for data platform team for random profiles"

  tags = {
    Name        = "Data platform database"
    Environment = "Dev"
    owner       = "blessing_and_leo"
    team        = "Data Platform Team"
    managed_by  = "Mayowa"
    service     = "airflow"
  }
}
