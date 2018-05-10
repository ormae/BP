"""
Suunnitelma:
- Pääikkuna:
    pelaa
        Valmispeliinlista = [False,False,False,False]

        # Ylös syötä pelaajat label
        # Neljä Entryriviä, Alas oikealle haku nappula, Alas vasemmalle
        # takaisin-nappula

        # Jos pelaajaa ei löydetä tietokannasta, sen tekstikentän alle
        # ilmestyy "luo pelaaja"-nappula.


            haku
                # Jos pelaaja löytyy tietokannassa muutetaan sen seuraavan listan
                # totuus arvo sen pelaajan indeksille.(Valmispeliinlista)
            luo uusipelaaja
                # Luodaan uusipelaaja ja muutetaan Valmispeliin listaa.


            # kun kaikki pelaajat ovat tietokannassa aloitetaan peli->
                peli
                    Radionappuloita
                    Alasvasen: takaisin Alasoikea: Syötätulos.
    tulokset
        highscoret layout toteutettu. Tietorakenne toteuttamattas

"""


# Importteja
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

kivy.require('1.10.0')

lista = {"tomi": [1, 0], "elkku": [3, 3]}

lista1 = ["1.   tomi   ", "3", "3", "3", "3","3", "3", "3", "3","3", "3", "3", "3"
          ,"3", "3", "3", "3","3", "3", "3", "3","3", "3", "3", "3"]


# Luokka PopUp-ikkunalle, joka tulee esille, kun käyttäjä tallentaa nimen
# tietorakenteeseen
class PopUpIkkunaOnnistuminen(Popup):
    """
    Luokka PopUp-ikkunalle, joka tulee esille, kun käyttäjä tallentaa nimen
    tietorakenteeseen
    """

    pass


class PopUpIkkunaEpäonnistuminen(Popup):
    """
    Luokka PopUp-ikkunalle, joka tulee esille, kun käyttäjä ei onnistu
    tallentamaan nimeä tietorakenteeseen
    """
    pass


class BeerPong(Screen):
    """Luokka päänäytölle, josta voi valita joko "Uusi peli", "Uusi pelaaja"
    tai "Tilastot" """

    pass

class Peli(Screen):
    pelaajat1 = ObjectProperty(True)
    pelaajat2 = ObjectProperty(False)

class UusiPeli(Screen):

    """
    Luokka näytölle "Uusi pelaaja"
    """

    # Joukkue 1
    pelaaja1 = ObjectProperty()
    pelaaja2 = ObjectProperty()

    # Joukkue 2
    pelaaja3 = ObjectProperty()
    pelaaja4 = ObjectProperty()

    # Väliaikainen tietorakenne
    pelaajien_nimet = []

    def lataa_nimi(self):
        """
        Hakee pelaajan syöttämän nimen input kentästä ja tallentaa sen
        tietopankkiin
        """

        # Hakee tiedon tekstikentästä
        pelaajan_nimet = [self.pelaaja1.text,self.pelaaja2.text,
                          self.pelaaja3.text,self.pelaaja4.text]
        valilista = []
        # Jos ei ole nimeä tekstikentässä, huomauttaa
        for nimi in pelaajan_nimet:
            if nimi == "":
                self.huomautus()
                valilista.clear()
                break
            else:
                # Lisäys väliaikaiseen pythonlistaan
                valilista.append(nimi)

        if valilista != []:
            # lisätään väliaikaisen listan sisältö päätietokantaan jos ei ole
            # tyhjiä nimiä
            for lisattavat in valilista:
                lista1.append(lisattavat)
            print(lista1)


    # Metodi onnistumisesta kertovalle PopUp-ikkunale
    def huomautus(self):
        huomautus_ikkuna = PopUpIkkunaEpäonnistuminen()
        huomautus_ikkuna.open()

    # Metodi epäonnistumisesta kertovalle PopUp-ikkunale
    def onnistuminen(self):
        onnistuminen_ikkuna = PopUpIkkunaOnnistuminen()
        onnistuminen_ikkuna.open()

    # Metodi, joka tyhjentaa tekstikentän, kun käyttäjä siirtyy takaisin
    # päänäyttöön
    def tyhjenna(self):
        self.ids.p1.text = ""
        self.ids.p2.text = ""
        self.ids.p3.text = ""
        self.ids.p4.text = ""


class Tilastot(Screen):
    lista2 = lista1

    # Tällä hetkellä ylimääräinen, ehkä myöhemmin tarvitsee

    """def paivita_lista(self):
        self.objekti_lista._trigger_reset_populate()
        sortat_nimet = reversed(
            sorted(lista.items(), key=lambda x: x[1][0] / (x[1][0] + x[1][1])))

        for i in sortat_nimet:
            lista.append(i)
            lista1.append("{}, {}, {}, {}".format(i[0], i[1][0], i[1][1], (
                    i[1][0] / (i[1][0] + i[1][1])) * 100))"""




class NaytonOhjausta(ScreenManager):
    """Luokka, joka ohjaa näyttöjä, kun niistä on tehty liikkuvia"""

    # Jotta nimen saa ladattua, täytyy tehdä metodia myös tänne NaytonOhjausta
    # luokkaan
    def lataa_nimi(self):
        # Käyttää kyseessä olevalle screenille metodia lataa_nimi(), joka tässä
        # tapauksessa on screenille/oliolle UusiPelaaja
        self.lataa_nimi()


root_widget = Builder.load_file("BP1.kv")
class PongApp(App):
    """ "App"-luokka, joka luo ite sovelluksen"""

    def build(self):
        # Returnaa 94-riviltä löytyvän muuttujan, joka sisältää kaikki
        # ulkonäölliset tiedot ikkunoista. Tämä täytyy returnaa, koska
        # sovelluksessa on monta ikkunaa
        return root_widget

PongApp().run()