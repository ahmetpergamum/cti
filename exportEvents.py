#!/usr/bin/python

# exports iocs as a suricata ids rule
# tested in python2.7.12
# boolen AND (&&) parameter works like OR for multiple tags

import urllib2
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

MISP_HOST="https://misp"
API_KEY=""
# export tlp:green and(or?) APT tagged events
# either tagged events are fetched (boolen OR with &&)
EXPORT_DATA="/events/nids/suricata/download/false/false/tlp;green&&APT"
# export all events
#EXPORT_DATA="/events/nids/suricata/download"
OUTPUT_FILE="misp-suricata"

URL="%s/%s" % (MISP_HOST, EXPORT_DATA)
request = urllib2.Request(URL)
f = open(OUTPUT_FILE,'w')
request.add_header('Authorization', API_KEY)
data = urllib2.urlopen(request, context=ctx).read()
f.write(data)
f.close()
