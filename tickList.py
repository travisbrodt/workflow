# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 02:59:37 2017

@author: tbrodt
"""
import win32clipboard                                   #Imports clipboard access
	
win32clipboard.OpenClipboard()                          #Imports everything from your clipboard and puts it in a list
data = win32clipboard.GetClipboardData().strip()

output = "'" + "','".join([str(i) for i in set(data.split())]) + "'"  

win32clipboard.EmptyClipboard()                         #Empty original pates clipboard
win32clipboard.SetClipboardText(output)                 #Puts data into clipboard
win32clipboard.CloseClipboard()                         #Close the clipboard
print(output)

#filter explanation = https://www.programiz.com/python-programming/methods/built-in/filter


