variable "aws_region" {
    type = string
    default = "us-west-1"
}

variable "project_name" {
  type    = string
  default = "orbital-parcel-ops"
}

variable "lambda_zip_path" {
  type        = string
  description = "Ruta al ZIP de la Lambda (build artifact)"
  default     = "lambda.zip"
}

variable "db_name" {
  type    = string
  default = "orbitalDB"
}

variable "db_username" {
  type    = string
  default = "orbital"
}

variable "db_instance_class" {
  type    = string
  default = "db.t3.micro"
}
