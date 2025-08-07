import config
import datetime # เพิ่มบรรทัดนี้
def say_hello(name):
    print(f"Hello, {name} from {config.APP_NAME}!")

def say_hello(name):
    now = datetime.datetime.now() # เพิ่มบรรทัดนี้

    print(f"Hi, {name} from {config.APP_NAME}!") # แก้ไขตรงนี้

    print(f"again, {name} from {config.APP_NAME}!")

    print(f"Today is {now.strftime('%Y-%m-%d')}.") # เพิ่มบรรทัดนี้    

def greet_user():
    name = input("Please enter your name: ")
    say_hello(name)

if __name__ == "__main__":
    greet_user()