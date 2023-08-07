import openai
openai.api_key = //your chatgpt api key


specpoint = ""
completion = openai.ChatCompletion.create(
   model = "gpt-3.5-turbo",
   messages = [{"role":"user", "content": "can you convert '" + specpoint + "' into a list of questions in an array"}]
)

print(completion.choices[0].message.content)
