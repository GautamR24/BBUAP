import user_input as ui
import authorize as a
import user_info as u
import verify_user as vu
print("select your choice: ")
print("press 1: if you are a new user")
print("press 2: if you are already registered")
print("press q: to quit")

value = False

while(value != True):
	user_input = ui.get_user_input()
	if user_input == '1':
		user_info = u.get_user_info()
		if a.authorization_done(user_info):
			#key = provide_key(user_info)
			print("you are successfully registered")
		else:
			print("not registered")
	if user_input == '2':
		user_info = u.get_user_info()
		if vu.get_user_verified(user_info):
			print("you are logged in")
		else:	
			print("not logged in")
	if user_input == 'q':
		value = True