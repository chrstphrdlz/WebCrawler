from urllib.request import urlopen,Request


def getNextUrl(HTMLstring, URLlist):
    stringWithURL = HTMLstring[0:]
        
    #print(stringWithURL)
        
    urlIndex = stringWithURL.find("\"http")
        
    if urlIndex == -1:
        
        return -1
    
    else:            
        stringWithURL = stringWithURL[urlIndex+1:]
            
        urlEnd = stringWithURL.find("\"")
            
        if urlEnd  ==-1:
            
            return -1
        
        else:
            url = stringWithURL[0:urlEnd]
                
            URLlist.append(url)

            return urlIndex+urlEnd+2
    
        



def makeURLlist(url):

    try:
        #webInfo = urlopen(url)

        hdr = {'User-Agent': 'Mozilla/5.0'}
        
        url = Request(url,headers = hdr)
        
        webInfo = urlopen(url)

    except:
        
        print("Could not open")
        
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
    
    for url in List[depth]:

        if url not in alreadyVisited:
        
            appendingList = makeURLlist(url)
            
            nextDepth = nextDepth + appendingList
        
    return nextDepth

    
url = ['http://en.wikipedia.org/wiki/Uniform_resource_locator'] # write the url here

#print(makeURLlist(url))

depthZeroList = []

depth = 0

depthZeroList.append(url)

listOfLists = depthZeroList

alreadyVisited = []

while depth < 3:

    if depth >0:
        alreadyVisited += listOfLists[depth-1]
    
    nextDepth = exploreDepth(listOfLists, depth, alreadyVisited)

    listOfLists.append(nextDepth)

    depth+=1

print(listOfLists)










    

