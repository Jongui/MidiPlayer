import json

# Loading resource file
def loadResourceData(locale, param):
    resource_name = "Resources/texts" + locale
    file = open(resource_name, "r")
    if file.mode == "r":
        ret = file.read()
        data = json.loads(ret)
    return data[param]
