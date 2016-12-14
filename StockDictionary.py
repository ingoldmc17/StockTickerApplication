
def createStockDict():
    '''Creates a dictionary with ticker as key & company name as value'''
    stockFile = open("listedCompanies2.0.csv","r") #open the file containing stocks and their symbols
    #print(stockFile.readlines())
    stockList = stockFile.readlines() #create a list of all elements in csv file
    stockDict = {} #create an empty dictionary that will hold stocks with symbols
    for i in range(len(stockList)-1): #loop through the list
        stockDict[stockList[i].split(',')[0]] = stockList[i].split(',')[1][:-1] #create key-value relationships for each company in stockDict
        i += 1
    stockFile.close()

    return stockDict




