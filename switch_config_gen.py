#!/usr/bin/python
# Used to generate Basic Brocade Switch Configurations

# Imports the regular expressions library
import re

def warning():
    print("#" * 60)
    print("It is your responsibility to verify")
    print("the validity of this configuration and information provided! ")
    print("#" * 60)
    print("USE AT YOUR OWN DISCRETION")
    print("#" * 60)

    gather_info()

#Gets necessary information to generate the configurations
def gather_info():
    print()
    print('#' * 40)
    print("Please provide the following information: ")
    print('#' * 40)

    customerID = input("Enter Customer ID (CID): ")
    customerName = input("Enter Customer Name: ")
    vlanID = input("Enter VLAN ID (xxxx): ")
    portDes = input("Enter the Port Designation x/x/xx: ")
    ip_range = input("Enter the valid IP address: ")
    cidr = input("Enter CIDR notation example (/29): ")
    ospf_area = input("Enter OSPF Area: ")
    ve = input("Enter VE (xxxx): ")
    xc = input("Enter closest neighbor (sh run | inc XC): ")

    validate_IP(ip_range)
    generate_config(customerID, customerName, vlanID, portDes, ip_range, cidr, \
                     ospf_area, ve, xc)

#Check for valid IP address
def validate_IP(ip_range):
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

    if(re.search(regex, ip_range)):  
        print("Valid Ip address")  
          
    else:  
        print("Invalid Ip address")
        break

#Generate FrontEnd and BackEnd configurations
def generate_config(customerID, customerName, vlanID, portDes, ip_range, cidr, \
                     ospf_area, ve, xc):

    print("")
    print("BACKEND")
    print("")
    print("enable")
    print("conf t")
    print("vlan " + vlanID)
    print("untag eth " + portDes)
    print("tag eth " + xc)
    print("end")
    print("")
    print("int eth " + portDes)
    print("port-name " + customerID+':'+customerName.replace(" ","")+"_"+vlanID)
    print("end")
    print("wr mem")
    print("")

    print("FRONTEND")
    print("")
    print("enable")
    print("vlan " + vlanID)
    print("untag eth " + portDes)
    print("router-interface ve " + ve)
    print("ip address " + ip_range+cidr)
    print("ip ospf area " + ospf_area)
    print("ip ospf passive")
    print("")
    print("int eth " + portDes)
    print("speed-duplex 1000-full-master")
    print("enable")
    print("int ve " + ve)
    print("enable")
    print("exit")
    print("wr mem")

warning()
