import openai

sys = ""

u1 = "Can we talk about Reverse Prompt Engineering? By Reverse Prompt Engineering I mean creating a prompt from a given text."

a1 = """Yes, of course! Reverse Prompt Engineering is an interesting and useful technique that involves generating a prompt that can be used to generate text similar to a given input text. This technique is becoming increasingly popular in natural language processing and machine learning.

The idea behind Reverse Prompt Engineering is to create a prompt that provides sufficient information to the language model to generate text that is consistent with the input text. The prompt should be designed in such a way that it includes relevant information about the context, style, and structure of the input text.

Reverse Prompt Engineering can be used in a variety of applications, such as generating summaries, paraphrasing text, or generating responses to a given prompt. It can also be used to improve the performance of language models by providing them with more specific and relevant information about the task at hand."""

u2 = "Great. Can you give me a simple example of Reverse Prompt Engineering?"

a2 = """Sure, here's a simple example of Reverse Prompt Engineering:

Let's say we have the following input text: "The quick brown fox jumps over the lazy dog."

To generate a prompt that can be used to generate text similar to this input text, we can try the following:

Prompt: "Write a sentence about a quick animal jumping over a lazy animal."

This prompt captures the key elements of the input text: a quick animal (the fox) jumping over a lazy animal (the dog). It also provides some guidance on the style and structure of the text (i.e., a sentence).

Using this prompt, a language model can generate text that is similar in style and structure to the input text. For example, it might generate the following:

Output: "A swift gazelle leaped over a sleeping lion."

In this output, we see a similar structure and style to the input text, with a quick animal (the gazelle) jumping over a lazy animal (the sleeping lion).

Of course, the quality and relevance of the output will depend on the specific language model and the prompt used, but this example should give you a basic idea of how Reverse Prompt Engineering works."""

u3 = "Good. Write a short explanation on how dog training works, and Reverse Prompt Engineer the explanation."

a3 = """Sure, here's a short explanation of how dog training works:

Dog training is the process of teaching a dog to behave in a certain way in response to specific commands or stimuli. It typically involves using positive reinforcement or negative reinforcement techniques to encourage desirable behaviors and discourage undesirable ones. Positive reinforcement involves rewarding a dog for exhibiting the desired behavior, while negative reinforcement involves removing a negative stimulus when the desired behavior is exhibited. Consistency, patience, and repetition are key elements of successful dog training.

Now, let's Reverse Prompt Engineer this explanation to generate a prompt that can be used to generate text similar to this explanation:

Prompt: "Explain the process of teaching a dog to behave in a certain way and the techniques involved in it."

This prompt captures the key elements of the explanation: the process of teaching a dog to behave in a certain way, the use of positive and negative reinforcement techniques, and the importance of consistency, patience, and repetition. It also provides some guidance on the style and structure of the text (i.e., an explanation).

Using this prompt, a language model can generate text that is similar in style and structure to the explanation. For example, it might generate the following:

Output: "Teaching a dog to behave in a certain way involves using positive and negative reinforcement techniques. Positive reinforcement involves rewarding the dog for exhibiting desirable behaviors, while negative reinforcement involves removing a negative stimulus when the desired behavior is exhibited. Consistency, patience, and repetition are important elements of successful dog training."

In this output, we see a similar structure and style to the original explanation, with a clear explanation of the process and techniques involved in dog training."""

u4 = "Great. Can you create a very technical reverse prompt engineering template?"

a4 = """Sure, here's a technical Reverse Prompt Engineering template:

Prompt: "Using [insert technical term], explain [insert concept or task] and the underlying principles that govern it."

This prompt template is designed to generate prompts for technical concepts or tasks, and is intended for use by domain experts or technical writers who are familiar with the subject matter. The technical term can be any relevant term or concept that is associated with the task or concept being explained.

For example, if we want to explain the concept of machine learning, we could use this template as follows:

Prompt: "Using supervised learning, explain the concept of machine learning and the underlying principles that govern it."

In this prompt, we've used the technical term "supervised learning" to narrow the focus of the explanation, and we've asked for an explanation of the broader concept of machine learning and the underlying principles that govern it.

Using this prompt, a language model can generate technical explanations of machine learning that are consistent with the principles of supervised learning. The output could include an explanation of the types of data used in supervised learning, the different algorithms used for machine learning, and the principles of statistical inference that underlie machine learning.

Of course, the specific technical term and concept will depend on the subject matter being explained, but this template can be adapted to a wide range of technical domains and applications."""

u5 = """Can you reverse engineer the following {product description), capture the writing style and the length of the text:
product description = Personalized Spatial Audio with dynamic head tracking places sound all around you.Note : If the size of the earbud tips does not match the size of your ear canals or the headset is not worn properly in your ears, you may not obtain the correct sound qualities or call performance. Change the earbud tips to ones that fit more snugly in your ear
Single fit
Force sensor lets you control your entertainment and answer or end calls
Sweat and water resistant for AirPods and charging case
Lightning Charging Case or MagSafe Charging Case
Up to 6 hours of listening time
Up to 30 hours total listening time"""

a5 = "Write a product description for a set of earbuds that offer personalized spatial audio with dynamic head tracking, including information on the size of the earbud tips, the force sensor, sweat and water resistance, and the charging case. The description should be concise and informative, with a focus on the technical features and specifications of the product."

u6 = "Rewrite the reverse prompt into a prompt that can be used for any product description with a user input feature in the prompt that uses {}."

model="gpt-3.5-turbo"
temperature=0.3

output = openai.ChatCompletion.create(
    model=model,
    messages=[
            # {"role": "system", "content": eval(prompt)},
            {"role": "user", "content": u1},
            {"role": "assistant", "content": a1},
            {"role": "user", "content": u2},
            {"role": "assistant", "content": a2},
            {"role": "user", "content": u3},
            {"role": "assistant", "content": a3},
            {"role": "user", "content": u4},
            {"role": "assistant", "content": a4},
            {"role": "user", "content": u5},
            {"role": "assistant", "content": a5},
            {"role": "user", "content": u6},
        ],
        temperature=temperature
    )
print(output.choices[0]['message']['content'])