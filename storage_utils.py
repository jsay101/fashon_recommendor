# Load credentials from environment variables or .env file
COS_API_KEY_ID = os.getenv('IBM_API_KEY')
COS_INSTANCE_CRN = os.getenv('IBM_SERVICE_INSTANCE_ID')
COS_ENDPOINT = 'https://s3.us-east.cloud-object-storage.appdomain.cloud'
BUCKET_NAME = 'cloud-object-storage-cos-standard-fashion-reco'
IBM_AUTH_ENDPOINT = 'https://iam.cloud.ibm.com/identity/token'

cos = ibm_boto3.client('s3',
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    ibm_auth_endpoint=IBM_AUTH_ENDPOINT,
    config=Config(signature_version='oauth'),
    endpoint_url=COS_ENDPOINT)

def upload_to_cos(file_path, filename):
    with open(file_path, 'rb') as file_data:
        cos.upload_fileobj(file_data, BUCKET_NAME, filename)

def download_file_from_cos(filename):
    with open(os.path.join('static/uploads', filename), 'wb') as file_data:
        cos.download_fileobj(BUCKET_NAME, filename, file_data)
