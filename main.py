name = input("Digite o seu nome: ")
age = int(input("Qual sua idade? "))
height = float(input("Qual sua altura? "))
weight = float(input("Qual seu peso? "))
sex = input("Qual seu sexo (Feminino/Masculino)? ").strip().capitalize()  # .strip() tira os espaços em branco e extras da resposta .capitalize() padroniza o texto
shape = input("Qual forma de dieta você quer? (Moderado/Agressivo): ").strip().capitalize()
print("\nEscolha seu nível de atividade física:")  # \n faz uma quebra de texto
print("1 - Sedentário (Pouco ou nenhum exercício)")
print("2 - Pouco ativo (Exercício leve, 1-3 dias por semana)")
print("3 - Moderadamente ativo (Exercício moderado, 3-5 dias por semana)")
print("4 - Muito ativo (Exercício intenso, 6-7 dias por semana)")
print("5 - Extremamente ativo (Exercício muito intenso ou trabalho físico)")
physical_activity = int(input("Digite o número correspondente ao seu nível de atividade física: "))

activity_level = {
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.9
}

if sex == "Feminino":  # "Se" o sexo for feminino
    tmb = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
elif sex == "Masculino":  # "Senão, será" Senão for feminino, será masculino
    tmb = 66 + (13.7 * weight) + (5 * height) - (6.8 * age) 
else:  # "Senão" Senão for nenhum dos dois
    print("Sexo inválido. Por favor, insira 'Feminino' ou 'Masculino'.")
    exit()

if physical_activity in activity_level:
    tmb_activity = tmb * activity_level[physical_activity]
    if shape == "Moderado":
        tmb_activity -= 500
        print(f"\n{name} com o objetivo escolhido, a quantidade de calorias que deve comer por dia é: {tmb_activity:.2f}")
    elif shape == "Agressivo":
        tmb_activity -= 1000
        print(f"\n{name} com o objetivo escolhido, a quantidade de calorias que deve comer por dia é: {tmb_activity:.2f}")
    else:
        print("Forma inválida. Por favor, escolha 'Moderado' ou 'Agressivo'.")
else:
    print("Nível de atividade inválido. Por favor, escolha um número de 1 a 5.")