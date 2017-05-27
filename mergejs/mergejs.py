#!/usr/bin/env python

## Import(s) ##
from bs4 import BeautifulSoup
import util.file.fileutil as fu
import util.string.stringutil as su
import util.common.dateutil as du
import os

# url = 'http://10.118.12.153:1080'
url = 'http://aa.com'

absParentPath = 'D:\\project\\java\\esg-aos-core-ui\\code\\dist\\'
absModulePath = absParentPath+'module\\'
absTgtPath = absParentPath+'merge\\'

if fu.exist(absTgtPath):
    fu.deleteDir(absTgtPath)

fu.mkdir(absTgtPath)


#source html
absHtmlPath = absModulePath+'index.html'

#target html
absTgtHtmlPath = absTgtPath + 'index.html'
absTgtJsPath = absTgtPath + 'main.js'
# absTgtCssPath = absTgtPath + 'main.css'

htmlContent = fu.read(absHtmlPath)

soup = BeautifulSoup(htmlContent, "html.parser")

scripts = soup.findAll('script')

def getAbsPath(absParent,tags,attrName):
    res = []
    for t in tags:
        rpath = su.removeTagAfter(t[attrName],'?')
        absPath = fu.getAbsPath(absParent,rpath)
        res.append(absPath)
    return res

absScripts = getAbsPath(absModulePath,scripts,'src' )
print 'src abs script:',absScripts

def cpFiles(filePaths,tgt):
    content = ''
    for f in filePaths:
        #print f
        #fileName = su.getTagAfter(f,'\\')
        #print 'tgtf:'+fileName
        content += fu.read(f)
    fu.write(tgt,content)

# cpFiles(absHtmlPath,absTgtHtmlPath)

cpFiles(absScripts,absTgtJsPath)

[s.extract() for s in soup(['script','link'])]


version = du.getNow(du.MMDDHHMM)

# newcss = soup.new_tag("link",href="http://.com/content/css?name=main&ver=0516")

# newcss = soup.new_tag("link",href=url+"/content/getstyles?name=main&ver="+version,rel="stylesheet",type="text/css")


# newcss = '<link rel="stylesheet" type="text/css" href="{0}" />'.format("http://10.118.12.118:1080/content/css?name=main&ver=0516")
# print newcss


# soup.head.append(newcss)

# newscript = soup.new_tag("script",href="http://.com/content/js?name=main&ver=0516")

newscript = soup.new_tag("script",src=url+"/content/getscript?name=main&ver="+version,type="text/javascript")
# newscript = "<script type=\"text/javascript\" src=\"{0}\"/>".format("http://10.118.12.118:1080/content/js?name=main&ver=0516")
#,type="text/javascript")
print newscript
soup.body.append(newscript)

htmlContent = soup.prettify()
htmlFmtContent = htmlContent.replace('amp;','')
# for c in htmlContent:
#     print 'raw '+c
#     print 'after ' +c.replace('amp;','')
#     htmlFmtContent += c.replace('amp;','')

print 'res:'+htmlFmtContent
fu.write(absTgtHtmlPath, htmlFmtContent)



'''
merge js
'''
if len(scripts)>1:
    absScripts = getAbsPath(absPath,scripts,'src')
    tgtScript = absPath+ tgtJsName
    print absScripts
    mergedContent = ''
    for f in absScripts:
        content = fu.read(f)
        mergedContent+=content
    fu.deleteFile(tgtScript)
    fu.write(tgtScript,mergedContent)

# for s in scripts:
#     rpath = stringutil.removeTagAfter(s['src'],'?')
#     print os.path.abspath(absPath+rpath)
