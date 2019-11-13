
#Imports
############################################################
#!/usr/bin/python
# -*- coding: utf8 -*-
import math
import numpy as np
import matplotlib
from datetime import datetime , timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from scipy.integrate import odeint
import os
import sys
from bs4 import BeautifulSoup
import requests
from itertools import count
from matplotlib.animation import FuncAnimation
import time
from time import gmtime, strftime
from datetime import datetime
############################################################

# Gets Bitcoin Price from some website
def get_price():


    __author__ = "Engine Bai"

    #the website
    url = "https://www.coinbase.com/price/bitcoin"

    #requesting the website
    req = requests.get(url)
    html = BeautifulSoup(req.text, "html.parser")
    html = str(html)
    needle_in_haystack = """<div class="ChartPriceHeader__BigAmount-sc-9ry7zl-4 dKeshi">"""
    result = html.find(needle_in_haystack)

    #parsing out the price from the html
    html = html[result+len(needle_in_haystack):result+len(needle_in_haystack)+26]
    result = html.find("$")
    html = html[result:len(html)]
    result = html.find("<")
    html = html[0:result]
    html = html[1:len(html)]
    splitter = ","
    bitcoin_price = html
    bitcoin_price = str(bitcoin_price.replace(","," "))
    bitcoin_price = str(bitcoin_price.replace(" ",""))
    bitcoin_price = float(bitcoin_price)

    return bitcoin_price


#Time array
x_vals = []

#array for the value of my sharehold of a bitcoin
y_vals = []

#array for price of one bitcoin
z_vals = []

#special iterator function
index = count()

#Animation function
def Animate(i):
    x_vals.append(next(index))

    #gets current price of bitcoin
    price = get_price()
    oprice = price
    z_vals.append(oprice)

    #the amount of bit coin I own .215... % of one
    price *= (0.002150193313)
    nprice = price
    y_vals.append(nprice)

    #First Graph
    plt.subplot(1, 2, 1)
    plt.plot(x_vals , y_vals , 'y--')

    # x axis label
    plt.xlabel('Time (seconds)')
    # y axis label
    plt.ylabel("""Bitcoin Price ($ US Dollars)\n""")

    # Set y axis value limit
    plt.ylim(nprice-10, nprice+10)

    #set number of ticks on y axis
    plt.yticks(fontsize=6)

    # Setting the title up
    time = int(strftime("%H", gmtime()))
    time += 7
    t1 = str(strftime("%a, %d %b %Y " , gmtime() ))
    t2 = str(strftime(":%M:%S",gmtime()))
    plt.title(t1 +str(time)+ t2  + " Current Value of Sharehold: $" + str("{0:.2f}".format(price)), fontsize=7)


    #Second Graph
    plt.subplot(1,2,2)
    plt.plot(x_vals , z_vals , 'r--')

    # x axis label
    plt.xlabel('Time (seconds)')

    # y axis label
    plt.ylabel("""Bitcoin Price ($ US Dollars)\n""")

    # Set the limit
    plt.ylim(oprice-200, oprice+200)
    plt.yticks(fontsize =6)
    plt.yticks(fontsize=8, rotation=90)

    # Setting the title up
    time = int(strftime("%H", gmtime()))
    time += 7
    t1 = str(strftime("%a, %d %b %Y " , gmtime() ))
    t2 = str(strftime(":%M:%S",gmtime()))
    plt.title(t1 +str(time)+ t2  + " Current Price: $" + str("{0:.2f}".format(oprice)) ,fontsize=7)


#fancy function for real time animation with matplotlib
ani = FuncAnimation(plt.gcf() , Animate , interval = 1000)

#show us the magic
plt.show()
