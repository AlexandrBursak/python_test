auth_types = ["google_oauth_user_account", "snowflake_oauth_user_account"]
associated_auth_types = ["basic", "snowflake_oauth_user_account"]
fields = [{"name": "address", "value": "google.com"}, {"name": "CLIENT_TIMESTAMP_TYPE_MAPPING", "value": "TIMESTAMP_NTZ"}, {"name": "db", "value": "TEST_DB"}, {"name": "application", "value": "DATAROBOT"}, {"name": "CLIENT_METADATA_REQUEST_USE_CONNECTION_CTX", "value": "true"}, {"name": "warehouse", "value": "DEMO_WH"}, {"name": "schema", "value": "PUBLIC"}, {"name": "OAuthAccessToken", "value": "${oauth_access_token}"}, {"name": "OAuthAccountId", "value": "${oauth_account_id}"}, {"name": "OAuthRefreshToken", "value": "${oauth_refresh_token}"}, {"name": "OAuthType", "value": "2"}, {"name": "OAuthUsername", "value": "${oauth_user_name}"}]
auth_fields = [
    "OAuthAccessToken",
    "OAuthAccountId",
    "OAuthRefreshToken",
    "OAuthType",
    "OAuthUsername"
]
# auth = filter(lambda x: x in associated_auth_types, auth_types)
auth = (x for x in auth_types if x in associated_auth_types)
print(len(list(auth)))

def qwerty(x):
    # print(x)
    return x.get("name") in auth_fields

field = filter(lambda x: x.get("name") in auth_fields, fields)
print(len(list(field)))

something = (x for x in fields if x.get("name") in auth_fields)
print(len(list(something)))

# when function is None
# (element for element in iterable if element)
