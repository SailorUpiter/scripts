import sys
import redfish

# When running remotely connect using the iLO address, iLO account name, 
# and password to send https requests
iLO_host = "https://10.20.15.208"
login_account = "admin"
login_password = "5ruXurur!"

## Create a REDFISH object
REDFISH_OBJ = redfish.RedfishClient(base_url=iLO_host,username=login_account, \
                          password=login_password, default_prefix='/redfish/v1')

# Login into the server and create a session
REDFISH_OBJ.login(auth="basic")

# Logout of the current session
REDFISH_OBJ.logout()