eltalt_kartya = 5
nem_eltalt_kartya = 5

mumusok_pontszam = 0
tunderek_pontszam = 0
alommanok_pontszam = 0
almodo_pontszam= 0

def alommanok():
    if eltalt_kartya == nem_eltalt_kartya:
        alommanok_pontszam = eltalt_kartya+2    
    elif eltalt_kartya-nem_eltalt_kartya== 1 or eltalt_kartya-nem_eltalt_kartya== -1:
        if eltalt_kartya>nem_eltalt_kartya:
            alommanok_pontszam =eltalt_kartya       
        else:
            alommanok_pontszam= nem_eltalt_kartya 

    elif eltalt_kartya-nem_eltalt_kartya >=2:
        if eltalt_kartya>nem_eltalt_kartya:
            alommanok_pontszam=nem_eltalt_kartya
        else:
            alommanok_pontszam=eltalt_kartya
    elif eltalt_kartya-nem_eltalt_kartya <=-2:
        if eltalt_kartya>nem_eltalt_kartya:
            alommanok_pontszam=nem_eltalt_kartya
        else:
            alommanok_pontszam=eltalt_kartya
    return alommanok_pontszam

def tunderek():
    tunderek_pontszam = eltalt_kartya
    return tunderek_pontszam

def mumusok():
    mumusok_pontszam = nem_eltalt_kartya
    return mumusok_pontszam

def almodo():
    pont=0
    kerdes = int(input("Az álmodó fel tudta idézni az álmokat? Ha igen, akkor írj be egy 1-est, ha nem, akkor 2-est: ",))
    if kerdes == 1:
        pont = eltalt_kartya+2
    else:
        pont = eltalt_kartya
    return pont
    
print("Az álmodó pontszáma:",almodo())
print("A Tündérek pontszáma:", tunderek())
print("A Mumusok pontszáma:", mumusok())
print("Az Álommanók pontszáma:", alommanok())
