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

variable "enable_public_migrations" {
  description = "Si es true, habilita acceso público temporal a RDS para correr migraciones desde tu PC"
  type        = bool
  default     = false
}

variable "my_ip_cidr" {
  description = "IP pública (solo se usa si enable_public_migrations=true)"
  type        = string
  default     = ""
}
