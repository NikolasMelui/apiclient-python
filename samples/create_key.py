from voximplant.apiclient import VoximplantAPI, VoximplantException

if __name__ == "__main__":
    voxapi = VoximplantAPI("credentials.json")
    
    # Create a key pair.

    
    try:
        res = voxapi.create_key()
        print(res)
    except VoximplantException as e:
        print("Error: {}".format(e.message))
    
