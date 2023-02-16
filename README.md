Always get public ip address

Device : zte f670 
Hardware revision : v2.0

Installation requirements :
1. python 3
2. selenium==4.8.0
3. google chrome and chrome driver version >= 109 (make sure it's version matching)

This script run chrome in headless mode

Notes :
- adjust ont_ip as your configuration
- adjust ont_pass value to your ont superadmin password
- adjust line 21 and 38 to a reasonable directory path and file on your system
- adjust line 50 to a value that match to your VLAN number

Tested on Debian 10, may aplicable on other *nix OS
