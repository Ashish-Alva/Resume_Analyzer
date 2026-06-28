output "ec2_public_ip" {
  description = "EC2 public IP — your application URL"
  value       = aws_eip.main.public_ip
}

output "rds_endpoint" {
  description = "RDS endpoint — use as DB_HOST in your .env"
  value       = aws_db_instance.postgres.address
}

output "s3_bucket_name" {
  description = "S3 bucket name — use as AWS_S3_BUCKET in your .env"
  value       = aws_s3_bucket.resumes.bucket
}

output "ecr_repository_url" {
  description = "ECR URL — use in Jenkinsfile and docker push commands"
  value       = aws_ecr_repository.app.repository_url
}

output "ssh_command" {
  description = "SSH command to connect to EC2"
  value       = "ssh -i YOUR_KEY.pem ec2-user@${aws_eip.main.public_ip}"
}