import openai

# Define OpenAI API key 
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "C# array example"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=4096,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)