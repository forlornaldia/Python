import random
question = input("What is your question? ")
answer = ""
random_number = random.randint(1, 20)
if random_number == 1:
  answer = "Yes - Definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
    answer = "It is certain."
elif random_number == 11:
    answer = "My reply is no."
elif random_number == 12:
    answer = "Don't count on it."
elif random_number == 13:
  answer = "Concentrate and ask again."
elif random_number == 14:
    answer = "Outlook good."
elif random_number == 15:
    answer = "Yes."
elif random_number == 16:
  answer = "Signs point to yes."
elif random_number == 17:
  answer = "Cannot predict now."
elif random_number == 18:
  answer = "You may rely on it."
elif random_number == 19:
  answer = "Most likely."
elif random_number == 20:
  answer = "As I see it, yes."
else:
  answer = "Error 01"
print(f"Question: {question}")
print(f"Magic 8-Ball's answer: {answer}")