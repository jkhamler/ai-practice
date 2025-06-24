import openai

# Set your OpenAI API key
client = openai.OpenAI(
    api_key="")

def chat_with_gpt(prompt, model="gpt-4", temperature=0.7):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print("Simple GPT Agent (OpenAI v1.0+). Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        reply = chat_with_gpt(user_input)
        print(f"GPT: {reply}")
