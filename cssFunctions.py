#function to accept elements to apply background
#I have used *tags because there is an unknown number of arguments to be entered into the function
#bgColor can be specified by user
def bgColor(*tags,bgColor,thisFile):
    for tag in tags:
        file=open(thisFile,'a+')
        file.writelines("<style>" + tag + "{background-color:"+bgColor+";}</style>")
        file.close()

newStyle=bgColor("h1","h2",thisFile="index.html",bgColor=input("BG COlor"))





