# DeepMole-PortScanner
A random order port scanner that can scan all 65535 ports in under 30 seconds

This python script will scan all 65535 ports and check which ones are open. Ports are scanned in random order in an attempt to avoid standard port scanning fingerprinting. 

The port scanner can be quite quick as it is possible to set the port response timeout variable, modifying this can greatly increase scan time. For instance, most devices on a network with sufficient bandwidth will respond on open ports within .01 seconds. 

---

## Usage: 

There are two variables that must be set by the user when the script is executed: 

1. IP address of target device
2. Port timeout variable (Valid options are any number or percent Ex: `1` `.01`

Example: 

`# python deepmole.py 10.1.1.1 .01`
