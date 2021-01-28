import requests

url = input('link: ')
userdata = input('usuario data: ')
passdata = input('senha data: ')
inf = {userdata : 'jbxzjcbdsjbcjdsbcjdbsbcjsdbcbsdjcb', passdata : 'jbxzjcbdsjbcjdsbcjdbsbcjsdbcbsdjcb'}
rs = requests.post(url, data=inf)
print(rs.text)