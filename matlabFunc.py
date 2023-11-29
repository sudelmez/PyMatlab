#matlab ile kullanmak için pcde matlab yüklü olmalı. o yüzden pythonda kütüphane kullanıldı.
#pip install matplotlib
import functools
import matplotlib
matplotlib.use("TkAgg") 
from matplotlib import pyplot as plt
import pandas as pd
plt.ion()  # Matplotlib interaktif modu

def on_point_click(event,ym):
    if event.artist.get_label() == 'Problem':
        index = int(event.ind[0])  
        problems = ym['Problem'].values
        selected_problem = problems[index]
        print(selected_problem)

def makeGraphic(x, y,y2, grafik_adi='grafik.png', excel_adi='veri.xlsx'):
    y3 = [0 if problem == '' else nps for problem, nps in zip(y2['Problem'].values, y2['Nps Score'].values)]

    plt.plot(x, y,label='NPS',color='blue')
    plt.scatter(x, y3,label='Problem',marker='o',color='red', picker=True)
    plt.xlabel('Date')
    plt.ylabel('Nps Score')

    plt.savefig(grafik_adi)

    plt.gcf().canvas.mpl_connect('pick_event', functools.partial(on_point_click, ym=y2))
    
    input("Grafik penceresini kapatmak için Enter tuşuna basın.")
    plt.show(block=False)
