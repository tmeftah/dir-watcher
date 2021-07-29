import sys
import rsa



# the same as in app.py
hash_key = b'c1210f11653341ab971f49e948ed3902'


# Read public and pivate key 

with open('private.pem','rb') as f:
    keydata = f.read()

privkey = rsa.PrivateKey.load_pkcs1(keydata)

with open('public.pem','rb') as f:
    keydata = f.read()


try:
    pubkey = rsa.PublicKey.load_pkcs1(keydata)
except :
    print('not valid key')
    sys.exit(1) 
    

# uuid will be send from client
client_uuid = '4C4C4544-0057-4E10-8056-C7C04F535432'

signature = rsa.sign(client_uuid.encode('utf-8')+ hash_key, privkey, 'SHA-1')
with open('license.key','wb') as f:
    f.write(signature)

print('license file generated...')


try:
    rsa.verify(data.encode('utf-8') + hash_key, signature, pubkey)
except rsa.VerificationError:
    # invalid license key - refuse to start
    print('invalid')
else:
    # start application
    print('valid key ')
