# DestinyScripts
Python scripts to pull information from Reddit related to Bungie's Destiny2 franchise 

There are two scripts in the main branch. Both scripts pull information from reddit.

One script pulls the Xur megathread and sends the text to a Slack channel via a webhook.
The other script pulls the Weekly Reset megathread and sends that data to Slack via a webhook.

Both scripts pull the data from DTG_Bot. DTG_Bot usually posts around the reset (Thursday 1pm EST for Xur and Tuesday 1pm EST for the weekly reset. I recommend setting an automated script to run this code (for instance crontab)

