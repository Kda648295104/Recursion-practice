jug1 = 0
jug2 = 0
def fill(jug1,jug2,n):
    if jug1 != n :
        print("Pump %d gallon in to jug1"%(4-jug1))
        jug1 = 4 - jug1  #4
        print("Pump 3 gallon in to jug2 from jug1")#3#2
        jug2 = 3 - jug2  #3
        jug1 = jug1 - jug2#1
        if jug1 == n:
            return None
        print("Pump out %d gallon from jug2"%jug2)
        print("Pump %d gallon in to jug2 from jug1 again" %jug1)
        jug2 = jug1#1
        jug1 = 0#0
        return fill(jug1,jug2,n)

fill(jug1,jug2,3)