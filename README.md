# joycontrol-gui
Emulate Nintendo Switch Controllers over Bluetooth.

Tested on Ubuntu 19.10, and with Raspberry Pi 3B+ and 4B Raspbian GNU/Linux 10 (buster)

## Features
Emulation of JOYCON_R, JOYCON_L and PRO_CONTROLLER. Able to send:
- button commands
- stick state
- nfc data (WIP)

## Installation
- Install dependencies

Ubuntu: Install the `dbus-python` and `libhidapi-hidraw0` packages
```bash
sudo apt install python3-dbus libhidapi-hidraw0
```

Arch Linux Derivatives: Install the `hidapi` and `bluez-utils-compat`(AUR) packages


- Clone the repository and install the joycontrol package to get missing dependencies (Note: Controller script needs super user rights, so python packages must be installed as root). In the joycontrol folder run:
```bash
sudo pip3 install .
```
- Consider to disable the bluez "input" plugin, see [#8](https://github.com/mart1nro/joycontrol/issues/8)

## GUI usage
first run the `joycontrol_gui.py` file with sudo:
```bash
sudo python3 joycontrol.gui.py
```
and navigate to `Change Grip/Order` on your switch and wait for the program to connect

once connected the program will print out the bluetooth(not available from the system settings) mac address of the switch in the terminal, copy it and go to the `config.py` file and set the `switchMac` variable to your switch's mac address:
```python
switchMac = "AA:AA:AA:AA:AA"
# replace AA:AA:AA:AA:AA with your mac address
```
after configuring this you dont need to use sudo anymore and the program will automatically connect to your switch upon execution

`config.py` is also where you change the keybindings of the  program. examples of how to change it keybinding can be found in the file itself
## Issues
- Some bluetooth adapters seem to cause disconnects for reasons unknown, try to use an usb adapter instead 
- Incompatibility with Bluetooth "input" plugin requires a bluetooth restart, see [#8](https://github.com/mart1nro/joycontrol/issues/8)
- It seems like the Switch is slower processing incoming messages while in the "Change Grip/Order" menu.
  This causes flooding of packets and makes pairing somewhat inconsistent.
  Not sure yet what exactly a real controller does to prevent that.
  A workaround is to use the reconnect option after a controller was paired once, so that
  opening of the "Change Grip/Order" menu is not required.
- ...


## Resources

[Nintendo_Switch_Reverse_Engineering](https://github.com/dekuNukem/Nintendo_Switch_Reverse_Engineering)

[console_pairing_session](https://github.com/timmeh87/switchnotes/blob/master/console_pairing_session)
