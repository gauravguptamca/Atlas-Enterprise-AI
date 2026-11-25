from app.config import settings

print (f"AWS Region: {settings().aws_region}")
print (f"AWS Access Key ID: {settings().aws_access_key_id}")
print (f"AWS Secret Access Key: {settings().aws_secret_access_key}")
print (f"S3 Bucket: {settings().s3_bucket}")
print (f"Database URL: {settings().database_url}")
print (f"Bedrock Embed Model: {settings().bedrock_embed_model}")
