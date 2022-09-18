
import authorize as a
import hashlib
import data
def verify(nonce,block):
	#print('nonce in verify is',nonce)
	temp = (str(block)+str(nonce)).encode()
	hash_temp = hashlib.sha256(temp).hexdigest()
	#print("verify_user value ",hash_temp)
	return hash_temp

def get_user_verified(user_info):
	block = {'Name':user_info[0],'Device_id':user_info[1]}
	print('\n')
	#print('this is the stored blockchain ',a.blockchain)
	print('\n')
	blockchain = data.retrieve_data()
	for each in blockchain:
		if each['Device_id'] == block['Device_id']:
			if verify(each['Nonce'],each) == user_info[2]:
				return True

	return False

