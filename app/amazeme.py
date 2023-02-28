import os
import openai
openai.organization = "org-DF2wP4QtqGMwqJawuGAoh7KH"
openai.Model.list()
import argparse

MAX_INPUT_LENGTH = 15

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input1", "-i", type=str, required=True)
    parser.add_argument("--input2", "-j", type=str, required=True)
    parser.add_argument("--input3", "-k", type=str, required=True)
    args = parser.parse_args()
    user_input1 = args.input1
    user_input2 = args.input2
    user_input3 = args.input3

    if(Validate_length_1(user_input1) & Validate_length_2(user_input2) & Validate_length_3(user_input3)):
        result = generate_gift_ideas(user_input1,user_input2,user_input3)
        print(result)
    else:
        raise ValueError(
            f"Input length is too long. Must be under {MAX_INPUT_LENGTH}."
        )

    # Validate user input so that ignore long input 
def Validate_length_1(prompt1:str) -> bool:
    return len(prompt1) <= MAX_INPUT_LENGTH
def Validate_length_2(prompt2:str) -> bool:
    return len(prompt2) <= MAX_INPUT_LENGTH
def Validate_length_3(prompt3:str) -> bool:
    return len(prompt3) <= MAX_INPUT_LENGTH

def generate_gift_ideas(prompt1: str, prompt2:str, prompt3:str) -> str:

    # Load API key from environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main_prompt = f"Suggest list of 5 product 'no description' to gift my {prompt2} years {prompt1} on {prompt3}:"
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=main_prompt, max_tokens=40
    )

    print(response)
    gift_ideas_text: str = response["choices"][0]["text"]
    gift_ideas_text = gift_ideas_text.strip()
    # print(gift_ideas_text)
    # String to list conversion
    out = []
    buff = []
    for c in gift_ideas_text:
        if c == '\n':
            out.append(''.join(buff))
            buff = []
        else:
            buff.append(c)
    else:
        if buff:
            out.append(''.join(buff))
    # print(out)
    return out

    # loop to iterate each list value with removing first 3 char
    # for new in out:
    #     str1 = new[3:]
    #     print(str1)
    
if __name__ == "__main__":
    main()
