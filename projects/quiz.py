#* PROJETO QUIZ EM PYTHON 

#* Perguntas
lista_perguntas = [
    {
        'enunciado' : 'Socrates nunca escreveu nada. Tudo o que se sabe sobre ele provem de seus discipulos, como Platao e Xenofonte. Socrates costumava dialogar nas pracas de Atenas, fazendo perguntas que levavam seus interlocutores a repensar suas certezas. O metodo socratico consistia principalmente em:', 
        'alternativas' : {
            'A' : 'oferecer respostas definitivas as grandes questoes filosoficas.', 
            'B' : 'utilizar a retorica para convencer os cidadaos de sua propria ignorancia.',
            'C' : 'aplicar o conhecimento cientifico como forma de evidenciar verdades absolutas.',
            'D' : 'realizar dialogos criticos para questionar conceitos e estimular o autoconhecimento.',
            'E' : 'transmitir conhecimentos prontos a seus discipulos por meio de discursos publicos.',
        },
        'resposta' : 'D'
    },
    {
        'enunciado' : 'Durante a democracia ateniense, Socrates foi acusado de corromper a juventude e nao reconhecer os deuses da cidade, sendo condenado a morte. Sua postura diante do julgamento e relatada na obra Apologia de Socrates, de Platao. A condenacao de Socrates revela um conflito entre:', 
        'alternativas' : {
            'A' : 'a filosofia critica e a manutencao da ordem tradicional.',
            'B' : 'o direito dos cidadaos e a tirania aristocratica.',
            'C' : 'a religiao politeista e a ciencia empirica.',
            'D' : 'os valores democraticos e a escravidao institucionalizada.',
            'E' : 'a racionalidade filosofica e a supersticao popular.',
        },
        'resposta' : 'A'
    },
]

#* Iteracao Sobre a Lista Para Exibir as Perguntas
pontuacao = 0
for indice, questao in enumerate(lista_perguntas, start=1):
    print(f'{indice}. {questao["enunciado"]}') # exibicao de cada pergunta
    
    for letra, texto in questao['alternativas'].items(): # exibicao das alternativas e dos textos das alternativas 
        print(f'{letra}) {texto}')
    
    # solicitar resposta do usuario
    resposta_usuario = input('Digite sua resposta: ').upper()
    
    if resposta_usuario == questao['resposta']:
        print('Resposta correta!')
        pontuacao += 1
    else:
        print('Resposta incorreta!')

print(f'Parabéns por concluir o quiz. Sua pontuação foi: {pontuacao}')