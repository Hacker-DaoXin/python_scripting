import requests, sys, webbrowser, bs4,re

print('Googling...') # display text while downloading the Google
# res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
search_query=str(input('what you want to search: '))
res = requests.get('http://google.com/search?q=' + search_query)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'lxml')
# print(soup.prettify())
linkElems = soup.select('.kCrYT a')
f=open('google_url.txt','w')
for i in range(len(linkElems)):
    #webbrowser.open('http://google.com' + linkElems[i].get('href'))
    f.write(linkElems[i].get('href'))
    f.write('\n')
f.close()
print('Writing to the file')
f2=open('google_url.txt','r')
final=open('final_Gurl.txt','w')
a=f2.readlines()
for i in a:
    s=re.sub('^(/url\?q=)','',i)
    final.write(s)
f2.close()
final.close()
t=open('final_Gurl.txt','r')
a=t.readlines()
p=open('test.txt','a')
for i in range(len(a)):
    p.write(a[i].split('&')[0])
    p.write('\n')

