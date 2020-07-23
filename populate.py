import pandas as pd
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','element.settings')
import django
django.setup()
from table.models import Element


table = pd.read_csv("C:/Users/benja/Desktop/projetinApi/fontes/c2dd862cd38f21b0ad36b8f96b4bf1ee-1d92663004489a5b6926e944c1b3d9ec5c40900e/Periodic Table of Elements.csv")
firstfill = table.loc[:,['Element','Symbol','AtomicMass','AtomicNumber','NumberofNeutrons','NumberofProtons',
                     'NumberofElectrons','Phase','Radioactive','Type']]

firstfill['Radioactive'] = firstfill['Radioactive'].fillna('no')

secondfill = firstfill.iloc[:].values
i,j,matrix = 0,0,[]

while i<118:
    primeiroElemento = secondfill[i][:]
    dict = {'Element':primeiroElemento[j],'Symbol':primeiroElemento[j+1],'AtomicMass':primeiroElemento[j+2],
            'AtomicNumber':primeiroElemento[j+3],'NumberofNeutrons':primeiroElemento[j+4],
            'NumberofProtons':primeiroElemento[j+5],'NumberofElectrons':primeiroElemento[j+6],
            'Phase':primeiroElemento[j+7],'Radioactive':primeiroElemento[j+8],'Type':primeiroElemento[j+9]}
    matrix.append(dict)
    i += 1


def add_Element(elements, symbol, atomicNumber, numberofNeutrons,
                numberofProtons, numberofElectrons, phase, radioactive, Type,AtomicMass):

    c = Element.objects.get_or_create(element=elements)[0]
    c.symbol = symbol
    c.atomicNumber = atomicNumber
    c.numberofNeutrons = numberofNeutrons
    c.numberofProtons = numberofProtons
    c.numberofElectrons = numberofElectrons
    c.phase = phase
    c.radioactive = radioactive
    c.tp = Type
    c.atomicMass = AtomicMass
    c.save()
    return c

def populate():
    for valor in matrix:
        p = add_Element(valor['Element'], valor['Symbol'],
                        valor['AtomicNumber'], valor['NumberofNeutrons'],
                        valor['NumberofProtons'], valor['NumberofElectrons'],
                        valor['Phase'], valor['Radioactive'], valor['Type'],valor['AtomicMass'])

if __name__=='__main__':
    print("Starting Periodic Table population script...")
    populate()