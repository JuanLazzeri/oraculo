import random
import time

input = input("Diga-me, qual a sua questão de hoje, mero mortal?\nQual a sua dúvida?\nO que te aflinge?\n>>")
frases = [
    "A resposta está dentro de você!",
    "E você se pergunta ainda?",
    "Será? O que seria certo? E o que seria errado? Quem define isso?",
    "Pergunte para a sua mãe!",
    "A resposta é 42!",
    "Se nem você sabe, como eu poderia saber?",
    "Talvez sim! Mas talvez não, também!",
    "Acho que depende!",
    "O vento sopra onde menos se espera!",
    "A vida é feita de escolhas!",
    ]

print("Aguarde um momento enquanto reflito sobre a sua questão...")

reticencias = [".","..", "..."]
for i in range(3):
    print(f"Pensando{reticencias[i % len(reticencias)]}", end="\r", flush=True)
    time.sleep(1)

print("Encontrei a resposta!")
time.sleep(1)

resposta_oraculo = random.choice(frases)
print(f"------------------------------------------------------------\nCom base nesta questão, respondo sabedoramente:\n {resposta_oraculo}\n------------------------------------------------------------")
print("Agora, se me der licença, preciso ir!")