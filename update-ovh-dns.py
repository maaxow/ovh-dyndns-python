import json
import ovh
import sys
from datetime import datetime
from requests import get

if len(sys.argv) == 1:
  sys.exit("Missing argument : python3 update-ovh-dns.py <domain>")

domain = sys.argv[1]
ip = get('https://api.ipify.org').text
client = ovh.Client(config_file='ovh.conf')

# get all records ids with filedType = 'A'
def getARecordsIds():
  return client.get('/domain/zone/' + domain + '/record', fieldType='A')

# get record details
def getRecord(id):
  return client.get('/domain/zone/' + domain + '/record/' + str(id))

# update a specific target record
def updateRecord(recordId, targetIp):
  client.put('/domain/zone/' + domain + '/record/' + str(recordId), target=targetIp)
  print(str(datetime.now()) + " DNS updated with " + targetIp)

# execute the script
def execute():
  recordsIds = getARecordsIds()
  for id in recordsIds:
    record = getRecord(id)
    target = record['target']
    if target != ip:
      updateRecord(id, ip)

execute()
