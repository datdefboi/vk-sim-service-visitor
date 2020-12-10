import json
import vk_api

def read_credentials():
    return json.load(open("cred.json"))

def get_api():
    creds = read_credentials()
    vk_session = vk_api.VkApi(creds["login"], creds["pass"], scope=vk_api.VkUserPermissions.GROUPS)
    vk_session.auth(reauth=True)

    return vk_session.get_api()