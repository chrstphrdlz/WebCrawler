from urllib2 import urlopen,Request,URLError
import sys
import re

#The starting page
startPage = "http://www.python.org/"

#The ending page
targetPage = "http://www.python.org/about/apps/"

#Required because wikipedia does not have entire urls inside HTML 
#If blank urls not changed

#siteVisiting = "https://en.wikipedia.org"
siteVisiting = ""

#This is The string it matches to find url
referencingString = "\"http"

#This is the terminating string
terminatingString = "\""

#This is an optional 
offsetFromExtractedString = 1

#This is the maximum depth for searchi
maxDepth = 2


#Makes a list of URLs gathered from this particular URL
def makeURLlist(url, parentPage):

    if ("http" not in url) and ("https" not in url):
        url = parentPage + url
    
    try:

        hdr = {'User-Agent': 'Mozilla/5.0'}
        
        urlString = "" + url 

        url = Request(url,headers = hdr)
        
        webInfo = urlopen(url)

        print("opened " + urlString + "\n")

    except URLError:

        print("Could not open " + urlString + "\n")
        
        return []
    

        
    data = str(webInfo.read())
    
    webInfo.close()
    
    URLlist = []

    indexOfNext = 0

    '''while indexOfNext != -1:
        
        data = data[indexOfNext:] 
        
        indexOfNext = getNextUrl(data, URLlist)'''

    URLlist = re.findall("(?<=href=\").*?(?=\")", data)

    print("URL LIST size:    " + str(len(URLlist)))

    if len(URLlist)>0:
        URLlist.pop()

    URLlist = list(set(URLlist))    

    return URLlist


#Adds all urls connected from each URL at the specified depth to the List
#Ignores the already visited sites
def exploreDepth(List, depth, alreadyVisited):

    nextDepth = []
    #print("sdfvasfd")
    for url in List[depth]:

        if url not in alreadyVisited:

            #print("Zdfasdfg")
            if depth == 0:
                appendingList = makeURLlist(url, startPage)
            #Will have to find 
            else:
                appendingList = makeURLlist(url, startPage)

            if targetPage in appendingList:

                print("Took "+str(depth+1)+" pages to get to Philosophy")
                sys.exit()
            
            nextDepth = nextDepth + appendingList
        
    return nextDepth


url = [startPage]

depthZeroList = []

depth = 0

depthZeroList.append(url)

listOfLists = depthZeroList

alreadyVisited = []

while depth < maxDepth:

    print("\n\n\n\nCurrent Depth = " + str(depth))

    if depth > 0:
        alreadyVisited += listOfLists[depth-1]
    
    nextDepth = exploreDepth(listOfLists, depth, alreadyVisited)

    listOfLists.append(nextDepth)

    depth+=1











    



