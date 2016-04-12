import httplib
import json
import argparse
import time
from datetime import datetime

aparser = argparse.ArgumentParser()
aparser.add_argument("URL", help="server:port of szambelan server", default="127.0.0.1:8080", nargs='?')
aparser.add_argument("dev", help="device id", default="test-client01", nargs='?')
args = aparser.parse_args()

#httplib.HTTPConnection._http_vsn = 10
#httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'


req = {
    "ver": "0.1",
    "dev": args.dev,
    "frames": [
        {
            "fid": str(time.time()),
            "ts" : datetime.now().isoformat(),
            "raw": "01 5a 41 42 43 44 00 00 00 00 0a 58 01 1a 00 00 00 01 a6 9a 00 00 00 00 07 bb",
        }
    ]
}

print req
print json.dumps(req)

def printText(txt):
    lines = txt.split('\n')
    for line in lines:
        print line.strip()

headers = {
    "Content-type": "application/json",
#    "Accept": "application/json",
}


svc = httplib.HTTPConnection(args.URL)
svc.set_debuglevel(65535)
svc.connect()

quote = "test"
#svc.request('POST', '/log', json.dumps(req))
svc.request('POST', '/log', json.dumps(req), headers)

response = svc.getresponse()
print response.status
if response.status == httplib.OK:
    print "Output from CGI request"
    printText (response.read())

svc.close()