user_name: str = input("Whats your name: ")
user_age: int = int(input("Whats your age: "))
user_hobby: str = input("What are your hobbys: ")

print(f"Hi {user_name}, I'm {user_age} years old")
print("Hi {}, I'm {} years old".format(user_name, user_age))
