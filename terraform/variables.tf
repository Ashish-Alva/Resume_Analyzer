variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Project name used for tagging all resources"
  type        = string
  default     = "resume-analyzer"
}

variable "your_ip_cidr" {
  description = "Your local machine public IP in CIDR format e.g. 203.0.113.0/32"
  type        = string
}

variable "ec2_key_pair_name" {
  description = "Name of your EC2 key pair in ap-south-1"
  type        = string
}

variable "db_password" {
  description = "postgres"
  type        = string
  sensitive   = true
}

variable "db_username" {
  description = "postgres"
  type        = string
  default     = "postgres"
}

variable "db_name" {
  description = "Database name"
  type        = string
  default     = "resume_db"
}

variable "account_id" {
  description = "Your AWS account ID"
  type        = string
}