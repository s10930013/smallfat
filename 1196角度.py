import requests
import time
while 6==6:
    response = requests.get('https://norgay.center/php/vilsnodes.php?loadranging=1&project_id=1')
    str1 = response.text.split('Tag1196')
    str2= str1[1].split('"')
    str3= str2[9].split('\\')

    print(float(str3[0]))
    time.sleep(1.5)
123