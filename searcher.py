from bs4 import BeautifulSoup
import requests
import re


def searcher():
	search = input("Enter Anime Name: ")

	# Website URL
	URL = f'https://gogoanime.wiki//search.html?keyword={search}&page=1'


	# Page content from Website URL
	page = requests.get( URL )
	recomd = []  
	# parse html content
	soup = BeautifulSoup( page.content , 'html.parser')
	data = soup.find_all(class_ = "name")
	for tags in data:
		recomd.append(tags.get_text())
	print(f"{len(recomd)} anime available")
	no_of_recd = int(input("Enter No. of recommendations: "))
	for x in range(no_of_recd):
		if x<=len(recomd)-1:
			print(f"{x+1}) {recomd[x]}")
		if x>len(recomd)-1:
			print(f"Only {len(recomd)} anime available")
			break
	anime = int(input("Enter choice: "))
	main = recomd[anime-1]
	return main 

def formator():
	name= searcher()

	str1 = name.lower()
	new_text = re.sub(r"[^a-zA-Z0-9 ]", "", str1)
	newstr= ''
	for i in range(len(new_text)):
	    if new_text[i] == ' ':
	        newstr = newstr + '-'
	    else:
	        newstr = newstr + new_text[i]

	episode = input('Enter Valid episode No.: ')
	anime_link= newstr+"-episode-"+episode
	return anime_link

