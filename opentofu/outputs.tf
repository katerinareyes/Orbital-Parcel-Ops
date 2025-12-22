output "api_endpoint" {
  value = aws_apigatewayv2_api.http_api.api_endpoint
}

output "rds_endpoint" {
  value = aws_db_instance.postgres.address
}

output "database_url" {
  value     = local.database_url
  sensitive = true
}