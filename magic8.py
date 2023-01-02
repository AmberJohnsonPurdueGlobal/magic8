#allows integers to be chosen at random
import random

#Generate username
name = ""
#Generate Question to ask
question = ""
#Generate series of possible answers
answer = ""
#Random question picker
random_number = random.randint(1, 9)
#uncomment to verify random answer picker is picking at random
#print(random_number)

#if user does not input name or question
#"Seeker, ask and I shall tell"
if name == "" and question == "":
  print("Seeker, ask and I shall tell")
  #If there is no name but a question 
  #"Seeker asks: question"
elif name == "":
  print("Seeker"+ " asks: " + question)
  #name is providedand question is not
  #"name, ask me a question!"
elif name == name and question == "":
  print(name + " ask me a question!")
  #both name and question provided
  #"Name asks: question"
else:
   print(name + " asks: " + question)

#After question is asked the magic8 redponds uless there is no question asked
if question != "":
  print("magic8 states: ")

#series of poosible answers within the 1-9 range to output only if a question is ASKED
if random_number == 1 and question != "":
  print("Yes - definitely.")
elif random_number == 2 and question != "":
  print("It is decidedly so.")
elif random_number == 3 and question != "":
  print("Without a doubt.")
elif random_number == 4 and question != "":
  print("Reply hazy, try again.")
elif random_number == 5 and question != "":
  print("Ask again later.")
elif random_number == 6 and question != "":
  print("Better not tell you now.")
elif random_number == 7 and question != "":
  print("My sources say no.")
elif random_number == 8 and question != "":
  print("Outlook not so good.")
elif random_number == 9 and question != "":
  print("Very doubtful.")
  #answer if outside range of 1-9 answers to ooutput
else:
   answer == "error"


