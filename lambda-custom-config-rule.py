import json,datetime,boto3

def lambda_handler(event, context):
    config_client = boto3.client('config')
  
    print("Event:",event)
    print("Context:",context)
    
    configuration_item=json.loads(event['invokingEvent'])['configurationItem']

    user_name=configuration_item['resourceName']
    resource_type=configuration_item['resourceType']
    resource_id=configuration_item['resourceId']
    ordering_timestamp=str(json.loads(event['invokingEvent'])['notificationCreationTime'])
    result_token=event['resultToken']
    
    response = config_client.put_evaluations(
      Evaluations=[
        {
            'ComplianceResourceType': resource_type,
            'ComplianceResourceId': resource_id,
            'ComplianceType': 'NON_COMPLIANT',
            'Annotation': user_name,
            'OrderingTimestamp': ordering_timestamp
        },
      ],
      ResultToken=result_token
    )
    print(response)
    
    return 1
