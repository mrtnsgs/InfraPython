import boto3
from ec2 import ec2_name_filter_by_id

client = boto3.client('ec2', region_name='us-east-1')
#response = client.describe_volumes()
print(response)

def ebs_get_volumes():
    volumes = []
    #lista todos os volumes e filtra
    for volume in response['Volumes']:
        volume_id = volume['VolumeId']
        volume_type = volume['VolumeType']
        volume_state = volume['State']
        instance_id = volume['Attachments'][0][InstanceId]
        instance_name = ec2_name_filter_by_id(instance_id)
        temp_dict['volume_id'] = volume_id
        temp_dict['volume_type'] = volume_type
        temp_dict['volume_state'] = volume_state
        temp_dict['instance_id'] = instance_id
        temp_dict['instance_name'] = instance_name
        volumes.append(temp_dict)
    return volumes

def ebs_get_volumes_available():
    response = client.describe_volumes(
        Filter=[
            {
                'Name': 'status',
                'Volues': [
                    'available', #(verificar na doc os status)
                ]
            },
        ],
    )
    count_volumes = response['Volumes']
    return len(count_volumes)

#print(response)
