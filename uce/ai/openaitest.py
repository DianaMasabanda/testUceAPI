import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ''


def inference(prompt: str) -> list:
    openai.organization = 'org-XXkIUZcRiRwPOVV0oLd6DjDC'
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40, '-'))

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un profesor de programación para niños, genera una explicación para el temas que se prporciona
            E.G: Programación
            -Es como armar un rompecabezas donde cada pieza forma el sistema completo"""},
            {"role": "user", "content": prompt}
        ]
    )

    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print('[SE TERMINÓ DE PROCESS]'.center(40, '-'))

    return [content, total_tokens]
