import importlib

boto3_spec = importlib.util.find_spec('boto3')
boto3 = importlib.import_module('boto3') if boto3_spec is not None else None

def list_s3_objects(bucket_name):
    """
    List all objects in an S3 bucket.
    
    Args:
        bucket_name (str): Name of the S3 bucket
    """
    if boto3 is None:
        print("Error: boto3 is not installed. Install it with 'pip install boto3'.")
        return
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            print(f"Objects in bucket '{bucket_name}':")
            for obj in response['Contents']:
                print(f" - {obj['Key']} (Size: {obj['Size']} bytes)")
        else:
            print(f"Bucket '{bucket_name}' is empty.")

    except Exception as e:
        print(f"Error listing objects in bucket: {e}")
        
if __name__ == "__main__":
    bucket_name = "your-bucket-name"
    list_s3_objects(bucket_name)