class Onderhoud:
    def __init__(self, type, datum, door_wie, bevindingen):
        self.type = type
        self.datum = datum
        self.door_wie = door_wie
        self.onderdelen = []
        self.verbruiksmiddelen = []
        self.tooling = []
        self.bevindingen = bevindingen

    def __repr__(self):
        return ' - '.join(map(str,self.__dict__.values()))

    def add_onderdeel(self, onderdeel):
        self.onderdelen.append(onderdeel)

    def add_verbruiksmiddelen(self, verbruiksmiddel):
        self.verbruiksmiddelen.append(verbruiksmiddel)

    def add_tool(self, tool):
        self.tooling.append(tool)

# ..................................................................
if __name__ == '__main__':
    onderhoudsbeurten = []

    onderhoudsbeurten.append( Onderhoud('Regulier', '2-2-2022', 'ELNT Knuppel', 'Neuswiel'))
    onderhoudsbeurten.append( Onderhoud('Regulier', '2-3-2022', 'ELNT Knuppel', 'Staartrotor'))

    onderhoud = Onderhoud('Spoed onderhoud', '22-2-2022', 'Peter', 'OK')
    onderhoud.add_tool( tool('Steeksleutel 10', '234234'))
    onderhoud.add_tool( tool('Steeksleutel 16', '234234'))
    onderhoud.add_tool( tool('Steeksleutel 24', '234263'))
    onderhoudsbeurten.append( onderhoud)

    for Onderhoud in onderhoudsbeurten:
        print(Onderhoud)
