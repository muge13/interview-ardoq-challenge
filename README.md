# Ardoq Assessment
## Question 1
### Challenge 
You have the following file content \
https://drive.google.com/open?id=18CkmWcXXlZZdJdzeVS8XIFgyuuf6EOcr \
How would you parse it to find if the oldest timestamp is older than 1 hour than the current time. If it is older to trigger some alarm of your choice slack message or email.
### Solution
The solution reads the daemon data file from the data folder, parses it and sends a notification to a slack channel if the condition is met. \
Requires SLACK_API_TOKEN environment variable \
Example command below \
```SLACK_API_TOKEN="{api_token}" python q1/main.py```
## Question 2
### Challenge
You have the test.json file url.
https://drive.google.com/open?id=1fQPNwD65XdbI3iu7ujCppxN7NWv9NUKL
Can you write an ansible playbook to get the file from the link and send one slack message with all the labels of the organizations:
a) that have "plan_id"== trial AND "days-remaining-trial" bigger than "0"  AND  status=="in_trial"
b) other than these with plan_id==trial OR plan_id=employee.
### Solution
The playbook fetches the json file, parses and escapes it,runs the queries based on the conditions and sends the slack message \
Requires SLACK_API_TOKEN environment variable \
Example command below 

```SLACK_API_TOKEN="{new_api_token}" ansible-playbook q2/main.yml```
## Question 3
### Challenge
If you have to do the same as in task 2 but with some linux command line tools, how would you approach this ?
### Solution
The bash executable fetches the file,escapes it,parses and runs the queries based on the conditions,,using jq, and sends the slack message \
Requires SLACK_API_TOKEN environment variable \
Example command below \
```SLACK_API_TOKEN="{new_api_token}" ./q3/main.sh```