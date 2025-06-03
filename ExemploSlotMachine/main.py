import random as rd
def spin_row():
    symbols = ['✉️','🍒','🧠','🪱','🛠️']

    return [rd.choice(symbols) for _ in range(3)]


def print_row(row):
    print('*************')
    print(" | ".join(row))
    print('*************')

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet *5
        elif row[0] == '✉️':
            return bet*2
        elif row[0] == '🧠':
            return bet*3
        elif row[0] == '🛠️':
            return bet*4
        elif row[0] =='🪱':
            print("GRANDE GANHO")
            return bet*1000
        
    return 0 

def main():
    balance = 100
    print("------------------------------------")
    print("| Bem-vindo ao jogo da minhoquinha |")
    print("|         ✉️  🍒 🧠 🪱  🛠️            |")
    print("------------------------------------")

    while balance > 0:
        print(f"CREDITO: {balance}")

        bet = input("QUANTO CREDITO PARA A MINHOCA ('q' se você se recusa): ")
        if bet == 'q':
            break

        if not bet.isdigit():
            print("A MINHOCA ESTA INSATISFEITA COM SUA FOLIA")
            continue
        bet = int(bet)

        if bet > balance:
            print("A MINHOCA SABE, NAO TENTE ENGANAR")
            continue

        if bet <=0:
            print("A MINHOCA ESTÁ INSTISFEITA. MAIS CREDITO")

        balance -= bet

        row = spin_row()
        print("A MINHOCA DIGERE...")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"VOCE FOI ABENÇOADO COM {payout} CREDITOS")
        else:
            print("A GRANDE MINHOCA NÃO TE ACHA DIGNO")

        balance +=payout
    print("****************************************")
    print(f"FIM. VOCÊ FOI ABENÇOADO COM {balance} CREDITOS")
    print("****************************************")
if __name__ == '__main__':
    main() 