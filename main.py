# dictionary that stores predefined questions as keys
# and their respective answers as values
outputs = {
    "hi": "Hi! Hope you are doing well.",
    "hello": "Hello! Hope you are doing well.",
    "how are you": "I am fine.\nWhat about you?",
    "who are you":"I am Rule Based Chatbot.",
    "how are you created":"I was built using Python",
    "thanks": "My Pleasure.\nIf you have another query Please ask."
}
while True:
    user_input = input("")
    clean = user_input.lower().strip()
    # the entered input is converted to lowercase by lower() function
    # and with strip() removed spaces
    if clean == "quit" or clean == "bye":
        print("GoodBye!")
        break
    elif clean == "":
        print("Please type")
    else:
        output = outputs.get(clean,"This is not mentioned in dictionary")
        print(output)