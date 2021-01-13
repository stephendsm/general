import random #We dont need a bunch of img form website, but we only need eg; 1 img
import urllib.request #a package that allows us to get data from website

#Download an img from web
def download_web_image(url): #url = www...
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg' # name is just a random number(eg; 258), str(name) transform that number to 'string'
    urllib.request.urlretrieve(url, full_name) # (website, name_the_file)

download_web_image('https://upload.wikimedia.org/wikipedia/commons/b/b6/Felis_catus-cat_on_snow.jpg') #(webpage), remember paste it inside ''
