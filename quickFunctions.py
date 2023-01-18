# This function sets the file name
def fileName(*filenames):
    for filename in filenames:
        open(filename, 'a+')

# Set doctype
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
    file.close()
def h2Tag(thisFile,content):
    file=open(thisFile,'a+')
    file.writelines("<h2>" + content + "</h2>")
    file.close()


fileName("index.html")
setTitle("index.html", "This is my title")
h1Tag("index.html","We are now in jerusalem")
h2Tag("index.html","We are now in Jerusalem")


