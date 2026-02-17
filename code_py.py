import qi

#Connexion à NAO
ip_robot = ""
port = 9559


session = qi.Session()
try:
	sesssion.connect (f"tcp://{ip_robot}:{port}")
	print ("Connexion réussie")
except RuntimeError:
	print("Impossible de se connecter au robot")
