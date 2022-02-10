# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:54:58 2022

@author: HiroZar
"""

import cv2
from pyzbar.pyzbar import decode

img = cv2.imread("exampleQR.png")
for barcode in decode(img):
    """
    print(barcode)
    Result:
        Decoded(data=b'https://www.youtube.com/channel/UCjGRsLZ0RMt4SgGNx2wzE1Q', 
                type='QRCODE', rect=Rect(left=38, top=37, width=264, height=264), 
                polygon=[Point(x=38, y=37), Point(x=38, y=300), Point(x=302, y=301), 
                         Point(x=301, y=37)])
        
    Data = barcode.data
    print(Data)
    Result:
        b'https://www.youtube.com/channel/UCjGRsLZ0RMt4SgGNx2wzE1Q'
    """
    
Data = barcode.data.decode('utf-8') 
print(Data)

"""
    Result:
        https://www.youtube.com/channel/UCjGRsLZ0RMt4SgGNx2wzE1Q
"""