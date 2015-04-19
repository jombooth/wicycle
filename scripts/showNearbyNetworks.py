#!/usr/bin/python

import subprocess, os, sys, json

def py_grep(buf, s):
    def py_grep_w(buf, s, __outputs__):
        while len(buf) > 0 and buf[:len(s)] != s:
            buf=buf[1:]

        if buf[:len(s)] == s:
            __outputs__.append(buf.split('\n')[0])
            buf = "\n".join(buf.split('\n')[1:])

        if buf != "":
            return py_grep_w(buf, s, __outputs__)
    
        return __outputs__
    
    return py_grep_w(buf, s, [])
		

dev_null = open(os.devnull, 'w')

networks_raw = subprocess.check_output(["iwlist", "scan"], stderr=dev_null)
networks_raw_list = networks_raw.split("Cell")[1:]

networks_as_dicts = []

for network in networks_raw_list:
    
    d = {}
    try:
        d["SSID"] = py_grep(network, "ESSID:")[0].split(':')[1][1:-1] 
        if d["SSID"] == "":
            d["SSID"] = "<hidden>"
        d["Encrypted"] = "off" not in py_grep(network, "Encryption key:")[0]
        
        if d["Encrypted"]:
            d["EncryptionType"] = py_grep(network, "IE:")[0].split(':')[1].strip()
	else:
            d["EncryptionType"] = "Unencrypted"
        
        d["SignalStrength"] = py_grep(network, "Quality=")[0].split(' ')[0].split('=')[1]
        
        networks_as_dicts.append(d)
    except:
        print >> sys.stderr,  sys.exc_info()

print json.dumps(networks_as_dicts)
  
