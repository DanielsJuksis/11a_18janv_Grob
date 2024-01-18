def rinda(ceļš):
    try:
        with open(ceļš, 'r', encoding='utf-8') as fails:
            rindas = fails.readlines()
            if len(rindas) >= 3:
                rindas = rindas[2]
                print("Trešā rinda: ", rindas)
            else:
                print("Kļūda: Nav pietiekami daudz rindu failā.")
    except FileNotFoundError:
        print(f"Fails '{ceļš}' netika atrasts.")
    except Exception as e:
        print(f"Nevarēja nolasīt failu. Kļūda: {e}")

faila_ceļš = '3.uzdevums.txt'
rinda(faila_ceļš)