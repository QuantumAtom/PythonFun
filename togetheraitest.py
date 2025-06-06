from together  import Together
client = Together()

def main():
    print("Let's talk!")
    print("Type in exit or quit to quit")
    while True:
        user_sez = input("\nWhat's up: ")
    # exit
        if user_sez.lower() in ["exit", "quit"]:
            print("Thanks for chatting!")
            break
        togetheragent(user_sez)
    

def togetheragent(request): 
    response=client.chat.completions.create(
        model="Qwen/Qwen3-235B-A22B-fp8-tput",
        messages=[
            {
                "role":"user", 
                "content":request
            }
        ]
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()  