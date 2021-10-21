# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:29:13 2021

@author: Viktor Fran
"""
import csv
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

COLUMN = 2
OUTPUT_DELIMITER = '\u0009'

loop = True
while loop:
    print("Select File to Open in Pop-up Window")
    input_file = filedialog.askopenfilename()
    output_file = filedialog.asksaveasfilename(defaultextension='.tsv', filetypes=(("TSV Files", "*.tsv"),("All Files", "*.*") ))

    ifile = open(input_file, 'r')
    ofile = open(output_file, 'w') # x - create/error, a - append/create, w - write/create
    data = csv.reader(ifile, delimiter='\t')
    odata = []
    
    # j = 0
    # for row in data:
    #     if len(row) == 0:
    #         j = 0
    #     else:
    #         while len(row) < COLUMN:
    #                 row.insert(0,' ')
    #         if len(odata) <= j: # First Column
    #             odata.append(row)
    #             j += 1
    #         else:
    #             odata[j].extend(row)
    #             j += 1
    
    j = 0
    for row in data:
        if len(row) == 0:
            j = 0
        else:
            if len(odata) <= j: # First Column
                while len(row) < COLUMN:
                    row.insert(0,' ')
                odata.append(row)
                j += 1
            else:
                if len(row) < COLUMN:
                    odata[j].extend(row)
                    j += 1
                else:
                    odata[j].append(row[1])
                    j += 1
    for row in odata:
        for cell in row:
            ofile.write(cell + OUTPUT_DELIMITER)
        ofile.write('\n')
    
    ifile.close()
    ofile.close()
    print("Successfully Converted")
    
    ask_loop = input("Again? Y/n") or 'Y'
    if ask_loop == 'Y' or ask_loop == 'y' or ask_loop == 'yes':
        pass
    else:
        loop = False
        