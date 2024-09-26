def enabled_OAuth_services():
    return {
        'google_oauth_user_account': True,
        'snowflake_oauth_user_account': False,
    }

def is_OAuth_fields_should_filter():
    return (x for x in enabled_OAuth_services() if x )


return is_OAuth_fields_should_filter()