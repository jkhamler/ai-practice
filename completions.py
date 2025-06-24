from openai import OpenAI

client = OpenAI(
  api_key=""
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "Is Python a good programming language?"}
  ]
)

print(completion.choices[0].message.content)