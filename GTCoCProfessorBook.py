# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class cocprofessor:

    def __init__(self, baseUrl):
        self._baseUrl = baseUrl
        self.file = None



    #get professor urls for one page    

    def urlonepage(self, baseUrl, pageNumber):

        page = pageNumber
        if pageNumber == 1:

            url = baseUrl + "?title="
        else:
            url = baseUrl + "?title=" + "&page=" + str(pageNumber)

        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        try:
            request = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(request)


            content = response.read().decode('utf-8')
            pattern = re.compile('<h4 class=.name fn.><a href="(.*?)">(.*?)</a></h4>',re.S)
            items = re.findall(pattern,content)
            urls = []
            for item in items:
                _url = "http://www.cc.gatech.edu" + item[0]
                urls.append(_url)
            return urls


        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason
    #get total page number

    def pageTotalNumber(self, baseUrl):
        page = 1
        url = baseUrl
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        try:
            request = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(request)


            content = response.read().decode('utf-8')
            pattern = re.compile('<a title="Go to last page" href=".*?page=(.*?)">last',re.S)
            items = re.findall(pattern,content)
           # for item in items:
            #    _url = "http://www.cc.gatech.edu/" + item[0]
            return items[0]



        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason
    #use professor urls in one page to get target url
    def getDetailUrl(self, url):
        response = urllib2.urlopen(url)
        content = response.read().decode('utf-8')
        try:
            pattern = re.compile('<div class="field field-name-field-person-url-homepage.*?<a\shref="(.*?)">.*?</a>',re.S)
            tagetUrl = re.findall(pattern,content)


            if len(tagetUrl) == 0:

                return None
            else:
                return tagetUrl[0]


        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason


        

baseUrl = 'http://www.cc.gatech.edu/people/faculty'
#initial
cocp = cocprofessor(baseUrl)
#tptal pages
totalNumber = cocp.pageTotalNumber(baseUrl)
fileName =  "professorWebsite.txt"
f = open(fileName,"w+")

for i in range(1,int(totalNumber) + 1):
        

#for page one

    onePageUrls = cocp.urlonepage(baseUrl, i)
    count = 1
    for onePageUrl in onePageUrls:
        print onePageUrl
        iwant = cocp.getDetailUrl(onePageUrl)

        if iwant != None:
            prepareFile = iwant + "\n"
            f.write(prepareFile.encode('utf-8'))
           # floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
            #f.write("\n")

       
        
        print iwant

        count += 1  
    



    





