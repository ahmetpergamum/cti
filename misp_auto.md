MISP Automation with Python or Curl
-----------------------------------

## Export ids rules from events
### python
[Sample code for python2](https://github.com/ahmetpergamum/cti/blob/master/exportEvents.py)
### curl
Sample curl command
```
curl -k -o rules.out --header "Authorization:Auth-key" https://misp/events/nids/suricata/download/false/false/tlp:green&&type:osint/2016-02-13/2016-02-29
```
