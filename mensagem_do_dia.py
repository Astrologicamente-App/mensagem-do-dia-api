import os
import random
from openai import OpenAI
import json

bichos = [
    "Abelha", "Anta",
    "Baleia", "Borboleta",
    "Cachorro", "Cavalo",
    "Dromedário", "Doninha",
    "Elefante", "Esquilo",
    "Foca", "Formiga",
    "Gato", "Girafa",
    "Hipopótamo", "Hiena",
    "Iguana", "Íbis",
    "Jacaré", "Javali",
    "Kanguru", "Koala",
    "Leão", "Leopardo",
    "Macaco", "Morcego",
    "Naja", "Narval",
    "Orangotango", "Onça",
    "Panda", "Pato",
    "Quati", "Quero-quero",
    "Raposa", "Rato",
    "Sapo", "Sagui",
    "Tatu", "Tigre",
    "Urso", "Urutu",
    "Veado", "Vaca",
    "Xexéu", "Xenops",
    "Zebra", "Zebu"
]



def calcular_signo(data_nascimento):
    dia, mes, ano = map(int, data_nascimento.split('/'))

    if (mes == 3 and dia >= 20) or (mes == 4 and dia <= 20):
        return "Áries"
    elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
        return "Touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gêmeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 21):
        return "Câncer"
    elif (mes == 7 and dia >= 22) or (mes == 8 and dia <= 22):
        return "Leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 21):
        return "Capricórnio"
    elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 18):
        return "Aquário"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 19):
        return "Peixes"
    else:
        return "Signo não suportado."


def escolhe_bicho(data_nascimento):
    dia, mes, ano = map(int, data_nascimento.split('/'))

    if dia > 27:
        return random.choice(bichos)
    
    # Caso contrário, escolhe com base na primeira letra
    letra = chr(ord('A') + dia - 1)
    bichos_filtrados = [bicho for bicho in bichos if bicho.startswith(letra)]
    
    # Se não houver bichos com a letra correspondente, escolhe aleatoriamente
    if not bichos_filtrados:
        return random.choice(bichos)
    
    return random.choice(bichos_filtrados)


def request_mensagem_do_dia(data_nascimento):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))  # Substitua pela sua chave de API no environment da OpenAI

    model_engine = "gpt-3.5-turbo-0125"

    # Calcular o signo com base na data de nascimento
    signo = calcular_signo(data_nascimento)

    # Montar o prompt em formato JSON
    prompt = json.dumps({
        "data-de-nascimento": data_nascimento,
        "signo": signo,
        "mensagem": "Informe em JSON a Mensagem do Dia específica para o signo baseado na data de aniversário."
    })

    response = client.chat.completions.create(
        model=model_engine,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
        ],
    )

    message_content = response.choices[0].message.content

    return message_content

