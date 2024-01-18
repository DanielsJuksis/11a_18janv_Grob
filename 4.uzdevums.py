def failiņš():
    try:
        fails = input("Ievadiet faila nosaukumu (piemēram, fails.txt): ")
        formāts = input("Ievadiet faila formātu (piemēram, txt): ")
        
        atrašanās = f"{fails}.{formāts}"

        with open(atrašanās, 'r', encoding='utf-8') as fails: