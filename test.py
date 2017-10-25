import boto3

cf = boto3.client('cloudformation')

print('Creating cloudformation stack')
response = cf.create_stack(
    StackName='aa-stack-test',
    TemplateURL='https://s3.amazonaws.com/aa-coreo-test/demo_agent.json',
    Parameters=[
        {
            'ParameterKey': 'CCAgentTokenKeyID',
            'ParameterValue': '599b8bfa28e49900d98abd8d'
        },
        {
            'ParameterKey': 'CCAgentTokenSecretKey',
            'ParameterValue': 'f25cfc2fe338f86b7ea6'
        }
    ]
    
)
print('Successfully created stack:')
print(response)
