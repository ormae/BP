"""
Suunnitelma:
- Pääikkuna:
    pelaa
        # Ylös syötä pelaajat label
        # Neljä tekstiriviä, Alas oikealle haku nappula
        # Jos pelaajaa ei löydetä tietokannasta, sen tekstikentän alle
        # ilmestyy luo pelaaja nappula.
        # kun kaikki pelaajat ovat tietokannassa aloitetaan peli->
            peli
                Radionappuloita
                Alasvasen: takaisin Alasoikea: Syötätulos.
    tulokset
        highscoret layout toteutettu.

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

class UusiPeli(Screen):
    pelaajat1 = ObjectProperty(True)
    pelaajat2 = ObjectProperty(False)

class UusiPelaaja(Screen):

    """
    Luokka näytölle "Uusi pelaaja"
    """

    # Kivyn ominaisuus. Mahdollistaa nimen tallentamisen nappia painamalla.
    pelaajan_nimi_inputti = ObjectProperty()

    # Väliaikainen tietorakenne
    pelaajien_nimet = []

    def lataa_nimi(self):
        """
        Hakee pelaajan syöttämän nimen input kentästä ja tallentaa sen
        tietopankkiin
        """

        # Hakee tiedon tekstikentästä
        pelaajan_nimi = self.pelaajan_nimi_inputti.text

        # Jos ei ole nimeä tekstikentässä, huomauttaa
        if pelaajan_nimi == "":
            self.huomautus()
        else:
            # Lisäys väliaikaiseen pythonlistaan
            lista1.append(pelaajan_nimi)
            self.onnistuminen()
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
        self.ids.pelaajan_nimi.text = ""


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


root_widget = Builder.load_file("testi1.kv")
class PongApp(App):
    """ "App"-luokka, joka luo ite sovelluksen"""

    def build(self):
        # Returnaa 94-riviltä löytyvän muuttujan, joka sisältää kaikki
        # ulkonäölliset tiedot ikkunoista. Tämä täytyy returnaa, koska
        # sovelluksessa on monta ikkunaa
        return root_widget

PongApp().run()