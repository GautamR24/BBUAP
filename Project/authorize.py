import data
import hashlib

#enesis_block = {'Name':'begin','Device_id':0,'index':1,'Nonce':0,'hash':0}
hash = []
blockchain = []
#blockchain.append(Genesis_block)
#data.save_data(blockchain)
#key = []
def valid_nonce(block,nonce,previous_block):
	guess = (str(block)+str(nonce)+str(previous_block)).encode()
	guess_hash = hashlib.sha256(guess).hexdigest()
	if guess_hash[0:2] == '00':
		hash.append(guess_hash)
		return True
	else:
		return False


def getUserData(name,id):
	block = {'Name':name,'Device_id':id}
	return block

def authorization_done(user_info):
	block = getUserData(user_info[0],user_info[1])
	print("block in new user ",block)
	blockchain = data.retrieve_data()
	previous_block = blockchain[len(blockchain)-1]
	Nonce = 1
	while not valid_nonce(block,Nonce,previous_block):
		Nonce += 2
	block['index']=len(blockchain)+1
	block['Nonce'] = Nonce
	block['hash'] = hash[0]

#	key.append(Nonce)
#	print("the nonce is",key)
#	print("the hash is",hash)
	hash.clear()
	blockchain.append(block)
	data.save_data(blockchain)
#	print("the blockchain is",blockchain)

	return True
