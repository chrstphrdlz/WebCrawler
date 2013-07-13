from urllib2 import urlopen,Request
import sys
startPage = "http://en.wikipedia.org/wiki/Automobile"
targetPage = "http://en.wikipedia.org/wiki/Adolf_Hitler"
siteVisiting = "https://en.wikipedia.org"
referencingString = "\"/wiki/"
terminatingString = "\""
offsetFromExtractedString = 1
appendingString = ""


def getNextUrl(HTMLstring, URLlist):
    #print(HTMLstring)
    stringWithURL = HTMLstring[0:]
        
    #print(stringWithURL)
        
    urlIndex = stringWithURL.find(referencingString)
        
    if urlIndex == -1:
        
        return -1
    
    else:            
        stringWithURL = stringWithURL[urlIndex+offsetFromExtractedString:]
            
        #print(stringWithURL[0:25])
        urlEnd = stringWithURL.find(terminatingString)
            
        if urlEnd  ==-1:
            
            return -1
        
        else:
            url = stringWithURL[0:urlEnd]
            
            #print(url)

            URLlist.append(siteVisiting+url)

            return urlIndex+urlEnd+2
    
        



def makeURLlist(url):

    try:
        #webInfo = urlopen(url)

        hdr = {'User-Agent': 'Mozilla/5.0'}
        
        urlString = "" + url 

        url = Request(url,headers = hdr)
        
        webInfo = urlopen(url)

        print(urlString)

    except:

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

    
url = [startPage] # write the url here

#print(makeURLlist(url))

depthZeroList = []

depth = 0

depthZeroList.append(url)

listOfLists = depthZeroList

alreadyVisited = []

while depth < 2:

    if depth > 0:
        alreadyVisited += listOfLists[depth-1]
    
    nextDepth = exploreDepth(listOfLists, depth, alreadyVisited)

    listOfLists.append(nextDepth)

    depth+=1

print(listOfLists)










    

