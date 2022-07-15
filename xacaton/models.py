class Cars:
    objects = []

    def __init__(self, mark, model, year, vol_eng, color, type_, probeg, cost):
        self.mark = mark
        self.model = model
        self.year = year
        self.vol_eng = vol_eng
        self.color = color
        self.type_ = type_
        self.probeg = probeg
        self.cost = cost
        Cars.objects.append(self)
        
    def __str__(self):
        return self
