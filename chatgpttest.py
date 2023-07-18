import openai
openai.api_key = "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"


specpoint = ""
completion = openai.ChatCompletion.create(
   model = "gpt-3.5-turbo",
   messages = [{"role":"user", "content": "can you convert '" + specpoint + "' into a list of questions in an array"}]
)

print(completion.choices[0].message.content)