# Simulação do agente especialista Genera

def responder(pergunta):
    return (
        "Resposta simulada baseada nos dados recuperados do relatório genético. "
        "As informações possuem caráter informativo e não substituem avaliação médica."
    )

if __name__ == "__main__":
    pergunta = input("Digite sua pergunta: ")
    print(responder(pergunta))
