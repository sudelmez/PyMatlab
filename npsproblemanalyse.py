import pandas as pd
from tkinter import filedialog
import tkinter as tk
import re

print("started")
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title="İşlem Yapmak İstediğiniz Problems Datasını Seçin")
second_file_path = filedialog.askopenfilename(title="İşlem Yapmak İstediğiniz ONE NPS Datasını Seçin")

problems = pd.read_excel(file_path, sheet_name="Data")
nps_df = pd.read_excel(second_file_path, sheet_name="Data")

columns_nps = ['Channel', 'Nps Score', 'Date']
columns_problems = ['Date', 'Problem', 'Channel']

#çalıştığını kontrol etme döngüsü
for key, df in problems.items():
    if isinstance(df, pd.Series):
        print(f"Column for {key}: {df.name}")
    else:
        print(f"Columns for {key}: {df.columns}")

if 'reset_index' in globals():
    print("Warning: 'reset_index' variable detected in global namespace. This may cause conflicts.")

problems_concatenated = pd.concat([problems[columns_problems].reset_index(drop=True) for df in problems.keys()])
problems_concatenated = problems_concatenated.sort_values(by=['Date'])  #Date e göre sıralama
problems_concatenated['Problem'].fillna('', inplace=True)

merged_df = pd.merge(nps_df, problems_concatenated, on=['Date', 'Channel'], how='left') #böylelikle eşleşmeyenler de koyuldu
print("merged")
merged_df = merged_df.drop_duplicates() #duplikeleri sil


output_file_path = "/Users/sudeolmez/Desktop/" + input("Lütfen dışarı aktarılacak dosyanın adını belirtin:") + ".xlsx"
with pd.ExcelWriter(output_file_path) as writer:
    merged_df.to_excel(writer, sheet_name='Merged Data', index=False)

print("İşlemler tamamlandı, Tebrikler!")
