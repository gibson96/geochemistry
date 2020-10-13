import scipy.stats as sci
from scipy.signal import savgol_filter as savfil
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

def pXRF_plot(file_all, file_avg, title, top_depth, bot_depth): #Defining a fuction to plot 
    
    """
    Summary
    -------
    Function to create plots of grain size proxies, proximity, major lithological components, and RedOx proxies from pXRF data
    
    Parameters
    ----------
    file_all: path to .csv file containing all pXRF values for each depth
    file_avg: path to .csv file containing only the average values for each depth
    title: string name of material/location e.g. "Peniche"
    top_depth: Float, depth to top of the core section to be plotted
    bot_depth: Float, depth to bottom of the core section to be plotted
    
    Returns
    -------
    Plot: "title_pxrf.pdf", including graphs of major lithological components, grain size proxies, and RedOx proxies
    """

#Lists produced from each column of the file_all .csv
    sample_depth = []
    Mg = []
    Al = []
    Si = []
    Phos = [] #Phosphorous
    Sul = [] #Sulphur
    KPot = [] #Potassium
    Ca = []
    Ti = []
    Van = [] #Vanadium
    Cr = []
    Mn = []
    Fe = []
    Co = []
    Ni = []
    Cu = []
    Zn = []
    Ars = [] #Arsenic, renamed from As to avoid conflicts
    Se = []
    Rb = []
    Sr = []
    Ytt = [] #Ytterbium
    Zr = []
    Nb = []
    Mo = []
    Ag = []
    Cd = []
    Sn = []
    Sb = []
    Wtun = [] #Tungsten
    Hg = []
    Pb = []
    Bi = []
    Th = []
    Ura = [] #Uranium
    LE = [] #"Lighter Elements", eg. Carbon, Oxygen, etc.
    
    
    with open(file_all, mode='r') as csv_pxrf_all:
        pxrf_all = csv.reader(csv_pxrf_all)
        next(csv_pxrf_all)
        for row in pxrf_all:
            sample_depth.append(float(row[0])) #append the 1st value in each row to the sample_depth list. "Float" required as otherwise it adds the values as strings, not numbers
            Mg.append(float(row[2]))
            Al.append(float(row[4]))
            Si.append(float(row[6]))
            Phos.append(float(row[8]))
            Sul.append(float(row[10]))
            KPot.append(float(row[12]))
            Ca.append(float(row[14]))
            Ti.append(float(row[16]))
            Van.append(float(row[18]))
            Cr.append(float(row[20]))
            Mn.append(float(row[22]))
            Fe.append(float(row[24]))
            Co.append(float(row[26]))
            Ni.append(float(row[28]))
            Cu.append(float(row[30]))
            Zn.append(float(row[32]))
            Ars.append(float(row[34]))
            Se.append(float(row[36]))
            Rb.append(float(row[38]))
            Sr.append(float(row[40]))
            Ytt.append(float(row[42]))
            Zr.append(float(row[44]))
            Nb.append(float(row[46]))
            Mo.append(float(row[48]))
            Ag.append(float(row[50]))
            Cd.append(float(row[52]))
            Sn.append(float(row[54]))
            Sb.append(float(row[56]))
            Wtun.append(float(row[58]))
            Hg.append(float(row[60]))
            Pb.append(float(row[62]))
            Bi.append(float(row[64]))
            Th.append(float(row[66]))
            Ura.append(float(row[68]))
            LE.append(float(row[70]))
    
#Lists produced from each column of the file_avg .csv
    sample_depth_avg = []
    Mg_avg = []
    Al_avg = []
    Si_avg = []
    Phos_avg = [] #Phosphorous
    Sul_avg = [] #Sulphur
    KPot_avg = [] #Potassium
    Ca_avg = []
    Ti_avg = []
    Van_avg = [] #Vanadium
    Cr_avg = []
    Mn_avg = []
    Fe_avg = []
    Co_avg = []
    Ni_avg = []
    Cu_avg = []
    Zn_avg = []
    Ars_avg = [] #Arsenic, renamed from As to avoid conflicts
    Se_avg = []
    Rb_avg = []
    Sr_avg = []
    Ytt_avg = [] #Ytterbium
    Zr_avg = []
    Nb_avg = []
    Mo_avg = []
    Ag_avg = []
    Cd_avg = []
    Sn_avg = []
    Sb_avg = []
    Wtun_avg = [] #Tungsten
    Hg_avg = []
    Pb_avg = []
    Bi_avg = []
    Th_avg = []
    Ura_avg = [] #Uranium
    LE_avg = [] #"Lighter Elements", eg. Carbon, Oxygen, etc.
    
    
    with open(file_avg, mode='r') as csv_pxrf_avg:
        pxrf_avg = csv.reader(csv_pxrf_avg)
        next(csv_pxrf_avg)
        for row in pxrf_avg:
            sample_depth_avg.append(float(row[0])) #append the 1st value in each row to the sample_depth list. "Float" required as otherwise it adds the values as strings, not numbers
            Mg_avg.append(float(row[2]))
            Al_avg.append(float(row[4]))
            Si_avg.append(float(row[6]))
            Phos_avg.append(float(row[8]))
            Sul_avg.append(float(row[10]))
            KPot_avg.append(float(row[12]))
            Ca_avg.append(float(row[14]))
            Ti_avg.append(float(row[16]))
            Van_avg.append(float(row[18]))
            Cr_avg.append(float(row[20]))
            Mn_avg.append(float(row[22]))
            Fe_avg.append(float(row[24]))
            Co_avg.append(float(row[26]))
            Ni_avg.append(float(row[28]))
            Cu_avg.append(float(row[30]))
            Zn_avg.append(float(row[32]))
            Ars_avg.append(float(row[34]))
            Se_avg.append(float(row[36]))
            Rb_avg.append(float(row[38]))
            Sr_avg.append(float(row[40]))
            Ytt_avg.append(float(row[42]))
            Zr_avg.append(float(row[44]))
            Nb_avg.append(float(row[46]))
            Mo_avg.append(float(row[48]))
            Ag_avg.append(float(row[50]))
            Cd_avg.append(float(row[52]))
            Sn_avg.append(float(row[54]))
            Sb_avg.append(float(row[56]))
            Wtun_avg.append(float(row[58]))
            Hg_avg.append(float(row[60]))
            Pb_avg.append(float(row[62]))
            Bi_avg.append(float(row[64]))
            Th_avg.append(float(row[66]))
            Ura_avg.append(float(row[68]))
            LE_avg.append(float(row[70]))

  
#Major Lithological Components
    
    #savename = title + ' Major Lithological Components'
    
    fig, axs = plt.subplots(3, figsize=(20,10), sharex=True)
    plt.minorticks_on()
    axs[0].scatter(sample_depth, Si, color="khaki")
    axs[0].plot(sample_depth_avg, Si_avg, color="Goldenrod")
    axs[0].set_ylabel('Sand Content (%Si)')
    axs[0].set_xlim(top_depth, bot_depth)
    axs[1].scatter(sample_depth, Al, color="lightgreen")
    axs[1].plot(sample_depth_avg, Al_avg, color="forestgreen")
    axs[1].set_ylabel('Clay Content (%Al)')
    axs[2].scatter(sample_depth, Ca, color="lightsteelblue")
    axs[2].plot(sample_depth_avg, Ca_avg, color="royalblue")
    axs[2].set_ylabel('Carbonate content (%Ca)')
    axs[2].set_xlabel('Depth(m)')
    fig.suptitle(title + " Major Lithological Components")    
    fig.tight_layout()
    fig.subplots_adjust(top=0.95) #Essentially removes huge gap from between title and plots
    plt.savefig(title + ' Major_Lithological_Components.pdf') 
    plt.show()
    

#Grain Size and Proximity
    a = np.array(Si)
    b = np.array(Al)
    Si_Al = a/b #Calculate Si/Al ratio for all values
    
    a_avg = np.array(Si_avg)
    b_avg = np.array(Al_avg)
    Si_Al_avg = a_avg/b_avg #Calculate Si/Al ratio for average values at each depth

    c = np.array(KPot)
    d = np.array(Rb)
    K_Rb = c/d #Calculate K/Rb ratio for all values
    
    c_avg = np.array(KPot_avg)
    d_avg = np.array(Rb_avg)
    K_Rb_avg = c_avg/d_avg #Calculate K/Rb ratio for average values at each depth
    
    e = np.array(Zr)
    f = np.array(Rb)
    Zr_Rb = e/f

    e_avg = np.array(Zr_avg)
    f_avg = np.array(Rb_avg)
    Zr_Rb_avg = e_avg/f_avg

    coeff, pval = sci.pearsonr(Si_Al_avg, K_Rb_avg) #Calculate Pearson's corellation coefficient
    round_coeff = np.around(coeff, 2) #Round it to 2 dp
    
    fig, axs = plt.subplots(2, figsize=(20,10), sharex=True)
    plt.minorticks_on()
    axs[0].scatter(sample_depth, Si_Al, color='khaki')
    axs[0].plot(sample_depth_avg, Si_Al_avg, color='goldenrod', label='Si/Al')
    axs[0].text(0.01, 0.05, 'Finer', weight='bold', transform=axs[0].transAxes)
    axs[0].text(0.01, 0.90, 'Coarser', weight='bold', transform=axs[0].transAxes)
    axs[0].text(0.90, 0.10, 'Correlation Coefficient:', weight='bold', transform=axs[0].transAxes)
    axs[0].text(0.90, 0.05, round_coeff, weight='bold', transform=axs[0].transAxes) #Plot rounded correlation coeff on graph
    axs[0].set_ylabel('Grain Size (Si/Al)')
    axs[0].set_xlim(top_depth, bot_depth)
    axs[0].legend()
    axs[0] = axs[0].twinx()
    axs[0].scatter(sample_depth, K_Rb, color='pink')
    axs[0].plot(sample_depth_avg, K_Rb_avg, color='purple', label='K/Rb')
    #axs[1].text(0.01, 0.05, 'Finer', weight='bold', transform=axs[1].transAxes)
    #axs[1].text(0.01, 0.90, 'Coarser', weight='bold', transform=axs[1].transAxes)
    axs[0].set_ylabel('Grain Size (K/Rb)')
    axs[0].legend()
    axs[1].scatter(sample_depth, Zr_Rb)
    axs[1].plot(sample_depth_avg, Zr_Rb_avg)
    axs[1].text(0.01, 0.05, 'More Distal', weight='bold', transform=axs[1].transAxes)
    axs[1].text(0.01, 0.90, 'More Proximal', weight='bold', transform=axs[1].transAxes)
    axs[1].set_ylabel('Proximity proxy (Zr/Rb)')
    axs[1].set_xlabel('Depth(m)')
    fig.suptitle(title + " Grain Size and Proximity Proxies")    
    fig.tight_layout()
    fig.subplots_adjust(top=0.95) #Essentially removes huge gap from between title and plots
    plt.savefig(title + '_GrainSize_Proximity.pdf')
    plt.show()
    


#Clay Types - Humidity
    
    Hum_arid = (np.array(Al))/(np.array(KPot))
    Hum_arid_avg = (np.array(Al_avg))/(np.array(KPot_avg))
    
    fig, ax = plt.subplots(figsize=(20,6), sharex=True)
    plt.minorticks_on()
    ax.set_ylabel('Kaolinite/Illite (Al/K)')
    #ax.set_ylim(0,1.0)
    ax.set_xlim(top_depth, bot_depth)
    ax.scatter(sample_depth, Hum_arid, color='tan')
    ax.plot(sample_depth_avg, Hum_arid_avg, color='saddlebrown')
    ax.text(0.03, 0.05, 'More Arid', weight='bold', transform=ax.transAxes)
    ax.text(0.03, 0.90, 'More Humid', weight='bold', transform=ax.transAxes)
    fig.suptitle(title + " Humidity")    
    fig.tight_layout()
    fig.subplots_adjust(top=0.95) #Essentially removes huge gap from between title and plots
    plt.savefig(title + '_Humidity.pdf')
    plt.show()
    

#Productivity and Clay types

    Prod = (np.array(Phos))/(np.array(Al)) #Productivity proxy of Phosphorous normalised to aluminium
    Prod_avg = (np.array(Phos_avg))/(np.array(Al_avg))
        
    fig, ax = plt.subplots(figsize=(20,6))
    plt.minorticks_on()
    ax.set_ylabel('P/Al')
    #ax.set_ylim(0, 0.1)
    ax.set_xlim(top_depth, bot_depth)
    ax.scatter(sample_depth, Prod, color='palegreen')
    ax.plot(sample_depth_avg, Prod_avg, color='forestgreen')
    ax.text(0.03, 0.05, 'Less Productive', weight='bold', transform=ax.transAxes)
    ax.text(0.03, 0.90, 'More Productive', weight='bold', transform=ax.transAxes)
    fig.suptitle(title + " Productivity")    
    fig.tight_layout()
    fig.subplots_adjust(top=0.95) #Essentially removes huge gap from between title and plots
    plt.savefig(title + '_Productivity.pdf')
    plt.show()


#RedOx Proxies

    Ars_Al = (np.array(Ars))/(np.array(Al))
    Mo_Al = (np.array(Mo))/(np.array(Al))
    Cu_Al = (np.array(Cu))/(np.array(Al))
    Ni_Al = (np.array(Ni))/(np.array(Al))
    Fe_Al = (np.array(Fe))/(np.array(Al))
    Sul_Al = (np.array(Sul))/(np.array(Al))
    
    Ars_Al_avg = (np.array(Ars_avg))/(np.array(Al_avg))
    Mo_Al_avg = (np.array(Mo_avg))/(np.array(Al_avg))
    Cu_Al_avg = (np.array(Cu_avg))/(np.array(Al_avg))
    Ni_Al_avg = (np.array(Ni_avg))/(np.array(Al_avg))
    Fe_Al_avg = (np.array(Fe_avg))/(np.array(Al_avg))
    Sul_Al_avg = (np.array(Sul_avg))/(np.array(Al_avg))

    
    fig, axs = plt.subplots(2, figsize=(20, 12), sharex=True)
    plt.minorticks_on()
    axs[0].set_ylabel('S/Al. Fe/Al')
    #axs[0].set_ylim(0, 13)
    axs[0].scatter(sample_depth, Sul_Al, color="darkkhaki")
    axs[0].plot(sample_depth_avg, Sul_Al_avg, color="Olive", label='S/Al')
    axs[0].set_xlim(top_depth, bot_depth)
    axs[0].text(0.03, 0.05, 'More Oxic', weight='bold', transform=axs[0].transAxes)
    axs[0].text(0.03, 0.90, 'Less Oxic', weight='bold', transform=axs[0].transAxes)
    #axs[0].set_ylabel('%Fe')
    axs[0].scatter(sample_depth, Fe_Al, color="lightcoral")
    axs[0].plot(sample_depth_avg, Fe_Al_avg, color="Firebrick", label='Fe/Al')
    #axs[0].text(0.03, 0.05, 'More Oxic', weight='bold', transform=axs[1].transAxes)
    #axs[0].text(0.03, 0.90, 'Less Oxic', weight='bold', transform=axs[1].transAxes)
    axs[0].legend()
    axs[1].set_ylabel('Ni/Al, Cu/Al, Mo/Al, Ars/Al')
    #axs[1].set_ylim(0,0.01)
    axs[1].scatter(sample_depth, Ni_Al, color="cornflowerblue")
    axs[1].plot(sample_depth_avg, Ni_Al_avg, color="royalblue", label='Ni/Al')
    #axs[0].text(0.03, 0.05, 'More Oxic', weight='bold', transform=axs[2].transAxes)
    #axs[0].text(0.03, 0.90, 'Less Oxic', weight='bold', transform=axs[2].transAxes)
    #axs[0].set_ylabel('%Cu')
    #axs[1].set_ylim(0,0.03)
    axs[1].scatter(sample_depth, Cu_Al, color="navajowhite")
    axs[1].plot(sample_depth_avg, Cu_Al_avg, color="chocolate", label='Cu/Al')
    #axs[0].text(0.03, 0.05, 'More Oxic', weight='bold', transform=axs[3].transAxes)
    #axs[0].text(0.03, 0.90, 'Less Oxic', weight='bold', transform=axs[3].transAxes)
    #axs[0].set_ylabel('%Mo')
    #axs[1].set_ylim(0,0.02)
    axs[1].scatter(sample_depth, Mo_Al, color="powderblue")
    axs[1].plot(sample_depth_avg, Mo_Al_avg, color="steelblue", label='Mo/Al')
    #axs[0].text(0.03, 0.05, 'More Oxic', weight='bold', transform=axs[4].transAxes)
    #axs[0].text(0.03, 0.90, 'Less Oxic', weight='bold', transform=axs[4].transAxes)
    #axs[0].set_ylabel('%As')
    #axs[1].set_ylim(0,0.02)
    axs[1].scatter(sample_depth, Ars_Al, color="palegreen")
    axs[1].plot(sample_depth_avg, Ars_Al_avg, color="forestgreen", label='As/Al')
    #axs[0].text(0.03, 0.05, 'More Oxic', weight='bold', transform=axs[5].transAxes)
    #axs[0].text(0.03, 0.90, 'Less Oxic', weight='bold', transform=axs[5].transAxes)
    axs[1].legend()
    fig.suptitle(title + " RedOx sensitive elements")
    fig.tight_layout()
    fig.subplots_adjust(top=0.95) #Essentially removes huge gap from between title and plots
    plt.savefig(title + '_RedOx.pdf')
    plt.show()
    

#Plot all
    '''
    fig, axs = plt.subplots(12, figsize=(20,45), sharex=True) 
    plt.xticks(np.arange(top_depth, bot_depth+1, 5))
    plt.minorticks_on()
    axs[9].scatter(sample_depth, Si, color="khaki")
    axs[9].plot(sample_depth_avg, Si_avg, color="Goldenrod")
    axs[9].set_ylabel('Sand Content (%Si)')
    axs[9].set_xlim(top_depth, bot_depth)
    axs[10].scatter(sample_depth, Al, color="lightgreen")
    axs[10].plot(sample_depth_avg, Al_avg, color="forestgreen")
    axs[10].set_ylabel('Clay Content (%Al)')
    axs[11].scatter(sample_depth, Ca, color="lightsteelblue")
    axs[11].plot(sample_depth_avg, Ca_avg, color="royalblue")
    axs[11].set_ylabel('Carbonate content (%Ca)')
    axs[6].scatter(sample_depth, Si_Al)
    axs[6].plot(sample_depth_avg, Si_Al_avg)
    axs[6].text(0.01, 0.05, 'Finer', weight='bold', transform=axs[6].transAxes)
    axs[6].text(0.01, 0.90, 'Coarser', weight='bold', transform=axs[6].transAxes)
    axs[6].set_ylabel('Grain Size (Si/Al)')
    axs[7].scatter(sample_depth, K_Rb)
    axs[7].plot(sample_depth_avg, K_Rb_avg)
    axs[7].text(0.01, 0.05, 'Finer', weight='bold', transform=axs[7].transAxes)
    axs[7].text(0.01, 0.90, 'Coarser', weight='bold', transform=axs[7].transAxes)
    axs[7].set_ylabel('Grain Size (K/Rb)')
    axs[8].scatter(sample_depth, Zr_Rb)
    axs[8].plot(sample_depth_avg, Zr_Rb_avg)
    axs[8].text(0.01, 0.05, 'More Distal', weight='bold', transform=axs[8].transAxes)
    axs[8].text(0.01, 0.90, 'More Proximal', weight='bold', transform=axs[8].transAxes)
    axs[8].set_ylabel('Proximity proxy (Zr/Rb)')
    axs[0].set_ylabel('S/Al')
    axs[0].scatter(sample_depth, Sul_Al, color="lightcoral")
    axs[0].plot(sample_depth_avg, Sul_Al_avg, color="Firebrick")
    axs[0].text(0.01, 0.05, 'More Oxic', weight='bold', transform=axs[0].transAxes)
    axs[0].text(0.01, 0.90, 'Less Oxic', weight='bold', transform=axs[0].transAxes)
    axs[1].set_ylabel('Fe/Al')
    axs[1].scatter(sample_depth, Fe_Al, color="lightcoral")
    axs[1].plot(sample_depth_avg, Fe_Al_avg, color="Firebrick")
    axs[1].text(0.01, 0.05, 'More Oxic', weight='bold', transform=axs[1].transAxes)
    axs[1].text(0.01, 0.90, 'Less Oxic', weight='bold', transform=axs[1].transAxes)
    axs[2].set_ylabel('Ni/Al')
    axs[2].set_ylim(0,0.03)
    axs[2].scatter(sample_depth, Ni_Al, color="lightcoral")
    axs[2].plot(sample_depth_avg, Ni_Al_avg, color="Firebrick")
    axs[2].text(0.01, 0.05, 'More Oxic', weight='bold', transform=axs[2].transAxes)
    axs[2].text(0.01, 0.90, 'Less Oxic', weight='bold', transform=axs[2].transAxes)
    axs[3].set_ylabel('Cu/Al')
    axs[3].set_ylim(0,0.03)
    axs[3].scatter(sample_depth, Cu_Al, color="lightcoral")
    axs[3].plot(sample_depth_avg, Cu_Al_avg, color="Firebrick")
    axs[3].text(0.01, 0.05, 'More Oxic', weight='bold', transform=axs[3].transAxes)
    axs[3].text(0.01, 0.90, 'Less Oxic', weight='bold', transform=axs[3].transAxes)
    axs[4].set_ylabel('Mo/Al')
    axs[4].set_ylim(0,0.02)
    axs[4].scatter(sample_depth, Mo_Al, color="lightcoral")
    axs[4].plot(sample_depth_avg, Mo_Al_avg, color="Firebrick")
    axs[4].text(0.01, 0.05, 'More Oxic', weight='bold', transform=axs[4].transAxes)
    axs[4].text(0.01, 0.90, 'Less Oxic', weight='bold', transform=axs[4].transAxes)
    axs[5].set_ylabel('As/Al')
    axs[5].set_ylim(0,0.02)
    axs[5].scatter(sample_depth, Ars_Al, color="lightcoral")
    axs[5].plot(sample_depth_avg, Ars_Al_avg, color="Firebrick")
    axs[5].text(0.01, 0.05, 'More Oxic', weight='bold', transform=axs[5].transAxes)
    axs[5].text(0.01, 0.90, 'Less Oxic', weight='bold', transform=axs[5].transAxes)
    fig.suptitle(title + " pXRF Plots") 
    fig.tight_layout()
    fig.subplots_adjust(top=0.97) #Essentially removes huge gap from between title and plots
    plt.savefig(title + '_pXRF.pdf')
    plt.show()  
    '''


def d13c_plot(file, title, top_depth, bot_depth): #defining function to plot d13C data    
    """
    Summary
    -------
    Function to plot d13C data sent from the NIGL isotope labs
    
    Parameters
    ----------
    file = path to .csv containing the data
    title = title to save the file as, and to title the plot
    top_depth = top depth of the core section to be plotted
    bot_depth = bottom depth of the core sectoin to be plotted
    
    Returns
    -------
    title.pdf plotting all d13C
    """
    
    #Lists produced from columns in spreadsheet
    sample_depth = []
    d13c = []
    C_cont = []
    N_cont = []
    CN_ratio = []
    
    with open(file, mode='r') as csv_d13c_all:
        d13c_all = csv.reader(csv_d13c_all)
        next(csv_d13c_all)
        for row in d13c_all:
            sample_depth.append(float(row[0]))
            d13c.append(float(row[1]))
            C_cont.append(float(row[2]))
            N_cont.append(float(row[3]))
            CN_ratio.append(float(row[4]))
    
    fig, axs = plt.subplots(2, figsize=(22,8))
    axs[1].plot(sample_depth, d13c, marker='.', color='grey')
    axs[1].set_ylabel('d13C org')
    axs[1].set_xlim(top_depth, bot_depth)
    axs[1].set_ylim(-35, -25)
    axs[0].plot(sample_depth, C_cont, marker='o', color='black')
    axs[0].set_ylabel('%C')
    axs[0].set_xlim(top_depth, bot_depth)
    axs[0].set_ylim(0, 3)
    plt.xticks(np.arange(top_depth, bot_depth+1, 5))
    plt.minorticks_on()
    fig.suptitle(title + " isotope data") 
    fig.tight_layout()
    fig.subplots_adjust(top=0.93) #Essentially removes huge gap from between title and plots
    plt.savefig(title + '_c-isotopes.pdf')
    plt.show()    


