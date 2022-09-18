import hashlib

def create_secret_hash(Nonce,block):
	temp = (str(block)+str(Nonce)).encode()
	hash_temp = hashlib.sha256(temp).hexdigest()
	#print("verify_user value ",hash_temp)
	return hash_temp