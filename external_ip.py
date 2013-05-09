#!/usr/bin/env python3
# Sample script to check external IP using http://checkip.dyndns.com/

try:
    import urllib.request as urllib2
except:
    import urllib2

import re

URL = "http://checkip.dyndns.com/"

def get_external_ip():
    res = urllib2.urlopen(URL)
    ex = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", str(res.read()))
    return ex[0]


if __name__=="__main__":
    print("External IP: %s" % get_external_ip())
