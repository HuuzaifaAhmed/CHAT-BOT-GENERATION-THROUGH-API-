from groq import Groq

client= Groq(api_key="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")
chat_completion = client.chat.completions.create (
    model="llama3-8b-8192",
    messages=[
        {
            "role": "system", 
             "content": "you are a helpful assistant"
        },

        {
             "role":"user",
             "content": "I want to know the meaning of life",
        }
    ],
    temperature=0.5,
    max_tokens=100,
    top_p=1,
    n=1,
    stop=None
)

print (chat_completion.choices[0].message.content)
