#!/usr/bin/env python3


from popup_list import *


def main():
    listitems = ['Amsterdam, Netherlands', 'Rotterdam, Netherlands', 'The Hague, Netherlands', 'Utrecht, Netherlands',
                 'Eindhoven, Netherlands', 'Tilburg, Netherlands', 'Groningen, Netherlands', 'Almere Stad, Netherlands',
                 'Breda, Netherlands', 'Nijmegen, Netherlands', 'Enschede, Netherlands', 'Haarlem, Netherlands',
                 'Arnhem, Netherlands', 'Zaanstad, Netherlands', 'Amersfoort, Netherlands', 'Apeldoorn, Netherlands',
                 ''s-Hertogenbosch, Netherlands', 'Hoofddorp, Netherlands', 'Maastricht, Netherlands',
                 'Leiden, Netherlands', 'Dordrecht, Netherlands', 'Zoetermeer, Netherlands', 'Zwolle, Netherlands',
                 'Deventer, Netherlands', 'Born, Netherlands', 'Delft, Netherlands', 'Alkmaar, Netherlands',
                 'Heerlen, Netherlands', 'Venlo, Netherlands', 'Leeuwarden, Netherlands',
                 'Amsterdam-Zuidoost, Netherlands', 'Hilversum, Netherlands', 'Hengelo, Netherlands',
                 'Amstelveen, Netherlands', 'Roosendaal, Netherlands', 'Purmerend, Netherlands', 'Oss, Netherlands',
                 'Schiedam, Netherlands', 'Spijkenisse, Netherlands', 'Helmond, Netherlands',
                 'Vlaardingen, Netherlands', 'Almelo, Netherlands', 'Gouda, Netherlands', 'Zaandam, Netherlands',
                 'Lelystad, Netherlands', 'Delfshaven, Netherlands', 'Alphen aan den Rijn, Netherlands',
                 'Hoorn, Netherlands', 'Velsen-Zuid, Netherlands', 'Ede, Netherlands', 'Bergen op Zoom, Netherlands',
                 'Capelle aan den IJssel, Netherlands', 'Assen, Netherlands', 'Nieuwegein, Netherlands',
                 'Veenendaal, Netherlands', 'Zeist, Netherlands', 'Den Helder, Netherlands', 'Hardenberg, Netherlands',
                 'Emmen, Netherlands', 'Oosterhout, Netherlands', 'Doetinchem, Netherlands', 'Kerkrade, Netherlands',
                 'Kampen, Netherlands', 'Weert, Netherlands', 'Woerden, Netherlands', 'Sittard, Netherlands',
                 'Heerhugowaard, Netherlands', 'Rijswijk, Netherlands', 'Middelburg, Netherlands',
                 'Emmeloord, Netherlands', 'Zwijndrecht, Netherlands', 'Waalwijk, Netherlands', 'Huizen, Netherlands',
                 'Vlissingen, Netherlands', 'Ridderkerk, Netherlands', 'Soest, Netherlands', 'Roermond, Netherlands',
                 'Drachten, Netherlands', 'Veldhoven, Netherlands', 'Heerenveen, Netherlands', 'Heusden, Netherlands',
                 'De Bilt, Netherlands', 'Medemblik, Netherlands', 'Tiel, Netherlands', 'Harderwijk, Netherlands',
                 'Maarssen, Netherlands', 'Venray, Netherlands', 'Hoogeveen, Netherlands', 'Barendrecht, Netherlands',
                 'Dronten, Netherlands', 'Nijkerk, Netherlands', 'Voorburg, Netherlands', 'Beverwijk, Netherlands',
                 'Goes, Netherlands', 'Zutphen, Netherlands', 'Heemskerk, Netherlands', 'Wageningen, Netherlands',
                 'Castricum, Netherlands', 'Gorinchem, Netherlands', 'Uden, Netherlands', 'Mijdrecht, Netherlands',
                 'IJsselstein, Netherlands', 'Epe, Netherlands', 'Sneek, Netherlands', 'Geleen, Netherlands',
                 'Maassluis, Netherlands', 'Wijchen, Netherlands', 'Houten, Netherlands', 'Papendrecht, Netherlands',
                 'Oldenzaal, Netherlands', 'Bussum, Netherlands', 'Valkenswaard, Netherlands', 'Meppel, Netherlands',
                 'Ypenburg, Netherlands', 'Winterswijk, Netherlands', 'Boxtel, Netherlands', 'Brunssum, Netherlands',
                 'Leusden, Netherlands', 'Best, Netherlands', 'Krimpen aan den IJssel, Netherlands',
                 'Heesch, Netherlands', 'Horst, Netherlands', 'Delfzijl, Netherlands', 'Barneveld, Netherlands',
                 'Veendam, Netherlands', 'Terneuzen, Netherlands', 'Geldrop, Netherlands', 'Uithoorn, Netherlands',
                 'Culemborg, Netherlands', 'Drimmelen, Netherlands', 'Dalfsen, Netherlands', 'Ermelo, Netherlands',
                 'Zaltbommel, Netherlands', 'Werkendam, Netherlands', 'Borger, Netherlands', 'Zevenaar, Netherlands',
                 'Oisterwijk, Netherlands', 'Leiderdorp, Netherlands', 'Geldermalsen, Netherlands',
                 'Heemstede, Netherlands', 'Beuningen, Netherlands', 'Broek op Langedijk, Netherlands',
                 'Wolvega, Netherlands', 'Duiven, Netherlands', 'Dongen, Netherlands', 'Wassenaar, Netherlands',
                 'Veghel, Netherlands', 'Waddinxveen, Netherlands', 'Anloo, Netherlands', 'Vught, Netherlands',
                 'Hoensbroek, Netherlands', 'Baarn, Netherlands', 'Noordwijk-Binnen, Netherlands',
                 'Diemen, Netherlands', 'Haaksbergen, Netherlands', 'Cuijk, Netherlands', 'Sliedrecht, Netherlands',
                 'Wijk bij Duurstede, Netherlands', 'Voorst, Netherlands', 'Steenbergen, Netherlands',
                 'Oud-Beijerland, Netherlands', 'Wierden, Netherlands', 'Schijndel, Netherlands', 'Nuenen, Netherlands',
                 'Putten, Netherlands', 'Oldebroek, Netherlands', 'Scheveningen, Netherlands',
                 'Loon op Zand, Netherlands', 'Aalsmeer, Netherlands', 'Goirle, Netherlands', 'Rucphen, Netherlands',
                 'Voorschoten, Netherlands', 'Losser, Netherlands', 'Lisse, Netherlands', 'Borssele, Netherlands',
                 'Veere, Netherlands', 'Volendam, Netherlands', 'Hellevoetsluis, Netherlands', 'Elburg, Netherlands',
                 'Hoogezand, Netherlands', 'Brummen, Netherlands', 'Woensdrecht, Netherlands',
                 'Oegstgeest, Netherlands', 'Hendrik-Ido-Ambacht, Netherlands', 'Geertruidenberg, Netherlands',
                 'Leerdam, Netherlands', 'Gendringen, Netherlands', 'Borne, Netherlands', 'Heiloo, Netherlands',
                 'Elst, Netherlands', 'Zundert, Netherlands', 'Tubbergen, Netherlands', 'Tegelen, Netherlands',
                 'Berkel en Rodenrijs, Netherlands', 'Raalte, Netherlands', 'Katwijk aan Zee, Netherlands',
                 'Stadskanaal, Netherlands', 'Cranendonck, Netherlands', 'Meerssen, Netherlands', 'Vianen, Netherlands',
                 'Tongelre, Netherlands', 'Leek, Netherlands', 'Lichtenvoorde, Netherlands', 'Wisch, Netherlands',
                 'Nunspeet, Netherlands', 'Bodegraven, Netherlands', 'Bladel, Netherlands',
                 ''s-Gravenzande, Netherlands', 'Aalten, Netherlands', 'Haren, Netherlands', 'Zeewolde, Netherlands',
                 'Benthuizen, Netherlands', 'Schagen, Netherlands', 'Groesbeek, Netherlands', 'Pijnacker, Netherlands',
                 'Driebergen-Rijsenburg, Netherlands', 'Winschoten, Netherlands', 'Heerde, Netherlands',
                 'Hillegom, Netherlands', 'Alblasserdam, Netherlands', 'Rhoon, Netherlands', 'Eersel, Netherlands',
                 'Bergeijk, Netherlands', 'Rhenen, Netherlands', 'Someren, Netherlands', 'Druten, Netherlands',
                 'Bunschoten, Netherlands', 'Weesp, Netherlands', 'Naaldwijk, Netherlands', 'Velp, Netherlands',
                 'Middelharnis, Netherlands', 'Broek in Waterland, Netherlands', 'Enkhuizen, Netherlands',
                 'Urk, Netherlands', 'Vlagtwedde, Netherlands', 'Beek, Netherlands', 'Steenwijk, Netherlands',
                 'Naarden, Netherlands', 'Sint-Oedenrode, Netherlands', 'Zandvoort, Netherlands',
                 'Bloemendaal, Netherlands', 'Korrewegwijk, Netherlands', 'Waalre, Netherlands', 'Gennep, Netherlands',
                 'Bergschenhoek, Netherlands', 'Eibergen, Netherlands', 'Asten, Netherlands', 'Lindenholt, Netherlands',
                 'Harlingen, Netherlands', 'Nederweert, Netherlands', 'Hoge Vucht, Netherlands',
                 'Westervoort, Netherlands', 'Harenkarspel, Netherlands', 'Staphorst, Netherlands', 'Nuth, Netherlands',
                 'Boskoop, Netherlands', 'Voorhout, Netherlands', 'Hilvarenbeek, Netherlands',
                 'Noordwijkerhout, Netherlands']

    answer, exitcode = popupInput().getInput('Cities', 'Please select your city?', listitems)

    if exitcode:
        print('Selected: %s\nExit Code: %d\n' % (answer, exitcode))
    else:
        print('Exited')


if __name__ == '__main__':
    main()
