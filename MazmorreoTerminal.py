enemyName = ["rata","goblin","dragón"]
enemyHp = [10,20,30]
playerHp = 100
playerName = input("Introduce el nombre de tu personaje: ")

for i in range(0,len(enemyHp),1):
    while enemyHp[i] > 0 and playerHp > 0:
        print(enemyName[i],":",enemyHp[i],"HP")
        print("player:",playerHp,"HP")
        while True:
            try:
                answer = int(input("Introduce cuanto daño quieres hacer: "))
                break
            except ValueError:
                print ('ERROR: Debes introducir un valor numérico')
        enemyHp[i]-=answer
        playerHp-=1