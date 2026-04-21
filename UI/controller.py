import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0
        self._allSituazioni = None
        self._giornateTrascorseCitta = {"Genova":0, "Torino":0, "Milano":0}
        self._giornateConsecutive = 0



    def handle_umidita_media(self, e):
        self._view.lst_result.clean()
        self._view.update_page()
        if self._mese==0:
            self._view.create_alert("Scegliere un mese!")
            return
        if not self._allSituazioni:
            self._allSituazioni = self._model.getAllSituazioni()
        sommeUmidita = {"Genova":0, "Torino":0, "Milano":0}
        contatoriApparazioni = {"Genova":0, "Torino":0, "Milano":0}
        for s in self._allSituazioni:
            if (self._mese == s.data.month):
                sommeUmidita[s.localita] += int(s.umidita)
                contatoriApparazioni[s.localita] += 1

        medieUmidita = {"Genova": sommeUmidita["Genova"]/contatoriApparazioni["Genova"], "Torino": sommeUmidita["Torino"]/contatoriApparazioni["Torino"], "Milano": sommeUmidita["Milano"]/contatoriApparazioni["Milano"]}
        #medieUmiditaSorted = dict(sorted(medieUmidita.items(), key=lambda item: item[1], reverse=True))
        self._view.lst_result.controls.append(ft.Text(f"L'umidità media nel mese selezionato è:"))
        for citta,media in medieUmidita.items():
            self._view.lst_result.controls.append(ft.Text(f"{citta}: {round(media,4)}  (giorni contati: {contatoriApparazioni[citta]})"))
        self._view.update_page()

        return

    def handle_sequenza(self, e):
        if self._mese==0:
            self._view.create_alert("Scegliere un mese!")
            return
        if not self._allSituazioni:
            self._allSituazioni = self._model.getAllSituazioni()
        situazioniMese = [s for s in self._allSituazioni if (self._mese==s.data.month and s.data.day<=15)]
        situazioniMese.sort(key=lambda s:s.data)

        for i in range(1,16):
            situazioniGiorno = []
            for s in situazioniMese:

                if s.data.day == i:
                    situazioniGiorno.append(s)
                if len(situazioniGiorno) == 3:
                    break
            umiditaMinimaGiorno = min([s.umidita for s in situazioniGiorno])




        self.recursion(situazioniMese)
        return

    def read_mese(self, e):
        self._mese = int(e.control.value)

    def recursion(self,situazioni):
        pass
