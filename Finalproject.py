from bs4 import BeautifulSoup
import requests

search=input("search :")
while (search!="x"):
    #url = input("Enter a website to extract the data from: ")
    #r  = requests.get("http://" +url)


    r  = requests.get("https://www.olx.com.pk/cars/?search%5Bdescription%5D=1&page=5")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("h3",class_="large lheight20 margintop10"):
            for link in atag.find_all('a'):
                text=(link.find('span').contents[0].strip())
                if search in text :
                    print(link.find('span').contents[0].strip())
                    print(link.get('href'))
                    print("___________________________________________________________________________________")

    r  = requests.get("https://www.olx.com.pk/cars/?search%5Bdescription%5D=1&page=4")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("h3",class_="large lheight20 margintop10"):
            for link in atag.find_all('a'):
                text=(link.find('span').contents[0].strip())
                if search in text :
                    print(link.find('span').contents[0].strip())
                    print(link.get('href'))
                    print("___________________________________________________________________________________")

    r  = requests.get("https://www.olx.com.pk/cars/?search%5Bdescription%5D=1&page=3")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("h3",class_="large lheight20 margintop10"):
            for link in atag.find_all('a'):
                text=(link.find('span').contents[0].strip())
                if search in text :
                    print(link.find('span').contents[0].strip())
                    print(link.get('href'))
                    print("___________________________________________________________________________________")
    r  = requests.get("https://www.olx.com.pk/cars/?search%5Bdescription%5D=1&page=2")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("h3",class_="large lheight20 margintop10"):
            for link in atag.find_all('a'):
                text=(link.find('span').contents[0].strip())
                if search in text :
                    print(link.find('span').contents[0].strip())
                    print(link.get('href'))
                    print("___________________________________________________________________________________")
    r  = requests.get("https://www.olx.com.pk/cars/")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("h3",class_="large lheight20 margintop10"):
            for link in atag.find_all('a'):
                text=(link.find('span').contents[0].strip())
                if search in text:
                    print(link.find('span').contents[0].strip())
                    print(link.get('href'))
                    print("___________________________________________________________________________________")

    r  = requests.get("https://www.carmudi.pk/cars/")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("h3",class_="item-title type-m"):
        for link in atag.find_all('a'):
            text=(link.get('href'))
            if search in text:
                print("https://www.carmudi.pk"+link.get('href'))
                print("___________________________________________________________________________________")
            
    r  = requests.get("https://www.carmudi.pk/cars/?sort=newest&page=2")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("h3",class_="item-title type-m"):
        for link in atag.find_all('a'):
            text=(link.get('href'))
            if search in text:
                print("https://www.carmudi.pk"+link.get('href'))
                print("___________________________________________________________________________________")
            
    r  = requests.get("https://www.carmudi.pk/cars/?sort=newest&page=3")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("h3",class_="item-title type-m"):
        for link in atag.find_all('a'):
            text=(link.get('href'))
            if search in text:
                print("https://www.carmudi.pk"+link.get('href'))
                print("___________________________________________________________________________________")
            
    r  = requests.get("http://www.pkmotors.com/used/car")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("div",class_="imagebox"):
        for link in atag.find_all('a'):
            text=(link.get('title'))
            print(link.get('href'))
            print("___________________________________________________________________________________")
        
    r  = requests.get("https://www.pakwheels.com/used-cars/search/-/")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("div",class_="col-md-9 grid-style"):
        for link in atag.find_all('a'):
            text=(link.find('h3').contents[0].strip())
            if search in text:
                print("https://www.pakwheels.com/"+link.get('href'))
                print("___________________________________________________________________________________")
            
    r  = requests.get("http://www.apnigari.com/cars_listing")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("div",class_="carstxtblak"):
        for link in atag.find_all('a'):
            print("http://www.apnigari.com/"+link.get('href'))
            print("___________________________________________________________________________________")
        
    r  = requests.get("http://www.apnigari.com/cars_listing/")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("div",class_="cl_carstxt"):
        for link in atag.find_all('a'):
            text=(link.get('href'))
            print("http://www.apnigari.com/"+link.get('href'))
            print("___________________________________________________________________________________")
        
    r  = requests.get("http://www.apnigari.com/cars_listing/page_2")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("div",class_="cl_carstxt"):
        for link in atag.find_all('a'):
            text=(link.get('href'))
            print("http://www.apnigari.com/"+link.get('href'))
            print("___________________________________________________________________________________")

    r  = requests.get("http://sastigari.com/search/cars/?condition=used&mk=&md=&price%5Bf%5D=&price%5Bt%5D=")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify())
    #print (soup.title.string)
    for atag in soup.find_all("a" ,class_="ia-card__title"):
        text=(atag.find('a').contents[0].strip())
        print(link.get('href'))
        print("___________________________________________________________________________________")
    search=input("search :")
