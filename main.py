import os
import requests
from requests.exceptions import ConnectionError


logo = """
██████████████████████████████████████    
█▄─▀█▄─▄█▀▀▀▀▀██▄─▄███▄─▄█─▄─▄─█▄─▄▄─█ 
██─█▄▀─██████████─██▀██─████─████─▄█▀█   
▀▄▄▄▀▀▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀
       █ ▄▀█  █▀▄ █        By Manisso               
      ▐▌          ▐▌
      █▌▀▄  ▄▄  ▄▀▐█ 
     ▐██  ▀▀  ▀▀  ██▌
    ▄████▄  ▐▌  ▄████▄
"""


def main():
  os.system('clear')
  print(logo)
  print('\n')
  try:
        response = requests.get("http://ipinfo.io/ip")
        content = response.content.decode("utf-8")
  except ConnectionError:
        content = "127.0.0.1     "

  try:
        push = requests.get("https://raw.githubusercontent.com/Manisso/Nlite/main/push.txt")
        ntf = push.content.decode("utf-8")
  except ConnectionError:
        ntf = "v 0.1 - No Internet"

  print(ntf)
  print("+---------------------------+")
  print("| Your IP : ",content,"|")
  print("+---------------------------+")
  print('\n')
  menu()


def menu():
  print("Select an option:\n")
  print("+----------------+")
  print("| [1]- PortScan  |")
  print("+----------------+")
  print("| [2]- RangeScan |")
  print("+----------------+")
  print("| [3]- Install   |")
  print("+----------------+")
  print("| [4]- Update    |")
  print("+----------------+")
  print("| [0]- Exit      |")
  print("+----------------+")
  print("\n")
  choice = input(">>> ")

  if choice == "1":
    tool1()
  elif choice == "2":
    tool2()
  elif choice == "3":
    install()
  elif choice == "4":
    update()
  elif choice == "0":
    os.system('clear')
    exit()
  else:
    print("\nInvalid choice. Please try again.\n")
    menu()


def tool1():
  print("Running PortScan ...")
  os.system('python ip.py')


def tool2():
  print("Running RangeScan ...")
  os.system('python rang.py')


def install():
  print("Running Installer ...")
  os.system('bash install.sh')


def update():
  print("Updating ...")
  os.system('bash update.sh')


if __name__ == "__main__":
  main()
