import random

#Generate username
name = "Amber"
#Generate Question to ask
question = "Will today be a good day?"
#Generate series of possible answers
answer = ""
#Random question picker
random_number = random.randint(1, 9)
#uncomment to verify random answer picker is picking at random
#print(random_number)

#Ask a question
print(name + " asks: " + question)

#series of poosible answers within the 1-9 range to output
if random_number == 1:
  print("Yes - definitely.")
elif random_number == 2:
  print("It is decidedly so.")
elif random_number == 3:
  print("Without a doubt.")
elif random_number == 4:
  print("Reply hazy, try again.")
elif random_number == 5:
  print("sk again later.")
elif random_number == 6:
  print("Better not tell you now.")
elif random_number == 7:
  print("My sources say no.")
elif random_number == 8:
  print("Outlook not so good.")
elif random_number == 9:
  print("Very doubtful.")
  #answer if outside range of 1-9 answers to ooutput
else:
   answer == "error"


