# ==========================================
# UPPGIFT 1 (Löses av Elev A)
# ==========================================
def berakna_rabatt(pris: float, rabatt_procent: float) -> float:
    """Funktionen har en bugg! Den drar inte av rabatten korrekt.

    Rätta till matematiska formeln så att den returnerar det nya priset.
    Exempel: berakna_rabatt(100, 20) ska returnera 80.0
    """
    # BUGG: Just nu lägger den till rabatten istället för att dra ifrån!
    slutpris = pris - (pris * (rabatt_procent / 100))
    return slutpris


# ==========================================
# UPPGIFT 2 (Löses av Elev B)
# ==========================================
def validera_anvandarnamn(anvandarnamn: str) -> bool:
    if len(anvandarnamn) >= 5:
        return True;
    else:
        return False;
    """Funktionen är inte färdigbyggd.

    Ett användarnamn är giltigt (True) om det är minst 5 tecken långt.
    Annars ska den returnera False.
    """
    
    # TODO: Skriv en if-sats som kollar om anvandarnamn är minst 5 tecken långt (använd len()).
    # Just nu returnerar den alltid False.
    


# ==========================================
# UPPGIFT 3 - MERGE KONFLIKT (Löses av BÅDA samtidigt!)
# ==========================================
# OBS! Ändra INTE denna variabel förrän ni når Steg 4 i instruktionen!
TEAM_MEDLEMMAR = ["leo","Sixten"]

def visa_team():
    print("Registrerade medlemmar i teamet:")
    for medlem in TEAM_MEDLEMMAR:
        print(f"- {medlem}")

        