#!/usr/bin/env python
#import requests
import github3, json, os.path

from json_helpers import DateTimeEncoder

ORG = 'yuvaanshis'
REPO = 'new_batch'
GITHUB_TOKEN = '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'
FILENAME_ISSUES = ORG + 'issues.json'

data = {}

if os.path.isfile(FILENAME_ISSUES):
	f = open(FILENAME_ISSUES)
	data = json.load(f)
	f.close()

#gh = Github(GITHUB_TOKEN)
#gh = Github()
#gh = github3.login(token=GITHUB_TOKEN)
#gh = Github("GITHUB_TOKEN")
gh = github3.login(token=GITHUB_TOKEN)

if REPO not in data.keys():
	data[REPO] = {}

for i in gh.get_issues(ORG, REPO, state='all'):
	data[REPO][i.number] = {
		'created_at': i.created_at,
		'closed_at': i.closed_at,
		'is_pull_request': (i.pull_request is not None),
		'labels': [l.name for l in i.labels]
	}

f = open(FILENAME_ISSUES, 'w')
json.dump(data, f, cls=DateTimeEncoder)
f.close()
