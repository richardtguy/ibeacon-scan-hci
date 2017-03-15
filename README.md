# ibeacon-scan-hci

Note that hcidump is not included in the standard Raspbian distribution.

`sudo apt-get install bluez-hcidump`

## To run the server as a systemd service

1. Ensure script `server.py` is executable
2. Create a new unit file `/lib/systemd/system/ibeacon.service`
```
[Unit]
Description=iBeacon Scanner Service

[Service]
ExecStart=/home/pi/ibeacon-scan-hci/server.py 0.0.0.0
StandardOutput=null

[Install]
WantedBy=multi-user.target
Alias=ibeacon.service
```
3. `sudo systemctl daemon-reload`
4. `sudo systemctl enable ibeacon.service`
5. `sudo systemctl start ibeacon.service`
6. `sudo systemctl status ibeacon.service`
```
● ibeacon.service - iBeacon Scanner Service
   Loaded: loaded (/lib/systemd/system/ibeacon.service; enabled)
   Active: active (running) since Wed 2017-03-15 15:55:01 UTC; 3s ago
 Main PID: 1800 (server.py)
   CGroup: /system.slice/ibeacon.service
           ├─1800 /usr/bin/python3 /home/pi/ibeacon-scan-hci/server.py 0.0.0.0
           └─1806 hcidump --raw -i hci0

Mar 15 15:55:01 pizero systemd[1]: Started iBeacon Scanner Service.
```
