import openai


while True:
    prompt = str(input("tell me what you want \n"))
    completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            temperature=0.5,
        )
    message = completions.choices[0]['text']
    print(message)


 
