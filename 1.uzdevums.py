def zakits(ceļš):
    try:
        with open(ceļš, 'r', encoding='utf-8') as fails:
            # Nolasa faila saturu
            saturs = fails.read()
            # Izdrukā nolasīto saturu
            print("Fails: ", saturs)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{ceļš}' netika atrasts.")
    except Exception as bac:
        print(f"Kļūda: Nevarēja nolasīt failu. Kļūda: {bac}")

# Aizstājiet 'tavs_faila_ceļš.txt' ar reālu faila ceļu
faila_ceļš = '1.uzdevums.txt'
zakits(faila_ceļš)