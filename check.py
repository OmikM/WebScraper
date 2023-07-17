import time, requests
from bs4 import BeautifulSoup
from notifications import sendMail

def check(Name,url,last_pkl,last_views,last_login,email):
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
            msg = Name+": Now you have"+str(pkl)+"PKLs. you have received"+str(pkl-last_pkl)+"\n"
            file.write(msg)
        if email!= None:
            sendMail(email, msg)
        last_pkl = pkl
    if views>last_views+1:
        with open("logs.txt", "a") as file:
            msg = Name+": Now you have str(views)"+str(views-(last_views+1))+"have viewd \n"
            file.write(msg)

    last_views = views
    last_login = Time
    return Name,url,last_pkl,last_views,last_login,email