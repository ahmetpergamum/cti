MISP Automation with Python or Curl
-----------------------------------

## Export ids rules from events
### Important

Boolen AND (&&) parameter works like OR for multiple tags

Issue discussion
[1](https://github.com/MISP/MISP/issues/2726)
[2](https://github.com/MISP/MISP/issues/2416)

### python
[Sample code for python2](https://github.com/ahmetpergamum/cti/blob/master/exportEvents.py)
### curl
Sample curl command
```
curl -k -o rules.out --header "Authorization:Auth-key" https://misp/events/nids/suricata/download/false/false/tlp:green&&type:osint/2016-02-13/2016-02-29
```

### PyMISP
Install pip3
```
sudo apt update
sudo apt -y install python3-pip
```
Requests module is a requirements check if it is installed
```
python3 -c "import requests"
echo $?
```
If ift is not installed
```
sudo pip3 install requests
```
Install pymisp from pip
```
pip3 install pymisp
```
Install pymisp latest version from repo
```
git clone https://github.com/MISP/PyMISP.git && cd PyMISP
git submodule update --init
pip3 install -I .
```
In the examples directory, you will need to change the keys.py.sample to enter your MISP url and API key.
```
cd /var/www/MISP/PyMISP/examples
cp keys.py.sample keys.py
vim keys.py
```

To test if your URL and API keys are correct, you can test with examples/last.py to fetch the last 10 events published.
```
python3 last.py -l 10
```
