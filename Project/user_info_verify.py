

def get_user_info():
	Name = input("enter your name")
	Device_id = input("enter your unique device id")
	user_hash = input("enter your secret hash")
	user_info = [Name,Device_id,user_hash]
	return user_info