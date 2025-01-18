prompt = "\nTell me the toppings you want on your pizza: "
prompt += "\nEnter 'quit' to end your order. "

toppings = []
message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)
        toppings.append(message)

print(toppings)
