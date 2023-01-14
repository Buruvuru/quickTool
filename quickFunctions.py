# This function sets the file name
def fileName(thisFileName):
    open(thisFileName, 'a+')

# Set doctyp
def setDoctype(thisFileName, doctype):
    file = open(thisFileName, 'a+')
    file.writelines("<!DOCTYPE html>")
    file.close()

# Set title of the file
def setTitle(thisFileName, title):
    file = open(thisFileName, 'a+')
    file.writelines("<title>" + title + "</title>")
    file.close()

def startBodyTag():
    tag = "<body>"
    return tag

def endBodyTag():
    tag ="</body>"
    return tag

def h1Tag(thisFile,content):
    file=open(thisFile,'a+')
    file.writelines("<h1>" + content + "</h1>")





fileName("index.html")
setTitle("index.html", "This is my title")
