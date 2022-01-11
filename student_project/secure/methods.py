from .models import Secure
import datetime
from .serializers import SecureSerializers
import jwt
import os
import json

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '_config', 'jwt_config.json')) as jwt_config_file:
    jwt_config = json.load(jwt_config_file)
    
class SecureCommonMethods():
    def register_user(data):
        try:
            try:
                userprofile_data=Secure.objects.get(username=data["username"])
                return {"success":False,
                        "error":{"error_id":"SECURE001",
                                "error_detail":"username already exist"
                                },
                                "status":400
                        }
            except Secure.DoesNotExist:
                new_data={}
                new_data=data
                new_data["entity_id"]="ENT"+datetime.now().strftime("%Y%m%d%H%M%S%f")
                serializer=SecureSerializers(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return {"success":True,
                            "status":200}
        except Exception as e:
            return {"success":False,
                        "error":{"error_id":"SECURE002",
                                "error_detail":str(e)
                                },
                                "status":500
                        }
                
    def Login(data):
        try:
            secure_data=Secure.objects.get(username=data["username"],password=data["password"])
            ser=SecureSerializers(secure_data)
            payload_data={
                "username":ser["username"],
                "entity_id":ser["entity_id"],
            }

            token_payload = payload_data
            # today_date=datetime.now().strftime("%Y-%m-%d")
            # if today_date <= token_payload["license_end_date"]:
            token = (jwt.encode(token_payload, jwt_config["secret"], algorithm=jwt_config["algorithm"])).decode('ascii')
            return {"success":True,
                    "token":token,
                    "status":200}
        except Exception as e:
            return {"success":False,
                        "error":{"error_id":"SECURE_log001",
                                "error_detail":str(e)
                                },
                                "status":500
                        }
            
    def verify_token(data):
        try:
            token = data.headers.get('Authorization')
            if(not(token)):
                return {"error_id": "SECURE_Tok001", "error_detail": "Token Not Found", "status":401}
            dec_token = jwt.decode(token, jwt_config["secret"], algorithm=jwt_config["algorithm"])
            return {"success":True,"data":dec_token,"status":200}
        except Exception as e:
            return {"error_id": "SECURE_tok002", "error_detail": str(e), "status":401}

            
    
            