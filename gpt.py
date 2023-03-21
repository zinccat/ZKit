import openai
import prompts

def gpt(inputs, prompt="prompts.default", model="gpt-3.5-turbo", temperature=0.3):
    output = openai.ChatCompletion.create(
    model=model,
    messages=[
            {"role": "system", "content": eval(prompt)},
            {"role": "user", "content": inputs},
        ],
        temperature=temperature
    )
    return output.choices[0]['message']['content']