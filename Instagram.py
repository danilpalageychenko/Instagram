from selenium import webdriver
from time import sleep


#list_of_usernames = ["timatiofficial","urgantcom","buzova86","borodylia","samburskaya","ververa","instagram","pavelvolyaofficial","selenagomez","taylorswift","arianagrande","beyonce","kimkardashian","justinbieber","cristiano",
#"kyliejenner","kendalljenner","nickiminaj","therock","nike","natgeo","neymarjr","leomessi","khloekardashian","katyperry","mileycyrus","jlo",
#"ddlovato","kourtneykardash","victoriassecret","badgalriri","kevinhart4real"]
list_of_usernames = ["timatiofficial","urgantcom","buzova86","borodylia","samburskaya","ververa","instagram","pavelvolyaofficial","selenagomez","taylorswift"]



options = webdriver.ChromeOptions()

options.binary_location = "C:\Program Files\Opera\launcher.exe" # path to opera executable, even though it's in PATH :/
#options.binary_location = "C:\Program Files\Opera\operadriver.exe" # path to opera executable, even though it's in PATH :/

browser = webdriver.Opera(opera_options=options,executable_path="C:\Program Files\Opera\operadriver.exe")

browser.get("https://www.instagram.com/")

browser.add_cookie({'name' : 'csrftoken','value' : 'vnkDbyxoTJcmXjJ23ctkv1OJgCcoh7Gn', 'domain': 'www.instagram.com','path' : '/'})
browser.add_cookie({'name' : 'ds_user_id','value' : '527051324', 'domain': 'www.instagram.com','path' : '/'})
browser.add_cookie({'name' : 'sessionid','value' : 'IGSC137d3184acd1af4c2bfd903e96f4dbb3fc9c64f1520bd23d43255de21b8406f6%3AmYdT7UzeNZ8oE4E5SJlM8TOy0pO4f8Ru%3A%7B%22_auth_user_id%22%3A527051324%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22527051324%3AXlkAsSdO65aYjOQO1gjaPj0qIt56gpol%3A9aeeb2bd1bdf6197da3495d88a25cea06a0cc7cd5a8000712c6deb09d0590f1c%22%2C%22_platform%22%3A4%2C%22last_refreshed%22%3A1500291136.2224447727%2C%22asns%22%3A%7B%22time%22%3A1500291136%2C%2282.117.254.206%22%3A34248%7D%7D', 'domain': 'www.instagram.com','path' : '/'})
browser.add_cookie({'name' : 'mid','value' : 'WWydwgAEAAGOjRGWyzGW0rCyAb5W', 'domain': 'www.instagram.com','path' : '/'})
 
while(True):
    i=0
    for username in list_of_usernames:
        i+=1
        browser.get("https://www.instagram.com/"+list_of_usernames[i]+"/")
        




        code = """
            time=30;
            a=document.getElementsByClassName("_ah57t");
            function nakr() {a[0].click();}
            nakr();
            console.log("Script runned.");
            """
        a = browser.execute_script(code)
        print("Pressing button to "+username)
        #sleep(2)
        #element = browser.find_element_by_class_name('_ah57t')
        #if element.get_attribute("Class") == "_ah57t _84y62 _frcv2 _rmr7s":
        #    a = browser.execute_script(code)
        sleep(30)


