def failiņš():
    try:
        fails = input("Ievadiet faila nosaukumu (piemēram, fails.txt): ")
        
        # Lietotājs ievada faila formātu (paplašinājumu)
        formāts = input("Ievadiet faila formātu (piemēram, txt): ")
        
        # Apvienojam nosaukumu un formātu, lai iegūtu pilnu ceļu
        atrašanās = f"{fails}.{formāts}"

        with open(atrašanās, 'r', encoding='utf-8') as fails: