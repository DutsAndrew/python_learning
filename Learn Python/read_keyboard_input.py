name = input("What is your name? ")
print('Hello ' + name)

job = input("What is your job? ")
print('Your job is ' + job)

num = input("Give me a number? ")
print('You said: ' + str(num))

def give_questionnaire():
  phone_number = input("What is your phone number")
  print('Your phone number is ' + phone_number)

  preferred_language = input("What is your favorite programming language? ")
  print('You answered ' + preferred_language)

give_questionnaire()
