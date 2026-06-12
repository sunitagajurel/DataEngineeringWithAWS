terraform {
}

resource "aws_s3_bucket" "app_bucket" {
  bucket = "de/day-5"
}

resource "aws_s3_bucket_versioning" "versioning_1" {
  bucket = aws_s3_bucket.app_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}