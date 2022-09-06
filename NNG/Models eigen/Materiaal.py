class Materiaal:
    def __init__(self, naam, omschrijving, atacode, soort, partnummer, serienummer, positie):
        self.naam = naam
        self.omschrijving = omschrijving
        self.atacode = atacode
        self.soort = soort
        self.partnummer = partnummer
        self.serienummer = serienummer
        self.positie = positie

    def __repr__(self):
        return ' - '.join(self.__dict__.values())



# ..................................................................
if __name__ == '__main__':

    materieel = []

    materieel.append( Materiaal('landingsgestel F16', 'Neuswiellandingsgestel', '0023', 'landingsgestel', 'L23423455', '234242', 'front'))
    materieel.append( Materiaal('landingsgestel F16', 'Neuswiellandingsgestel', '0024', 'landingsgestel', 'L23423456', '423434', 'rechtsachter'))
    materieel.append( Materiaal('landingsgestel F16', 'Hoofdlandingsgestel', '0020', 'landingsgestel', 'L23423450', '345345', 'hoofd'))
    materieel.append( Materiaal('landingsgestel F35', 'Hoofdlandingsgestel', '0044', 'landingsgestel', 'M23423450', '345345', 'hoofd'))


    for materiaal in materieel:
        if 'F35' in materiaal.naam:
            print(materiaal)



# of alleen 1 item
# print(materiaal1.naam)