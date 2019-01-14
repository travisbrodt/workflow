# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 02:59:37 2017

@author: tbrodt
"""
import win32clipboard

win32clipboard.OpenClipboard()
text = win32clipboard.GetClipboardData().strip()

print(text)
output = ",".join([str(i) for i in set(text.split())])

print(output)

win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(output)
win32clipboard.CloseClipboard()

