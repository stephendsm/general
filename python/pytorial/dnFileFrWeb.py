from urllib import request

#download a CSV file from internet
#CSV file is just a comma separated value file
goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/TWTR?period1=1578595685&period2=1610218085&interval=1d&events=history&includeAdjustedClose=true'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url) #open website and store it in 'response'
    csv = response.read() #use that variable 'response' and read data from website
    csv_str = str(csv) #make gurantee the variable 'csv' to be string
    lines = csv_str.split("\\n") #whenever it comes across this new character '\\' in 'csv_str' it breaks it up
    dest_url = r'goog.csv' # r provides a special task where we can type like 'C:\bucky/..'
                           # 'goog.csv' is a file name which we are giving
    fx = open(dest_url, "w") #(file, 'w') # 'w' we want to read and write to it
    #we want to go throu that file now i.eloop it now so that we can read
    for line in lines:
        fx.write(line + "\n") #take that file 'fx' and we gonna write to it
                              #remember each line(i.e see lines) print a new line'\n'
    fx.close()

download_stock_data(goog_url)

