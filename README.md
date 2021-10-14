M1 Restore v1.0 - by sodium (MOB)

IMEI Restore Utility for the Netgear Nighthawk M1 Hotspot Router

The goal for this project was to make it simple for anyone to restore / change
the IMEI on the Netgear Nighthawk M1.

I wrote it in python and have supplied the source and a complied version
for those that can't, or simply don't want to set up a python environment.

WARNING: I take no responsibility for what you do with this utility.

Usage:

m1restore.exe <new 15 digit imei>
Example: m1restore.exe 013364005176495

This is a command line based program. You should run it from the command line
on your Windows pc.

Step By Step Guide (FOLLOW THESE STEPS CAREFULLY!)
-----------------------------------------------------------------------------
1) Turn off the M1. Take out the battery and the sim card. It's important
that you leave the sim and battery out for the duration of this process.

2) Plug the M1 in to your computer via the USB cable. The device should power
up and indicate that a sim card is missing. Take a paper clip and hold down
the reset button for 10 seconds. The device should restore to factory settings.

3) After the device reboots in to factory default mode, it should connect via
tether to your computer. You may see your default browser try to load MSN. This
is typically what happens when the device is in USB Tether mode. If the
device doesn't enter tether, login to 192.168.1.1 via a web browser. The default
login is Admin / attwifi. Configure the device in the settings menu to tether
via usb.

4) After your PC is tethered to the device, you should be able to run the
m1restore.exe utility. Make sure you enter the correct IMEI number.

If you receive an error, you either didn't fully factory reset your device or
your device isn't in usb tether mode.

5) The device will boot after IMEI restore has completed. You can login to
the web interface to verify your IMEI was sucessfully updated. At this point
you can power down the device, put a sim card and the battery back in.
-----------------------------------------------------------------------------
Shouts: MOB, HCH, tophat, techn0_logic, jouser, kf.
B.Kerler for the sierrakeygen code.

What? You thought we retired?
