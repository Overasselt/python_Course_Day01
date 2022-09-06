class Gebeurtenis:
    def __init__(self, intensieteit, datum, betrokken_gebruiker, omschrijving, locatie, omstandigheden):
        self.intensieteit = intensieteit
        self.datum = datum
        self.betrokken_gebruiker = betrokken_gebruiker
        self.omschrijving = omschrijving
        self.locatie = locatie
        self.omstandigheden = omstandigheden

    def __repr__(self):
        return ' - '.join(self.__dict__.values())

# ..................................................................
if __name__ == '__main__':
    gebeurtenissen = []

    gebeurtenissen.append( Gebeurtenis('**', '2-2-2022', 'ELNT huppelduif', 'Harde Landing', 'Woensdrecht', 'Mist'))
    gebeurtenissen.append( Gebeurtenis('***', '2-3-2022', 'ELNT huppelduif', 'Zeer harde Landing', 'Woensdrecht', 'Zonnig'))


    for Gebeurtenis in gebeurtenissen:
        print(Gebeurtenis)
