#matlab ile kullanmak için pcde matlab yüklü olmalı. o yüzden pythonda kütüphane kullanıldı.
#pip install matplotlib

import matplotlib.pyplot as plt
import pandas as pd

def makeGraphic(x, y,y2, grafik_adi='grafik.png', excel_adi='veri.xlsx'):
    plt.plot(x, y,label='NPS',color='blue')
    plt.scatter(x, y2,label='Problem',marker='o',color='red')
    plt.xlabel('Date')
    plt.ylabel('Nps Score')
    # plt.title('Problem')

    plt.savefig(grafik_adi)

    veri_cercevesi = pd.DataFrame({'X': x, 'Y': y})

    veri_cercevesi.to_excel(excel_adi, index=False)

    plt.show()

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# makeGraphic(x, y, grafik_adi='my_graph.png', excel_adi='my_data.xlsx')
