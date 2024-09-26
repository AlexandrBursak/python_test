auth_types = ['google_oauth_user_account', 'snowflake_oauth_user_account']
auth_fields_exclude = {
    'OAuthAccessToken',
    'OAuthAccountId',
    'OAuthRefreshToken',
    'OAuthType',
    'OAuthUsername',
}

params = {
    "jdbc_fields": [
        {'name': 'OAuthAccessToken', 'value': 'sdssdvsdvsd',},
        {'name': 'OAuthAccountId', 'value': 'sdssdvsdvsd',},
        {'name': 'someOtherField', 'value': 'sdssdvsdvsd',}
    ]
}

conf_int = 1

def enabled_OAuth_services():
    return {
        'google_oauth_user_account': True,
        'snowflake_oauth_user_account': False,
    }

def is_oauth_fields_should_filter():
    return list(k for k, v in enabled_OAuth_services().items() if v)


# print (is_OAuth_fields_should_filter())


associated_auth_types = [
    x for x in auth_types if x in auth_types[conf_int]
]

print(associated_auth_types, auth_types)


result = False
if associated_auth_types:
    current_services = set(set(associated_auth_types) & set(auth_types))
    available_fields = set(x.get('name') for x in params.get('jdbc_fields', []))
    print(current_services)
    if list(set(is_oauth_fields_should_filter()) & current_services) and list(available_fields & auth_fields_exclude):
        result = True
    print (result)
print ('Final result')
