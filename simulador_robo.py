import time
import random

posicao = 0
obstaculo = random.randint(5, 15)

def mostrar_ambiente():
    ambiente = ""
    for i in range(20):
        if i == posicao:
            ambiente += "🤖"
        elif i == obstaculo:
            ambiente += "🚧"
        else:
            ambiente += "▫️"
    print(ambiente)

def mover_robo():
    global posicao
    while True:
        mostrar_ambiente()
        comando = input("Digite o comando (frente / direita / esquerda / parar): ").lower()

        if comando == "parar":
            print("Robô desligado!")
            break
        elif comando == "frente":
            if posicao + 1 == obstaculo:
                print("⚠️ Obstáculo à frente! Escolha outra direção.")
            else:
                posicao += 1
        elif comando == "esquerda":
            print("↪️ Virando à esquerda (simulação)")
        elif comando == "direita":
            print("↩️ Virando à direita (simulação)")
        else:
            print("❌ Comando inválido.")
        
        time.sleep(0.5)
        print()

mover_robo()
