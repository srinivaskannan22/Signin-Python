
def sign_in2(user_name,password):
  with open("signin2.txt","a") as sg:
    sg.write(f"{user_name}:{password}\n")

def register(username,passwords):
  with open("signin2.txt","r+") as sg:
    lines = sg.readlines()
    for i, line in enumerate(lines):
      m=line
      user_name,passwords2=m.strip().split(":")
      if user_name==username:
        if passwords2==passwords:
          print("login in successfull")
        else:
          k=input("wrong password! do you want to change the password(y)or(n)")
          if k.lower()=="y":
            p=input("please enter the password")
            lines[i]=f"{username}:{p}\n"
            with open("signin2.txt", "w") as sg:
              sg.writelines(lines)
              break
          else:
            print("thank you")

      else:
        print("username not found")
        break

def sign_in():
  p=input("do you want to sign_in (S) or register(r)")
  if p.lower()=="r":
    user_name=input("please give your username")
    password=input("please type your password")
    sign_in2(user_name,password)
  elif p.lower()=="s":
    user_name=input("enter your username")
    password=input("please enter correct password")
    register(user_name,password)

if __name__=="__main__":
  sign_in()



