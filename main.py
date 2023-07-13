import requests
from bs4 import BeautifulSoup
import time


# url but for this version it works only for my
url = ""

# path to file must be changed if python script will not be in the same folder as txt files 
# then it can look like it C:\\Users\\User\\Folder\\file

with open("data.txt", "r") as file:
    file = [i for i in file]
    last_pkl = int(file[0])
    last_views = int(file[1])
    last_login = file[2]
print(last_pkl,last_views,last_login)

while True:
    Time = time.strftime("%D:%H:%M:%S", time.localtime())
    with open("logs.txt", "a") as file:
        file.write("______________________\n"+Time+'\n')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    td_pkl = soup.find('td', style="font-weight:bold;color:#006934;font-size:24px;text-align:right;padding-right:4px;")
    a_pkl = td_pkl.find("a").text
    pkl = int(a_pkl.replace(" ", ""))

    p_views = soup.find('p', style="margin: 8px 0 0; color: gray; text-align: right; font-size: 8px;")
    b_views = p_views.find("b")
    views = int(b_views.text[:-5])

    if last_pkl != pkl:
        with open("logs.txt", "a") as file:
            file.write("Now you have"+str(pkl)+"PKLs. you have received"+str(pkl-last_pkl)+"\n")
        last_pkl = pkl
    if views>last_views+1:
        with open("logs.txt", "a") as file:
            file.write(str(views-(last_views+1))+"People have viewd now its"+str(views)+"\n")

    with open("data.txt", "w") as file:
        file.write(str(pkl)+"\n")
        file.write(str(views)+"\n")
        file.write(Time)

    last_views = views
    last_login = Time

    # time program will wait in secounds before refreshing web 
    print("yes sr")
    time.sleep(10000)