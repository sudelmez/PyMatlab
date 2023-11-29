import pandas as pd
from tkinter import filedialog
import tkinter as tk
import re
from matlabFunc import makeGraphic
#pip install openpyxl

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

print("Kaydetme işlemi tamamlandı.")

filtered_df_CC = merged_df[merged_df['Channel'] == 'CC'].copy()
filtered_df_CC['Problem'].fillna('', inplace=True)
listCCProblem = [0 if problem == '' else nps for problem, nps in zip(filtered_df_CC['Problem'].values, filtered_df_CC['Nps Score'].values)]
makeGraphic(filtered_df_CC['Date'].values, filtered_df_CC['Nps Score'].values, filtered_df_CC)

# filtered_df_7000 = merged_df[merged_df['Channel'] == '7000'].copy()
# filtered_df_7000['Problem'].fillna('', inplace=True)
# list7000Problem = [0 if problem == '' else nps for problem, nps in zip(filtered_df_7000['Problem'].values, filtered_df_7000['Nps Score'].values)]
# makeGraphic(filtered_df_7000['Date'].values, filtered_df_7000['Nps Score'].values, list7000Problem)