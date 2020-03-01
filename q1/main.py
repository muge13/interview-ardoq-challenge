import json
import re
from datetime import datetime,timedelta
import requests
import logging
import cfg
import os
from urllib3.exceptions import InsecureRequestWarning


with open("data/daemonEDN.data") as data_file:
    fetched_data = data_file.read()
def parse_data(data):
    data=fetched_data.split("\n")[1]
    #parse format
    parsed_data=re.sub(":([^, ]+)",r"'\1'",data)
    #parse digits
    parsed_data=re.sub("(\d+)|\"(.*?)\"",r"'\1\2'",parsed_data)
    #parse nils
    parsed_data=re.sub("nil","'nil'",parsed_data)
    #convert to json
    parsed_data=re.sub("' '","':'",parsed_data)
    parsed_data=re.sub("' {'","':{'",parsed_data)
    # parsed_data=re.sub(":([^, ]+)",r'\1',parsed_data)
    parsed_data=re.sub("'",'"',parsed_data)
    return parsed_data

json_data=json.loads(parse_data(fetched_data))
stream_pos=json_data['change-stream-position']
now = datetime.now()
timestamp = datetime.timestamp(now)
oldest_={
    'cluster-time': 
    {
        'time': datetime.timestamp(now), 
        'id': '0', 
        'inc': '0'}, 
        'tx-number': 'nil', 
        'resume-token': 'nil'
}
for val in stream_pos:
    cluster_time=int(stream_pos[val]['cluster-time']['time'])
    if cluster_time<int(oldest_['cluster-time']['time']):
        oldest_=stream_pos[val]

time_diff=int(datetime.timestamp(now - timedelta(hours=1)))

if int(oldest_['cluster-time']['time'])<time_diff:
    print("Sending notification")
    body="Record Found:"+"\n"+str(oldest_)
    channel = cfg.slack['channel']
    slack_token = cfg.slack['SLACK_API_TOKEN']
    data = {
        'token': slack_token,
        'channel': channel,
        'as_user': True,
        'text': body
    }
    
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    requests.post(url='https://slack.com/api/chat.postMessage',data=data)   
    print("Message sent")

