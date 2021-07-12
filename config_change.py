import os 

from netmiko import ConnectHandler
from csv import reader

# open file in read mode
with open('taget_devices.csv', 'r') as read_obj:

    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)

    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        
        #Convert list to string
        ip_add = ''.join(row)

        #User name and Password for Device
        user = admin
        pw = cisco

        #Sepcify the target device and Crendentials
        switch = {
            'device_type': 'cisco_ios', 
            'ip': ip_add, # row variable is a list that represents a row in csv
            'username': user, 
            'password': pw, 
            'port' : 22
        }

        #Adding Config set Commands
        add_snmp = [
                    'int fa1/0/1', 
                    'switchport mode access' ,
                    'switchport access vlan 100,
                    ]

        save = 'write mem'

        try: 
            c = ConnectHandler(**switch) #Passing Credentials to Connect Handler
            c.enable() #Enable Mode
            c.send_config_set(add_snmp) #Adding SNMP Config Lines
            output = c.send_command_expect(save)  #Save the Config
            print('SNMP config changed on '+ switch.get("ip"))
            c.disconnect() #Close the Connection

        except Exception as e: 
            print(e)
