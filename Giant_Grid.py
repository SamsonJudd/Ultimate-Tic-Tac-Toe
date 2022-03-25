#THIS FILE IS THE MAIN FILE THAT IS MEANT TO BE RUN TO BRING UP THE GRID. WE CANNOT USE THE IF NAME = MAIN BECAUSE NO
#FUNCTIONS ARE DEFINED HERE. ALL FUNCTIONS DEFINED ARE USED IN OTHER MODULES

from tkinter import *
import buttons_only as bo #IMPORTS THE BUTTONS FROM THE BUTTONS ONLY FILE SO THEY CAN BE PUT INTO A GIANT GRID




root = Tk()




bo.b1.grid(row=0, column=0) #Places b1 in the grid at a specific row and column, this repeats for all buttons
bo.b2.grid(row=0, column=1)
bo.b3.grid(row=0, column=2, padx=(0, 10)) #the pad function here creates an extra space between this and the one to its right, this repeats
bo.b4.grid(row=1, column=0)
bo.b5.grid(row=1, column=1)
bo.b6.grid(row=1, column=2, padx=(0, 10))
bo.b7.grid(row=2, column=0, pady=(0, 10))
bo.b8.grid(row=2, column=1, pady=(0, 10))
bo.b9.grid(row=2, column=2, pady=(0, 10), padx=(0, 10)) #the pad function here creates an extra space between this button and the one to its right as well as below it,this repeats
bo.b10.grid(row=0, column=3)
bo.b11.grid(row=0, column=4)
bo.b12.grid(row=0, column=5,padx=(0, 10))
bo.b13.grid(row=1, column=3)
bo.b14.grid(row=1, column=4)
bo.b15.grid(row=1, column=5, padx=(0, 10))
bo.b16.grid(row=2, column=3, pady=(0, 10))
bo.b17.grid(row=2, column=4, pady=(0, 10))
bo.b18.grid(row=2, column=5, pady=(0, 10),padx=(0, 10))
bo.b19.grid(row=0, column=6)
bo.b20.grid(row=0, column=7)
bo.b21.grid(row=0, column=8)
bo.b22.grid(row=1, column=6)
bo.b23.grid(row=1, column=7)
bo.b24.grid(row=1, column=8)
bo.b25.grid(row=2, column=6, pady=(0, 10))
bo.b26.grid(row=2, column=7, pady=(0, 10))
bo.b27.grid(row=2, column=8, pady=(0, 10))
bo.b28.grid(row=3, column=0)
bo.b29.grid(row=3, column=1)
bo.b30.grid(row=3, column=2, padx=(0, 10))
bo.b31.grid(row=4, column=0)
bo.b32.grid(row=4, column=1)
bo.b33.grid(row=4, column=2, padx=(0, 10))
bo.b34.grid(row=5, column=0,pady=(0, 10))
bo.b35.grid(row=5, column=1,pady=(0, 10))
bo.b36.grid(row=5, column=2, padx=(0, 10),pady=(0, 10))
bo.b37.grid(row=3, column=3)
bo.b38.grid(row=3, column=4)
bo.b39.grid(row=3, column=5,padx=(0, 10))
bo.b40.grid(row=4, column=3)
bo.b41.grid(row=4, column=4)
bo.b42.grid(row=4, column=5,padx=(0, 10))
bo.b43.grid(row=5, column=3,pady=(0, 10))
bo.b44.grid(row=5, column=4,pady=(0, 10))
bo.b45.grid(row=5, column=5,pady=(0, 10),padx=(0, 10))
bo.b46.grid(row=3, column=6)
bo.b47.grid(row=3, column=7)
bo.b48.grid(row=3, column=8)
bo.b49.grid(row=4, column=6)
bo.b50.grid(row=4, column=7)
bo.b51.grid(row=4, column=8)
bo.b52.grid(row=5, column=6,pady=(0, 10))
bo.b53.grid(row=5, column=7,pady=(0, 10))
bo.b54.grid(row=5, column=8,pady=(0, 10))
bo.b55.grid(row=6, column=0)
bo.b56.grid(row=6, column=1)
bo.b57.grid(row=6, column=2, padx=(0, 10))
bo.b58.grid(row=7, column=0)
bo.b59.grid(row=7, column=1)
bo.b60.grid(row=7, column=2, padx=(0, 10))
bo.b61.grid(row=8, column=0)
bo.b62.grid(row=8, column=1)
bo.b63.grid(row=8, column=2, padx=(0, 10))
bo.b64.grid(row=6, column=3)
bo.b65.grid(row=6, column=4)
bo.b66.grid(row=6, column=5,padx=(0, 10))
bo.b67.grid(row=7, column=3)
bo.b68.grid(row=7, column=4)
bo.b69.grid(row=7, column=5,padx=(0, 10))
bo.b70.grid(row=8, column=3)
bo.b71.grid(row=8, column=4)
bo.b72.grid(row=8, column=5,padx=(0, 10))
bo.b73.grid(row=6, column=6)
bo.b74.grid(row=6, column=7)
bo.b75.grid(row=6, column=8)
bo.b76.grid(row=7, column=6)
bo.b77.grid(row=7, column=7)
bo.b78.grid(row=7, column=8)
bo.b79.grid(row=8, column=6)
bo.b80.grid(row=8, column=7)
bo.b81.grid(row=8, column=8)






root.mainloop() #sets this file as the main file that will bring up the GUI

