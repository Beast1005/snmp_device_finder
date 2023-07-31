from netmiko import ConnectHandler
from pysnmp.hlapi import *

def take_traceroute(ip_address,host):
    oid = '1.3.6.1.2.1.1.5.0'
    error_indication,error_status,error_index,var_binds=next(
        getCmd(SnmpEngine(),
               CommunityData("secretkey"),
               UdpTransportTarget(host,161),
               ContextData(),
               ObjectType(ObjectIdentity(oid))
    )
    for var_bind in var_binds:
            print(f"Hostname: {var_bind[1]}")