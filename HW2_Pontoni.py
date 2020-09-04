from bs4 import BeautifulSoup
import urllib
import csv
import os
import io

# 	Set WD
os.chdir('/Applications/GitHub/python_summer2020')


def petitions(page):
	with open('hw2_keenan.csv', 'w') as f:
		w = csv.DictWriter(f, fieldnames = ("Title" , "Published Date", "Issues", "Number of Signatures", "URL"))
		w.writeheader()
		#Per Patrick's example, open the website
		web_address = 'https://petitions.whitehouse.gov'
		web_page = urllib.request.urlopen(web_address)
		#Per Patrick's example,  parse the site
		soup = BeautifulSoup(web_page.read())
		pl = soup.find_all('article')
		petition = {}
		pl = soup.find_all('article')
		del pl[0]
		for i in range(0,20):
			#	"Title"
			a_tag = pl[i].find_all('a', href=True)
			petition["Title"] = a_tag[0].getText()
			#	"URL"
			petition["URL"] = "https://petitions.whitehouse.gov" + a_tag[0].get("href")
			#	"Number of signatures"
			span_tag = pl[i].find_all('span')
			petition["Number of Signatures"] = span_tag[1].getText ("signatures-number")
			#	"Issues"
			h6_tag = pl[i].find_all('h6')
			h6_list = []
			for k in range(0,len(h6_tag)):
				h6_list.append(h6_tag[k].getText())	
			petition["Issues"] = ", ".join(h6_list)
				#	"Creator" and "Published date"
			final = BeautifulSoup((urllib.request.urlopen(petition["URL"])).read())
			h4_tag = final.find_all('h4')[0]
			petition["Published Date"] = (h4_tag.getText())[1] 
			w.writerow(petition)
