### ajustar credencias de acesso

import boto3 #sdk aws

#Seleciona instancia da ec2 na região especifica
client = boto3.client('ec2', region_name='us-east-1')

def ec2_all():
    instances = []
    response = client.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['IntanceId']
            instance_name = instance['Tags'][0]['Value']
            instance_type = instance['InstanceType']
            instance_key = instance['Keyname']
            instance_state_code = instance['State']['Code']
            instance_state_name = instance['State']['Name']
            instance_privateid = instance['PrivateIpAddress']
            instance_subnetid = instance['SubnetId']
            instance_vpcid = instance['VpcId']
            
            #print(instance_id, instance_name, instance_type, instance_key, instance_state_code, instance_state_name, instance_privateid, instance_subnetid, instance_vpcid)

            temp_dict = {}
            temp_dict['instance_id'] = instance_id
            temp_dict['instance_name'] = instance_name
            temp_dict['instance_type'] = instance_type
            temp_dict['instance_key'] = instance_key
            temp_dict['instance_state_code'] = instance_state_code
            temp_dict['instance_state_name'] = instance_state_name
            temp_dict['instance_privateid'] = instance_privateid
            temp_dict['instance_subnetid'] = instance_subnetid
            temp_dict['instance_vpcid'] = instance_vpcid
            instances.append(temp_dict)
    return instances

def ec2_filter_by_id(instance_id):
    response = client.describe_instances(InstancesIds=[instance_id])

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['IntanceId']
            instance_name = instance['Tags'][0]['Value']
            return instance_name

def ec2_stop(instance_id):
    response = client.stop_instances(InstanceIds=[instance_id])

    current_state = response['StoppingInstances'][0]['CurrentState']['Name']
    previous_state = response['StoppingInstances'][0]['PreviousState']['Name']

    message = f'Instance ID: {instance_id} current state is {current_state} and the previous state is: {previous_state}'
    return message

def ec2_start(instance_id):

    response = client.start_instances(InstanceIds=[instance_id])
    current_state = response['StartingInstances'][0]['CurrentState']['Name']
    previous_state = response['StartingInstances'][0]['PreviousState']['Name']

    message = f'Instance ID: {instance_id} current state is {current_state} and the previous state is: {previous_state}'
    return message

'''
# pega o id e estado atual da maquina
all_ec2 = ec2_all()   
for ec2 in all_ec2:
    ec2_instanceid = ec2['instance_id']
    ec2_state_name = ec2['instance_state_name']
    ec2_name = ec2['instance_name']
    print(ec2_instanceid, ec2_name, ec2_state_name)

instance_id = '' #recebe o id e para a instance
'''