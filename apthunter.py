#!/usr/bin/env python

# Use the argparse library to simplify the command-line argument handling
# https://docs.python.org/3/library/argparse.html
import argparse

# Use the json library to simply the handling of JSON
# https://docs.python.org/3/library/json.html
import json

# This will parse the command-line arguments for our program
# Very simple example of JSON being used:
# python apthunter.py -wa '{"color":"Red"}'
parser = argparse.ArgumentParser(description="A program to hunt for Advanced Persistent Threats (APT).  It provides a command-line wrapper for the Federated Security Module(FSm) to query the indicies which contain sensor data in Elasticsearch.", prog="apthunter", epilog="Copyright 2019 Wade W. Wesolowsky")
parser.add_argument("-s",
	"--server",
	help="Hostname of the Elasticsearch server.",
	default="127.0.0.1")
parser.add_argument("-p",
	"--port",
	help="Port the Elasticsearch server is running on.",
	type=int,
	default=9200)
parser.add_argument("-ht",
	"--honeytrap",
	help="Search the honeytrap* index in Elasticsearch.  This index will contain HoneyTrap status messages and Honeypot connection attempts.",
	type=json.loads)
parser.add_argument("-log",
	"--logstash",
	help="Search the logstash-* index in Elasticsearch.  This index will contain Zeek network traffic monitoring information.",
	type=json.loads)
parser.add_argument("-pf",
	"--pfsense",
	help="Search the pfsense-* index in Elasticsearch.  This index will contain firewall status messages and Snort alerts.",
	type=json.loads)
parser.add_argument("-ss",
	"--sweetsecurity",
	help="Search the sweet_security index in Elasticsearch.  This index will contain detected device information and port scans.",
	type=json.loads)
parser.add_argument("-ssa",
	"--sweetsecurityalerts",
	help="Search the sweet_security_alerts index in Elasticsearch.  This index will contain new (unique) Sweet Security log events.",
	type=json.loads)
parser.add_argument("-t",
	"--tardis",
	help="Search the tardis index in Elasticsearch.  This index will contain historical hosts, IP addresses, and websites.",
	type=json.loads)
parser.add_argument("-wa",
	"--wazuhalerts",
	help="Search the wazuh-alerts-3.x-* index in Elasticsearch.  This index will contain log events above the alert thresholds in Wazuh.",
	type=json.loads)
parser.add_argument("-wm",
	"--wazuhmonitoring",
	help="Search the wazuh-monitoring-3.x-* index in Elasticsearch.  This index will contain all Wazuh monitoring logs.",
	type=json.loads)
parser.add_argument("--debug",
	help="Outputs useful information to find errors.")

# This gets the arguments!
args = parser.parse_args()

