#!/usr/bin/env python

## Import(s) ##
from BeautifulSoup import BeautifulSoup
import util.file.fileutil as fu
import util.string.stringutil as stringutil
import os


absPath = 'D:\\project\\java\\aos\\ui\\dist\\module\\'
absHtmlPath = absPath+'index.html'
absTgtHtmlPath = absPath+'index1.html'

htmlContent = fu.read(absHtmlPath)
#print htmlContent

soup = BeautifulSoup(htmlContent)
csses = soup.findAll('link')


scripts = soup.findAll('script')
#print soup.prettify()
#print scripts

def getAbsPath(absParent,tags,attrName):
    res = []
    for t in tags:
        rpath = stringutil.removeTagAfter(t[attrName],'?')
        absPath = os.path.abspath(absParent + rpath)
        res.append(absPath)
    return res

tgtJsName = 'res.js'



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
