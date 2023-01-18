#function to accept elements to apply background
#I have used *tags because there is an unknown number of arguments to be entered into the function
#bgColor can be specified by user
def bgColor(*tags,bgColor,thisFile):
    for tag in tags:
        file=open(thisFile,'a+')
        file.writelines("<style>" + tag + "{background-color:"+bgColor+";}</style>")
        file.close()

#newStyle=bgColor("h1","h2",thisFile="index.html",bgColor=input("BG COlor"))

def bgImage(*tags,bgImage,thisFile):
    for tag in tags:
        file=open(thisFile,'a+')
        file.writelines("<style>"+tag +"{ \n"
                                        "background-image:url("+bgImage+");\n"
                                        "margin-left:100px;\n"
                                        "}</style>")
        file.close()
#newbgImage=bgImage("body",bgImage=input("path to bg image"),thisFile="index.html")

def noBorder(*tags,thisFile):
    for tag in tags:
        file=open(thisFile,'a+')
        file.writelines("<style>"+tag+"{border-style: none;}")
        file.close()

def dottedBorder(*tags,thisFile):
    for tag in tags:
        file=open(thisFile,'a+')
        file.writelines("<style>"+tag+"{border-style: dotted;}")
        file.close()

#newBorder=dottedBorder("h1",thisFile="index.html")

def dashedBorder(*tags,thisFile):
    for tag in tags:
        file=open(thisFile,'a+')
        file.writelines("<style>"+tag+"{border-style: dashed;}")
        file.close()

newBorder=dashedBorder("h2",thisFile="index.html")


