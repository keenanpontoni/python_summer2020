##HW3
#Keenan Pontoni


import sys
import os
import io
import csv
import pandas as pd 
import numpy as np
import tweepy
import importlib

##per Patrick's lecture:

##I used the start_twitter .py file from github:
sys.path.insert(0, '/Users/keenanpontoni/Documents')
twitter = importlib.import_module('start_twitter')
api = twitter.client


wustlpolisci = api.get_user('WUSTLPoliSci')
wustlpolisci_followers = wustlpolisci.followers_ids()
len(wustlpolisci_followers)

followers = {}
for i in wustlpolisci_followers:
	followers[i] =  (api.get_user(i)).statuses_count 

wustlpolisci_active = max(followers, key=followers.get)
api.get_user(wustlpolisci_active).name

##Getting an output in non-English characters: '十勝餡粒々@アメリカPh.D.リベンジ'


followers_most = {}
for i in wustlpolisci_followers:
	followers_most[i] = (api.get_user(i)).followers_count

wustlpolisci_mostfollowers = max(followers_most, key=followers_most.get)
api.get_user(wustlpolisci_mostfollowers).name

##Brendan Nyhan has the most followers


##I used help from Alper for setting this up. Once I had the concept, I was able to taylor it to the extended situations.


three_types = {}
for i in wustlpolisci_followers:
	if followers_most[i] <= 100:
		three_types[i] = "Layman"
	elif (followers_most[i] <= 10000) and (followers_most[i] > 100):
		three_types[i] = "Expert"
	else:
		three_types[i] = "Celebrity"



wustlpolisci_friends = []
for friend in tweepy.Cursor(api.friends, id ="WUSTLPoliSci").items():
	wustlpolisci_friends.append(friend) 
len(wustlpolisci_friends)


##Output: 159

friends_dic = {}
for i in wustlpolisci_friends:
	friends_id = i.id
	friends_statuses = i.statuses_count 
	friends_dic[friends_id] =  friends_statuses



wustlpolisci_friends_active = max(friends_dic, key=friends_dic.get)
api.get_user(wustlpolisci_friends_active).name

##Output: The New York Times


friends_types = {}
for i in wustlpolisci_friends:
	friends_id = i.id
	friends_popularity = i.followers_count
	if friends_popularity <= 100:
		friends_types[friends_id] = "Layman"
	elif (friends_popularity <= 10000) and (friends_popularity > 100):
		friends_types[friends_id] = "Expert"
	else:
		friends_types[friends_id] = "Celebrity"


##Got stuck on pulling from here.


print(friends_types)
