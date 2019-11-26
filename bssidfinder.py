import requests, os

os.system('clear')
print("<//LYNEX TEAM//>")
print("[BSSIDFinder / coded by p1mpus]")

bssid = input("Enter BSSID: ")
print("")
ss = "http://mobile.maps.yandex.net/cellid_location/?clid=1866854&lac=-1&cellid=-1&operatorid=null&countrycode=null&signalstrength=-1&wifinetworks=" + bssid + ":-65&app=ymetro"
url = ss
r = requests.get(url)
print(r.text)
input("Enter...")
