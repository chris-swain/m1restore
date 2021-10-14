HOST = "192.168.1.1"
PORT = 5510
TIMEOUT = 3

import telnetlib
import time
import re
import sierrakeygen2
import luhn
import sys

#verify supplied imei is valid
newimei = sys.argv[1]

imeiverification = luhn.verify(newimei)

if imeiverification is False:
    print ('Not a valid IMEI Number!')
    sys.exit()
    
#connect to device
tn = telnetlib.Telnet(HOST, PORT, TIMEOUT)

#grab some information about the device
tn.write(b"ATI\r\n")
time.sleep(10)
atiresponse = tn.read_very_eager().decode('utf-8')

#grab the starting imei
imeipattern = "\r\nIMEI: (.*?)\\r\nIMEI SV:"
imei = re.search(imeipattern, atiresponse).group(1)
print("Device Current IMEI: " + imei)

#grab the openlock hash
tn.write(b"AT!OPENLOCK?\r\n")
time.sleep(10)
openlockresponse = tn.read_very_eager().decode('utf-8')
#DEBUG: print("Open lock response: " + openlockresponse)

#parse the response to a challenge
challenge = openlockresponse[15:-8]
print("Open Lock Challenge: " + challenge)

#keygen openlock hash
keygen = sierrakeygen2.SierraGenerator()
devicegeneration = "MDM9x40"
resp = keygen.run(devicegeneration, challenge, 0)
print("Key Generator Response: " + resp)

#throw that openlock hash over
print("Disabling Open Lock")
openlockwrite = "AT!OPENLOCK=\"" + resp + "\"\r\n"
tn.write(openlockwrite.encode('ascii'))
time.sleep(10)

#unlock imei
print("Unlocking IMEI")
tn.write(b"AT!NVIMEIUNLOCK\r\n")
time.sleep(10)

#parse new imei with checksum
print("Updating IMEI")
fullimei = luhn.append(newimei)
encryptimei = ','.join(fullimei[i:i + 2] for i in range(0, len(fullimei), 2))
encryptimeiwrite = "AT!NVENCRYPTIMEI=" + encryptimei + "\r\n"
tn.write(encryptimeiwrite.encode('ascii'))
time.sleep(10)

#reset router
print("IMEI Restored. Rebooting Router")
tn.write(b"AT!RESET\r\n")
tn.close()

#DEBUG: routerresponse = tn.read_very_eager().decode('utf-8')
#DEBUG: print("Router Response: " + routerresponse)
