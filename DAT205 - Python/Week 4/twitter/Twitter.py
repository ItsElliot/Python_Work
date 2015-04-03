#Import nessary libraries
import twitter 
import datetime
import urllib2

#Get timestamp
now = datetime.datetime.today()

#Load Twitter keys and secrets from the txt file
file = open("TwitterCredentials.txt") 
cred = file.readline().strip().split(",") 
#Validate access 
api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],access_token_key=cred[2],access_token_secret=cred[3])

#Store Twitter ID
userID = 3121532979 

#Load and open current chrome browsing history
googleCurrentSession = open("/Users/Elliot/Library/Application Support/Google/Chrome/Default/Current Session") 
#Read last google session 
googleLastSession = googleCurrentSession.read() 

#Start and End the index of last session
indexStart = googleLastSession.rfind("http") 
indexEnd = googleLastSession.find(chr(0), indexStart) 

#Prepare last session page address
url = googleLastSession[indexStart:indexEnd] 
print(url)

urlreceived = urllib2.urlopen(url) 
html = urlreceived.read()

#Search through html page to find the <title> tags to get the title of last viewed page
beginTitle = html.find("<title>") + len("<title>") 
finishTitle = html.find("</title>", beginTitle)
title = html[beginTitle:finishTitle] 


#Publish on Twitter
mySession = api.PostUpdate("This is just amazing!: " + str(title) + "! You can find it on  " + url + str(now))
print("Status updated to: " + mySession.text)    