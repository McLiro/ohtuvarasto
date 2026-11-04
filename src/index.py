from varasto import Varasto

#liian pitkä kommentti, jota pylint ei sallisi, mutta kirjoitankin sen kuitenkin että voin testata, pylintin toimintaa githubissa.

def tulosta_luodut_varastot(mehua, olutta):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


def tulosta_oluen_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def muokkaa_mehuvarastoa(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def tulosta_virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)
    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def kokeile_lisayksia(mehua, olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def ota_olutta(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")


def ota_mehua(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def kokeile_ottoja(mehua, olutta):
    ota_olutta(olutta)
    ota_mehua(mehua)


def suorita_esimerkki(mehua, olutta):
    tulosta_luodut_varastot(mehua, olutta)
    tulosta_oluen_getterit(olutta)
    muokkaa_mehuvarastoa(mehua)
    tulosta_virhetilanteet()
    kokeile_lisayksia(mehua, olutta)
    kokeile_ottoja(mehua, olutta)


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    suorita_esimerkki(mehua, olutta)


if __name__ == "__main__":
    main()
