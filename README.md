
# Blockchain based user authentication protocol

We use numerous tools/apps/webApps where we have to login before using.
Through this project I have tried to create a blockchain based authentication protocol which could help in securing the authentication process.


## Tech/tools/Language


**Language** - Python(3.7.5)

**Technology** - Blockchain.

**Web Framework** - Flask

**Other** - HTML, Css.
## Methodolgy

There are two important aspect of this project :-

1. **User registration process**:-

-> the user will provide his name and unique device-id.

-> then we will calculate a hash for the block using four things ie,
(name,device-id,Nonce,previous block hash)

-> after storing the hash in the new block made we will update the blockchain.

->we will provide the secret hash to user for future logins

2. **User login process**:-

->the user will provide his name, unique device-id, secret hash.

->we will retrieve the whole blockchain, then iterate through the blockchain and for
every block we will compare it’s device-id with the device-id provided by the user.

-> if the device-id matches then we create the hash of the combo containing the
block and Nonce.

-> if the hash now generated matches with the hash provided by the user then the
login is successful otherwise not.

## License

[MIT](https://choosealicense.com/licenses/mit/)

