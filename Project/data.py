
import json
import os
def save_data(blockchain):
	with open('db.txt',mode = 'w') as f:
		f.write(json.dumps(blockchain))

def retrieve_data():
	file_path = 'db.txt'
	if os.stat(file_path).st_size == 0:
		return []
	else:
		with open('db.txt',mode='r') as f:
			blockchain = f.readline()
			#print("the data after retriving is  ",blockchain)
			blockchain = json.loads(blockchain)
			return blockchain

	