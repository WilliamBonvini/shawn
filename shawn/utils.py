import openai


def get_response(content: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": content}
        ]
    )
    response = completion.choices[0].message.content
    return response
