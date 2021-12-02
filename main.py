import requests
from bs4 import BeautifulSoup
import re
import webbrowser
import searcher

anime_code = searcher.formator()

url = "https://gogoanime.wiki/"+anime_code
  

def get_gogo(url):
	# creating request object
	req = requests.get(url)
	  
	# creating soup object
	data = BeautifulSoup(req.text, 'html.parser')
	  
	# finding all li tags in ul and printing the text wimport reithin it
	data1 = data.find_all('iframe')

	link=re.findall('"([^"]*)"', str(data1))
	linkgogo  = link[5]
	return (f"https:{linkgogo}")


# import module
import codecs
  
# to open/create a new html file in the write mode
f = open('Anime.html', 'w')

# the html code which will go in the file GFG.html
html_template = """
<html>
<head>
<title>Anime</title>
</head>
<body>
<iframe width="560" height="315" src="{}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  
</body>
</html>
""".format(get_gogo(url))
print(get_gogo(url))
# writing the code into the file
f.write(html_template)
webbrowser.open('Anime.html')
# close the file
f.close()
input()