from noaqi import ALProxy
import qi

#Connexion à NAO
ip_robot = "11.0.0.131"
port = 9559


session = qi.Session()
try:
	sesssion.connect (f"tcp://{ip_robot}:{port}")
	print ("Connexion réussie")
except RuntimeError:
	print("Impossible de se connecter au robot")
