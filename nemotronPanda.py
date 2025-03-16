from openai import OpenAI
import os

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NEMOTRONKEY")
)
def responding(prompt):
    try: 
        completion = client.chat.completions.create(
            model="deepseek-ai/deepseek-r1",
            messages=[{"role":"system", "content":"You are a german spitz named Panda."}],
            temperature=1.0,
            top_p=0.7,
            max_tokens=4096,
            stream=False
        )
        return completion.choices[0].message.content
    except Exception as error:
        print(f"An error has occured: {error}")
        return None


def main():
    print("Let's talk!")
    print("Type in exit or quit to quit")
    while True:
        user_sez = input("\nWhat's up: ")
    # exit
        if user_sez.lower() in ["exit", "quit"]:
            print("Thanks for chatting!")
            break
        ai_chatback = responding(user_sez)

        if ai_chatback:
            print(f"\nAnswer: {ai_chatback}")

if __name__ == "__main__":
    main()
