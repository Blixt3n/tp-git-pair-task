"""
TEAMPUSSLET - Tillämpad Programmering
Ett skript som testar modul-funktioner när de är färdigbyggda.
"""
from tasks import berakna_rabatt, validera_anvandarnamn, visa_team

def main():
    print("=== VÄLKOMMEN TILL TEAMPUSSLET ===")

    # Test för Uppgift 1
    print("\n--- Testar Uppgift 1: Rabattberäkning ---")
    resultat1 = berakna_rabatt(100, 20)
    if resultat1 == 80.0:
        print("Uppgift 1 PASSERAD! (Rabatten beräknades korrekt till 80.0 kr)")
    else:
        print(f"Uppgift 1 EJ: Fick {resultat1}, förväntade mig 80.0")

    # Test för Uppgift 2
    print("\n--- Testar Uppgift 2: Användarnamn ---")
    test_namn = "Programmerare"
    resultat2 = validera_anvandarnamn(test_namn)
    if resultat2 == True:
        print(f"Uppgift 2 PASSERAD! '{test_namn}' godkändes korrekt.")
    else:
        print(f"Uppgift 2 EJ KLAR: '{test_namn}' blev inte godkänt.")

    # Test för Uppgift 3
    print("\n--- Testar Uppgift 3: Teaminformation ---")
    visa_team()


if __name__ == "__main__":
    main()