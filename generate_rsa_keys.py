import rsa
pubkey, privkey = rsa.newkeys(512)


# Generate new public and private key

with open('private.pem','wb') as f:
    f.write(privkey.save_pkcs1())

with open('public.pem','wb') as f:
    f.write(pubkey.save_pkcs1())
