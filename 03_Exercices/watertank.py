class WaterTank:
    all_watertanks_fill_level = 0 # valeur a la creation de citernes
    all_watertanks_count = 0

    def __init__(self,base_weight:float, max_capacity:float,fill_level:float = 0):
        self.base_weight = base_weight
        self.max_capacity = max_capacity
        self.fill_level = fill_level
        # a chaque nouvelle citerne le niveau total augmente
        WaterTank.all_watertanks_fill_level += fill_level
        # a chaque nouvelle citerne le nombre de citerne augment
        WaterTank.all_watertanks_count += 1


    def total_weight(self):
        return self.base_weight + self.fill_level
    
    def fill(self, amount):
        self.fill_level += amount
        WaterTank.all_watertanks_fill_level += amount

    def empty(self,amount):
        self.fill_level -= amount
        WaterTank.all_watertanks_fill_level -= amount

    def __str__(self):
        return f"Citerne poid vide : {self.base_weight} niveau : {self.fill_level} capacite max : {self.max_capacity}"
    
if __name__ == "__main__":
    wt1 = WaterTank(1,10)
    wt2 = WaterTank(2,30,20)

    print(wt1)
    print(wt2)
    print("Niveau total : ",WaterTank.all_watertanks_fill_level)

    wt1.fill(8)
    print(wt1)
    print("Niveau total : ",WaterTank.all_watertanks_fill_level)

    wt1.empty(4)
    print(wt1)
    print("Niveau total : ",WaterTank.all_watertanks_fill_level)

        