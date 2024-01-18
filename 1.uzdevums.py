def zakits(ceļš):
    try:
        with open(ceļš, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print("Fails: ", saturs)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{ceļš}' netika atrasts.")
    except Exception as bac:
        print(f"Kļūda: Nevarēja nolasīt failu. Kļūda: {bac}")

faila_ceļš = '1.uzdevums.txt'
zakits(faila_ceļš)