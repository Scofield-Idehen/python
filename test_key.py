
import hashlib, urllib.request 

def read_wordlist(url):
  """
  Read wordlist from URL
  Return list of password strings
  """

def hash_password(password):
  """
  Hash password string using SHA1 
  Return hash string
  """

def crack_password(wordlist, hash):
  """
  Bruteforce try wordlist passwords
  Return password string if found
  """

if __name__ == "__main__":

  url = "https://weakpasswords.txt"
  hash = hash_password("secretpass")
  
  wordlist = read_wordlist(url)

  cracked_pass = crack_password(wordlist, hash)

  if cracked_pass:
    print("Password cracked", cracked_pass)
  else:
    print("Password secure")