import requests
from bs4 import BeautifulSoup
import time


# url but for this version it works only for my
url = ""

# path to file must be changed if python script will not be in the same folder as txt files 
# then it can look like it C:\\Users\\User\\Folder\\file

with open("pkl_data.txt", "r") as file:
    file = [i for i in file]
    last_pkl = int(file[0])
    last_views = int(file[1])
    last_login = file[2]
print(last_pkl,last_views,last_login)

while True:
    Time = time.strftime("%D:%H:%M:%S", time.localtime())
    with open("pkl_log.txt", "a") as file:
        file.write("______________________\n"+Time+'\n')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    b = soup.find_all('b')

    pkl = int(b[6].text)
    views = int(b[12].text[:-5])

    if last_pkl != pkl:
        with open("pkl_log.txt", "a") as file:
            file.write("Now you have"+str(pkl)+"PKLs. you have received"+str(pkl-last_pkl)+"\n")
        last_pkl = pkl
    if views>last_views+1:
        with open("pkl_log.txt", "a") as file:
            file.write(str(views-(last_views+1))+"People have viewd now its"+str(views)+"\n")

    with open("pkl_data.txt", "w") as file:
        file.write(str(pkl)+"\n")
        file.write(str(views)+"\n")
        file.write(Time)

    last_views = views
    last_login = Time

    # time program will wait in secounds before refreshing web 
    time.sleep(10000)