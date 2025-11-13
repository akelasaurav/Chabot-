def chatbot():
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("chatbot: Hi!")
        elif user_input == "how are you?":
            print("chatbot: I'm doing well,thank you!")
        elif user_input == "bye":
            print("chatbot: Goodbye!")
            break
        else:
            print("chatbot: I'm sorry, I don't undetrstand that.")



chatbot()            
