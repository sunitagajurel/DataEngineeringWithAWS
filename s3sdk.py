import boto3
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')




import uuid
def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response

first_bucket_name, first_response = create_bucket(
    bucket_prefix='firstpythonbucket', 
    s3_connection=s3_resource.meta.client)

# print(first_response)


# second_bucket_name, second_response = create_bucket(
#     bucket_prefix='secondpythonbucket', s3_connection=s3_resource)


# print(second_response)




def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name


first_file_name = create_temp_file(300, 'firstfile.txt', 'f')

print(first_file_name)

first_bucket = s3_resource.Bucket(name=first_bucket_name)
first_object = s3_resource.Object(
    bucket_name=first_bucket_name, key=first_file_name)






first_bucket = s3_resource.Bucket(name=first_bucket_name)
first_object = s3_resource.Object(
    bucket_name=first_bucket_name, key=first_file_name)



first_object_again = first_bucket.Object(first_file_name)


# using oibject

s3_resource.Object(first_bucket_name, first_file_name).upload_file(
    Filename=first_file_name)

first_object.upload_file(first_file_name)



# using Bucket

s3_resource.Bucket(first_bucket_name).upload_file(
    Filename=first_file_name, Key=first_file_name)

# client
s3_resource.meta.client.upload_file(
    Filename=first_file_name, Bucket=first_bucket_name,
    Key=first_file_name)


s3_resource.Object(first_bucket_name, first_file_name).download_file(
    f'/{first_file_name}') # Python 3.6+



def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)

copy_to_bucket(first_bucket_name, second_bucket_name, first_file_name)

