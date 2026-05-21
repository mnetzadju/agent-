# Cisco Automation Engine using Netmiko
# Usage: python cisco_automation_engine.py
from netmiko import ConnectHandler

# Define list of devices
devices = [
    {'device_type': 'cisco_ios', 'host': '10.1.1.1', 'username': 'admin', 'password': 'password123'},
    {'device_type': 'cisco_ios', 'host': '10.1.1.2', 'username': 'admin', 'password': 'password123'}
]

commands = [
    'ntp server 10.1.1.100',
    'logging 10.1.1.200',
    'snmp-server community MyROComm RO'
]

def run_automation():
    for device in devices:
        try:
            print(f"Connecting to {device['host']}...")
            net_connect = ConnectHandler(**device)
            output = net_connect.send_config_set(commands)
            print(f"Output for {device['host']}:\n{output}")
            net_connect.save_config()
            net_connect.disconnect()
        except Exception as e:
            print(f"Failed to connect to {device['host']}: {e}")

if __name__ == "__main__":
    print("WARNING: Run this only in a controlled environment!")
    # run_automation() # Uncomment to run
