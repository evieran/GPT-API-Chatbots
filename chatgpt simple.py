import openai

openai.api_key = "####"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 benefits of building a chatbot with openai apis "}])
print(completion.choices[0].message.content)