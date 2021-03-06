# ucs info credentials
UCSM_LOGIN = 'admin'
UCSM_PASSWORD = 'P@ssw0rd'
UCSM_IP = '10.94.140.115'

# Aci credentials will be gathered dynaically

VLAN_GROUP_DN = 'fabric/lan/net-group-aci-dvs-01'
DVS_NAME = 'aci-dvs-01'

UCSM_VIP_MAP = {
    '192.168.1.221': '10.94.140.117',
    '192.168.1.220': '10.94.140.117',
    '192.168.1.201': '10.94.140.115',
    '192.168.1.202': '10.94.140.115'
}

UCS = {
    '10.94.140.115': {
        "FI_A": '192.168.1.220',
        "FI_B": '192.168.1.221'
    },
    '10.94.140.117': {
        "FI_A": '192.168.1.201',
        "FI_B": '192.168.1.202'
    }
}

GARBAGE_COLLECTION_INTERVAL = 4
DELIMTER = "--"
