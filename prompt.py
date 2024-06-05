from openai import OpenAI

def gerar_palavra(idioma, dificuldade):
    idioma = idioma
    dificuldade = dificuldade

    client= OpenAI(api_key = "")
    prompt= [{"role":"user", "content":"gere uma palavra de nivel {}, toda em minusculo, sem acentos, em {}".format(dificuldade, idioma)}]


    response = client.chat.completions.create(
        
            model = "gpt-3.5-turbo-0125",
            messages = prompt,
            max_tokens = 50,
            temperature = 1
        )

    palavra = response.choices[0].message.content
    
    return palavra