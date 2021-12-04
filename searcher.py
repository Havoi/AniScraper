from bs4 import BeautifulSoup
import requests
import re


def searcher():
	search = input("Enter Anime Name: ")
	pageno = 5
	# Website URL
	recomd = [] 
	for x in range(1,pageno):
		URL = f'https://gogoanime.wiki//search.html?keyword={search}&page={x}'
		# Page content from Website URL
		page = requests.get( URL )
		 
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


def hypen(anime_code): 

    code=[]
    temp = None 
    for x in anime_code:
        code.append(x)
    # for x in code:
   
    #   if temp == x and x == "-":
    #       code[x].remove()
    #   temp = x
    length = len(code)
    
    # Iterating the index
    # same as 'for i in range(len(list))'
    for i in range(0,length):
        
        try:
            x = code[i]
        except:
            pass 
        if temp == x and x == "-":
            print(i)
            code.pop(i)
        temp = x

    
    return "".join(code)

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

	episode = input('Enter Valid episode No (1 for movies) :')
	anime_link= newstr+"-episode-"+episode
	new_link = hypen(anime_link)
	return new_link
