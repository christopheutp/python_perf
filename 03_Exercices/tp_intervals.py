class IntervalError(Exception):
    pass

class Intervalle:
    def __init__(self,inf: int,sup: int):
        try:
            if not isinstance(inf,int) or not isinstance(sup,int):
                raise IntervalError
            
            if inf <= 0 or sup <= 0:
                raise IntervalError
            
            if sup <= inf:
                raise IntervalError

            self.__borne_inf = inf
            self.__borne_sup = sup

        except IntervalError:
            print("Erreur: Bornes invalides !!!")

    def modif_borne_sup(self,value):
        try:
            if not isinstance(value,int):
                raise IntervalError
            
            if value <= self.__borne_inf:
                raise IntervalError

            self.__borne_sup = value

        except IntervalError:
            print("Erreur: Bornes invalides !!!")

    def modif_borne_inf(self,value):
        try:
            if not isinstance(value,int):
                raise IntervalError
            
            if value > self.__borne_sup or value <= 0:
                raise IntervalError

            self.__borne_inf = value

        except IntervalError:
            print("Erreur: Bornes invalides !!!")

    def lire_inf(self):
        return self.__borne_inf
    
    def lire_sup(self):
        return self.__borne_sup
    
    def __str__(self):
        return f"De {self.__borne_inf} à {self.__borne_sup}"
    
    def __contains__(self,value):
        return self.__borne_inf <= value <= self.__borne_sup
    
    # def __add__(self,inf,sup):
    #     return Intervalle(self.__borne_inf+inf,self.__borne_sup+sup)
    
    def __add__(self,other):
        if not isinstance(other,Intervalle):
                raise TypeError
        
        return Intervalle(self.__borne_inf + other.lire_inf(),self.__borne_sup + other.lire_sup())
    
    def __sub__(self,other):
        if not isinstance(other,Intervalle):
                raise TypeError
        
        return Intervalle(self.__borne_inf - other.lire_inf(),self.__borne_sup - other.lire_sup())
    
    def __mul__(self,other):
        if not isinstance(other,Intervalle):
                raise TypeError
        
        return Intervalle(self.__borne_inf * other.lire_inf(),self.__borne_sup * other.lire_sup())
    
    def __and__(self,other):
        if not isinstance(other,Intervalle):
                raise TypeError
        
        min_value = max(self.__borne_inf,other.lire_inf())
        max_value = min(self.__borne_sup,other.lire_sup())

        if min_value < max_value:
             return Intervalle(min_value,max_value)
        else:
             return None
        

if __name__ == '__main__':
     intervalleA = Intervalle(2,8)
     intervalleB = Intervalle(8,2)
     print(intervalleA)
     print(intervalleA.__contains__(4))
     print(intervalleA.__contains__(9))
     print(5 in intervalleA)
     intervalleC = Intervalle(2,8)
     intervalleD = intervalleA + intervalleC
     print(intervalleD)