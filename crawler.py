import click, requests
from bs4 import BeautifulSoup
 
@click.command()
@click.option('--query', help='Write the query to search on archlinux.org')
@click.argument('query', nargs=1)
 
def showDataThroughURL(query):
  urlQuery = "https://wiki.archlinux.org/index.php?search={}&title=Special%3ASearch&profile=default&fulltext=1".format(query)

  page  = requests.get(urlQuery)
  soup  = BeautifulSoup(page.text, 'html.parser')
  found = soup.find('span', {'class':'mw-headline'})

  if found is not None:
    print("[SPACE] - JUMP A PAGE \n[ENTER] - SCROLL DOWN\n[Q] - EXIT")
    
    foundUrl  = "https://wiki.archlinux.org" + soup.find('div', {'class': 'searchresults'}).find('li', {'class': 'mw-search-result'}).find('a')['href']
    foundPage = requests.get(foundUrl)
    foundSoup = BeautifulSoup(foundPage.text, 'html.parser')

    click.echo_via_pager(foundSoup.get_text())
  else:
    print("Page not found.")
 
if __name__ == '__main__':
  showDataThroughURL()