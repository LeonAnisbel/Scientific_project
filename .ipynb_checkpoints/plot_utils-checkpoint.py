import matplotlib.pyplot as plt
import numpy as np
def function_plot(lats,lons,z,x,xlab='',ylab='',title=''):
    
    """
    Make a plot of the latitudinal cross-section of z  
    """


    a = np.searchsorted(lons,x) 
    z = z[:,a]       

    fig = plt.figure(figsize=[10, 5])
    plt.plot(lats, z)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.xlabel(xlab, fontsize=20)
    plt.ylabel(ylab, fontsize=20)
    plt.title(title, fontsize=20)
    plt.text(85, -5, r'North Pole', fontsize=18,color = 'r')
    plt.text(-120, -5, r'South Pole', fontsize=18,color = 'r')
    plt.text(-15, 2, r'Equator', fontsize=18,color = 'r')
    plt.ylim(0, 35)
    plt.show()