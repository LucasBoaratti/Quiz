def quiz(): #Função para iniciar o quiz
    print("Seja bem-vindo(a) ao quiz do T3ddy! Aqui você terá que acertar todas as alternativas para vencer.\n") #Exibindo a mensagem de boas vindas na tela/terminal
    print("Quiz criado pelo b3ar: Lucas Henrique Boaratti Silva.\n") #Exibindo o nome do criador do quiz na tela/terminal

    perguntas = [ #Criando as perguntas, alternativas e colocando as respostas corretas em uma lista na variável perguntas
        { #Criando um dicionário com cada pergunta, alternativa e a resposta correta
            "Pergunta": "Qual é o nome do T3ddy?", 

            "Alternativas": {
                "A": "Lucas Henrique", 
                "B": "Lucas Olioti", #Resposta correta
                "C": "Lucas Souza", 
                "D": "Lucas Rangel",
            }, 

            "Resposta": "b",
        },
        {
            "Pergunta": "Em que ano T3ddy começou no youtube?",
            
            "Alternativas": {
                "A": 2014, 
                "B": 2012, #Resposta correta
                "C": 2013, 
                "D": 2011,
            }, 

            "Resposta": "b",
        },
        {
            "Pergunta": "Qual é o canal de games do T3ddy?",
            
            "Alternativas": {
                "A": "T3ddy games", #Resposta correta 
                "B": "T3ddy jogos", 
                "C": "T3ddy gamer", 
                "D": "T3ddy gameplays"
            }, 

            "Resposta": "a",
        
        },
        {
            "Pergunta": "Qual é o vídeo com mais vizualizações do canal do T3ddy? (Vídeos postados até 02/01/2025)",
            
            "Alternativas": {
                "A": "Testei o aplicativo que traduz os latidos do meu cachorro", 
                "B": "SE EU RIR = AUMENTA 1 MINUTO DE VÍDEO", 
                "C": "COMO É SER UMA MERDA? | Ploft", 
                "D": "AVISO: VOCÊ NÃO VAI DORMIR DEPOIS DESSA CONVERSA" #Resposta correta
            }, 

            "Resposta": "d",
        },
        {
            "Pergunta": "Qual é o vídeo mais visto no canal de games do T3ddy?",
            
            "Alternativas": {
                "A": "Testei o App Talking Angela pra ver se ele Espiona as Crianças mesmo", #Resposta correta
                "B": "Cansei de fazer vídeos, agora sou motorista de ônibus", 
                "C": "O Jogo virou.... Eu espionei a Ângela pra ver se encontro o Hacker", 
                "D": "Baixei o My Talking Angela 2 pra ver se ela ainda hackeia crianças"
            }, 

            "Resposta": "a",
        },
    ]

    pontuacao = 0 #Armazenando o valor inicial 0 para a pontuação

    for numeroPergunta, pergunta in enumerate(perguntas): #Laço de repetição para enumerar as perguntas
        print(f"Pergunta {numeroPergunta + 1}: {pergunta['Pergunta']}") #Exibindo a pergunta na tela/terminal

        for alternativa, respostaAlternativa in pergunta['Alternativas'].items(): #Laço de repetição para mostrar as alternativas e as respostas na tela/terminal
            print(f" {alternativa}) {respostaAlternativa}") #Exibindo as alternativas e as respostas na tela/terminal

        respostaUsuario = input("\nDigite a alternativa correta: ").lower() #O usuário vai digitar a resposta 

        if respostaUsuario == pergunta['Resposta']: #Verificando se o usuário acertou a pergunta, de acordo com a resposta certa
            print("\nResposta correta. Parabéns!\n") #Exibindo a mensagem de parabenizaçaõ para o usuário na tela/terminal
            pontuacao = pontuacao + 1 #Aumentando a pontuação conforme for acertando a pergunta
        else: #Caso o usuário não acerte a pergunta...
            print(f"\nDesculpe, mas a resposta está incorreta. Resposta certa: {pergunta['Alternativas'][pergunta['Resposta'].upper()]} \n") #Exibindo a mensagem de resposta errada na tela/terminal

    print(f"Resultado final: Você acertou {pontuacao} de {len(perguntas)} perguntas!") #Exibindo o resultado final, após terminar todas as perguntas, na tela/terminal

    if pontuacao == len(perguntas): #Verificando se o usuário acertou todas as perguntas
        print("\nVocê acertou todas as perguntas. Meus parabéns!\n") #Exibindo a mensagem de parabenização na tela/terminal
    elif pontuacao > len(perguntas) // 2: #Verificando se o usuário acertou metade das questões
        print("\nÓtimo, você foi muito bem!\n") #Exibindo a mensagem de parabenização na tela/terminal
    else: #Caso o usuário acerte menos da metade das perguntas...
        print("\nDesculpe, mas você não foi bem. Que tal tentar de novo?\n") #Exibindo a mensagem de parabenização na tela/terminal
 
while True: #Laço de repetição para rodar o código e o jogo para o usuário
    quiz() #Executando a função 

    continuarQuiz = input("Você quer continuar o quiz? Digite 's' para sim ou 'n' para não: ").lower() #O usuário vai verificar se quer continuar jogando

    if continuarQuiz == "n": #Caso a resposta do usuário for não
        print("\nObrigado por jogar o quiz do T3ddy! Até a próxima.") #Exibindo a mensagem de agradecimento na tela/terminal
        break #Parando o código por completo