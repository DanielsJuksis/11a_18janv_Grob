import csv

def kolonaa2(csv_ceļš):
    try:
        with open(csv, 'r', encoding='utf-8') as csv_fails:
            lasa = csv.reader(csv_fails)
            for rinda in lasa:
                if len(rinda) >= 2:
                    otrakolona = rinda[1]
                    print("Otrās kolonnas dati: ", otrakolona)
                else:
                    print("Kļūda: Rindā nav otrās kolonnas!")
    except FileNotFoundError:
        print(f"Kļūda: Fails '{csv_ceļš}' nav.")
    except Exception:
        print(f"Kļūda: Nevarēja nolasīt CSV failu.")
csv_faila_ceļš = '2.uzdevums.csv'
kolonaa2(csv_faila_ceļš)