from urllib2 import urlopen,Request,URLError
import sys

#The starting page
startPage = "http://en.wikipedia.org/wiki/Formal_fallacy"

#The ending page
targetPage = "https://en.wikipedia.org/wiki/Philosophy"

#Required because wikipedia does not have entire urls inside HTML 
#If blank urls not changed
siteVisiting = "https://en.wikipedia.org"

#This is The string it matches to find url
referencingString = "\"/wiki/"

#This is the terminating string
terminatingString = "\""

#This is an optional 
offsetFromExtractedString = 1

#This is the maximum depth for searchi
maxDepth = 2


#Finds the next URL from the entire HTML string and adds it to the list
def getNextUrl(HTMLstring, URLlist):

    stringWithURL = HTMLstring[0:]
        
    urlIndex = stringWithURL.find(referencingString)
        
    if urlIndex == -1:
        
        return -1
    
    else:            
        stringWithURL = stringWithURL[urlIndex+offsetFromExtractedString:]
                
        urlEnd = stringWithURL.find(terminatingString)
            
        if urlEnd  ==-1:
            
            return -1
        
        else:
            url = stringWithURL[0:urlEnd]
            
            checkingURL =    siteVisiting+url
            
            URLlist.append(siteVisiting+url)

            return urlIndex+urlEnd+2
    
        


#Makes a list of URLs gathered from this particular URL
def makeURLlist(url):
    
    try:

        hdr = {'User-Agent': 'Mozilla/5.0'}
        
        urlString = "" + url 

        url = Request(url,headers = hdr)
        
        webInfo = urlopen(url)

        #print(urlString)

    except URLError:

        print("Could not open")

        #print(urlString)
        
        return []
    

        
    data = str(webInfo.read())
    
    webInfo.close()
    
    URLlist = []

    indexOfNext = 0
    
    while indexOfNext != -1:
        
        data = data[indexOfNext:] 
        
        indexOfNext = getNextUrl(data, URLlist)

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
        
            appendingList = makeURLlist(url)

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

    if depth > 0:
        alreadyVisited += listOfLists[depth-1]
    
    nextDepth = exploreDepth(listOfLists, depth, alreadyVisited)

    listOfLists.append(nextDepth)

    depth+=1











    



