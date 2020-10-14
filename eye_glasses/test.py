import requests
r = requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTE3xtyyV8Wd0sMscBgfNwttEECnZ8qUdqSag&usqp=CAU', allow_redirects=True)
open('test.jpg', 'wb').write(r.content)
