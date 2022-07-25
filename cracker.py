import hashlib
import string
import itertools

# get salt
with open("salt.txt", "r") as f:
  salt = f.read().strip()

# get hashes
hashes = []
with open("hashes.txt", "r") as f:
  for line in f:
    hash = line.strip()
    hashes.append(hash)

# start cracking
cracked_passwords = []

# dictionary attack with rockyou.txt
with open("rockyou.txt", "r", encoding='utf-8', errors='ignore') as f:
  for line in f:
    # strip new line character
    rockyou = line.strip()
    # concat salt and dictionary password, encode to utf-8
    salted_rockyou=(salt + rockyou).encode('utf-8')
    # hash salted dictionary password
    hash_password = hashlib.sha256(salted_rockyou).hexdigest()
    # check if dictionary password matches passwords
    for h in hashes:
      if h == hash_password:
        # if there is a match, add to cracked list
        cracked_passwords.append(hash_password+":"+rockyou)
        # remove cracked hash
        hashes.remove(h)
        break

# brute force remaining hashes
characters = string.ascii_letters + string.digits + string.punctuation
# find passwords with lengths up to 9 characters
for len in range(1, 5):
  # add and change characters in guess
  for guess in itertools.product(characters, repeat=len):
    guess = ''.join(guess)
    # concat salt and guess, encode to utf-8
    salted_guess=(salt + guess).encode('utf-8')
    # hash salted dictionary password
    hash_password = hashlib.sha256(salted_guess).hexdigest()
    # check if guesses matches passwords
    for h in hashes:
      if h == hash_password:
        # if there is a match, add to cracked list
        cracked_passwords.append(hash_password+":"+guess)
        # remove cracked hash
        hashes.remove(h)
        break

# print cracked passwords to cracked.txt
f=open("cracked.txt","w+")
for c in cracked_passwords:
  f.write(c+"\n")
# print noncracked hashes
for h in hashes:
  f.write(h+":\n")
f.close()
