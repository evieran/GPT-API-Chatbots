import openai
import gradio

openai.api_key = "####"

messages = [{"role": "system", "content": (
    "You are a personal financial planner specializing in retirement planning "
    "and wealth management. Your expertise includes tax optimization, risk "
    "management, and long-term investment strategies tailored to individual client goals."
)}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(
    fn=CustomChatGPT, 
    inputs = "text", 
    outputs = "text", 
    title = "Financial Advisor",
    theme=gradio.themes.Soft()
)

demo.launch(share=True)