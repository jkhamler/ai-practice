import openai

# Set your OpenAI API key
client = openai.OpenAI(
    api_key="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")

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
