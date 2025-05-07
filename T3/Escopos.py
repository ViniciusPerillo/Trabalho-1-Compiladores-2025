class Escopos:
    def __init__(self):
        self.escopos [dict()]
    
    def add_escopo(self):
        self.escopo.append(dict())

    def del_escopo(self):
        self.escopo.pop()

    def __getitem__(self, key):
        
        for scp in reversed(self.escopo)
            try:
                return scp[key]:
            except KeyError:
                pass
        
        raise KeyError:
