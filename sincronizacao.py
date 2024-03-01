import threading
import time

recurso_disponivel = False
cv = threading.Condition()

def produtor():
    global recurso_disponivel
    while True:
        with cv:
            recurso_disponivel = True
            print("Produtor: Recurso produzido!")
            cv.notify_all()  # Notifica os consumidores
        
        # Espera um tempo antes de produzir novamente
        time.sleep(1)

def consumidor(id):
    global recurso_disponivel
    while True:
        with cv:
            while not recurso_disponivel:
                cv.wait()  # Espera pelo recurso
            # Consome o recurso
            print("Consumidor", id, ": Recurso consumido!")
            recurso_disponivel = False
        
        # Realiza o processamento do recurso
        
        # Espera um tempo antes de consumir novamente
        time.sleep(0.5)

def main():
    try:
        num_consumidores = int(input('Olá, digite a quantidade de consumidores que deseja: '))

        prod = threading.Thread(target=produtor) # Thread do produtor
        consumidores = [
            threading.Thread(target=consumidor, args=(i,)) # Thread do consumidor
            for i in range(1, num_consumidores + 1)
        ]

        prod.start()

        for consumir in consumidores:
            consumir.start()
        
        prod.join()

        for consumir in consumidores:
            consumir.join()

        print("Todos os consumidores foram executados. Processo Finalizado")

    except ValueError:
        print('Isso não é um número inteiro. Tente novamente.')
        main()

    

    # t1 = threading.Thread(target=produtor)  # Thread do produtor
    # t2 = threading.Thread(target=consumidor, args=(1,))  # Thread do consumidor 1
    # t3 = threading.Thread(target=consumidor, args=(2,))  # Thread do consumidor 2

    # t1.start()
    # t2.start()
    # t3.start()

    # t1.join()
    # t2.join()
    # t3.join()

if __name__ == "__main__":
    main()
