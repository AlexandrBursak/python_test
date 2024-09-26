import re

def validate_bucket_name(bucket_name):
    """
    Rules for the bucket name validation from google: https://cloud.google.com/storage/docs/buckets#naming
    """
    if len(bucket_name) < 3:
        return False

    if '.' in bucket_name:
        if len(bucket_name) > 222:
            return False

        components = bucket_name.split('.')
        if any(len(component) > 63 for component in components):
            return False

    elif len(bucket_name) > 63:
        return False

    """
    The Bucket name should: 
        - start and end with number or letter, 
        - can only contain lowercase letters, numeric characters, dashes (-), underscores (_), and dots (.)
    """
    if not re.match(r'^[a-z0-9]{1}[a-z0-9\-_.]+[a-z0-9]{1}$', bucket_name):
        return False

    # Google doesn't allow buckets to have IP-like format
    if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', bucket_name):
        return False

    return True

# Test the validation function
bucket_names = [
    "valid-bucket",
    "my.bucket",
    "bucket_verification",
    "1234567890.12345678901234567890123456789012345678901234567890.1234567890",
    "192.168.5.4",
    "goog-bucket",
    "mygooglebucket",
    "Bucket.name",
    "bucket.namE",
    "buckeT.name",
    "_bucket.name",
    "bucket.name.",
    "1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890.1234567890",
    "1234567890.1234567890.1234567890123456789012345678901234567890123456789012345678901234567890.1234567890",
]

for bucket_name in bucket_names:
    if validate_bucket_name(bucket_name):
        print(f"{bucket_name} is valid")
    else:
        print(f"{bucket_name} is NOT valid")