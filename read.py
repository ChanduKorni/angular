# -*- coding: utf-8 -*-
"""
Created on Wed May 29 04:59:42 2019

@author: Chandra Sekhar
"""

# Reading an excel file using Python 
import xlrd 

# Give the location of the file 
loc = ("Book1.xlsx")

# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

# For row 0 and column 0 
sheet.cell_value(0, 0) 

print(sheet.nrows) 

# Program extracting first column 
import xlrd 

loc = ("Book1.xlsx") 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 

for i in range(sheet.nrows): 
	print(sheet.cell_value(i, 0)) 

# Program to extract a particular row value 
import xlrd 

loc = ("Book1.xlsx") 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

sheet.cell_value(0, 0) 

print(sheet.row_values(6)) 
