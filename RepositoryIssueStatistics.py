from pygithub3 import Github
import datetime
from datetime import timedelta

def getLength(itr):
	sum=0
	for page in itr:
		for resouce in page:
			sum+=1
	return sum


gh = Github()

today = datetime.datetime.now()
yesterday = today - timedelta(1)
before7day = today - timedelta(7)
print yesterday
print before7day


repo_issues = gh.issues.list_by_repo(user="Shippable", repo="support")
repo_issues_24Hr = gh.issues.list_by_repo("Shippable", "support",**{"since":yesterday})
repo_issues_7days = gh.issues.list_by_repo("Shippable", "support",**{"since":before7day})

print "Calculating..."

openIssues = getLength(repo_issues)
openIssues24Hr = getLength(repo_issues_24Hr)
openIssues7days = getLength(repo_issues_7days)

print "Total Number of Open Issues: "+str(openIssues)
print "Number of open issues that were opened in the last 24 hours: "+str(openIssues24Hr)
print "Number of open issues that were opened more than 24 hours ago but less than 7 days ago: "+str(openIssues7days - openIssues24Hr)
print "Number of open issues that were opened more than 7 days ago: "+str(openIssues - openIssues7days)