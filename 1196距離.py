import requests
import time
import openpyxl
while 7==7:
    response = requests.get('https://norgay.center/php/vilsnodes.php?loadranging=1&project_id=1')
    str1 = response.text.split('Tag1196')
    str2= str1[1].split('"')
    str3= str2[5].split('\\')

    print(int(str3[0]))
    time.sleep(1.5)123