#!/bin/bash

# install jq
# apt-get install jq
# fetch json file
file_id="1fQPNwD65XdbI3iu7ujCppxN7NWv9NUKL"
filename="data/test.json"
curl -L -o ${filename} "https://drive.google.com/uc?export=download&id=${file_id}"
base=$(sed 's/-/_/g' ${filename}) 
WEBHOOK_URL="https://hooks.slack.com/services/${SLACK_API_TOKEN}"

# jq '.organzations[plan_id==`trial`].name' <<< "${first}"
first_parse=$(jq -r '.organzations[] | select((.plan_id=="trial") and (.status=="in_trial")and (.days_remaining_trial>0)) |.name' <<< "${base}")
second_parse=$(jq -r '.organzations[] | select((.plan_id=="trial") or (.plan_id="employee"))|.name' <<< "${base}")

echo "Sending Notification"
curl -X POST -H 'Content-type: application/json' --data '{"text":"First Parse:'"\n$first_parse"'\n\nSecond Parse:'"\n$second_parse"'"}' ${WEBHOOK_URL}
echo ""
echo "Notification Sent"