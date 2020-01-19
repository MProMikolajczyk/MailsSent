def read_user_prop(prop):
    with open("config.txt", "r") as f:
        content  = f.readlines()
        userConfig = {}
        for line in content:
            key_config = line.split(':')[0].strip()
            value_config = line.split(':')[1].strip()
            userConfig[key_config] = value_config
        if prop == 'gmail_user':
            return userConfig['gmail_user']
        elif prop == 'gmail_password':
            return userConfig['gmail_password']
    f.close()