# Lascar's Tool do draw parametrical function, with sliders

import json
from math import *
import os
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg) 
from matplotlib import pyplot as plt
import tkinter as tk


root = tk.Tk()
root.title("LascaR's parametric equation plot")
root.iconbitmap('lascar.ico')
root.geometry('1300x1000')



nbfunction=10
entries={}
labels={}
rights={}
lefts={}
functions=[]
logs={}
xBounds=[0,1]
yBounds=[0,1]

def plot(e): 
    fig = Figure(figsize = (7, 7), 
                    dpi = 100) 
    
    plot=fig.add_subplot(111)
    plot.set_xlim(xBounds)
    plot.set_ylim(yBounds)
    
    ys={}
    for fn in range(nbfunction):

        tem=parameters.get()
        logs["param"]=tem
        zem=tem.split(',')
        
        fo=functions[fn].get()
        logs["f"+str(fn)]=fo
        if fo!="":
            for i in zem:
            
                fo=fo.replace('$'+i,str(entries[i].get()))
                logs[i]=[str(entries[i].get()),str(lefts[i].get()),str(rights[i].get())]

            
            ty=[]
            tx=[] 
            for i in range(1001):
                fo2=fo
                for fnr in range(fn):
                    if fnr in ys:
                        fo2=fo2.replace('$y'+str(fnr),str(ys[fnr][i]))
          
                x=xBounds[0]+(xBounds[1]-xBounds[0])*i/1000
                y=eval(fo2)
                ty.append(y)
                tx.append(x)

            ys[fn]=ty
             
            plot.plot(tx,ty)
    plot.grid(True)
 
    logs["xBounds"]=[str(xminEntry.get()),str(xmaxEntry.get())]
    logs["yBounds"]=[str(yminEntry.get()),str(ymaxEntry.get())]

    f=open("autosave","w")
    json.dump(logs,f,indent=2)
    f.close()


    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master = root)   
    canvas.draw() 
    canvas.get_tk_widget().place(x=10,y=260) 

def updateparam(e):
    t=parameters.get()
    z=t.split(',')

    vals={}
    rvals={}
    lvals={}
    for i in entries:
        vals[i]=entries[i].get()
        rvals[i]=rights[i].get()
        lvals[i]=lefts[i].get()
        labels[i].destroy()
        rights[i].destroy()
        lefts[i].destroy()
        entries[i].destroy()
    
    entries.clear()
    rights.clear()
    lefts.clear()
    labels.clear()
    count=0
    for i in z:
       
        labels[i]=tk.Label(root, text=i)
        labels[i].place(x=720,y=47+count*60)
        rights[i]=tk.Entry(root,name='right'+i,width=4)
        lefts[i]=tk.Entry(root,name='left'+i,width=4)
        if i in rvals:
            rights[i].insert(0,rvals[i])
        else:
            rights[i].insert(0,1)
            rvals[i]=1
        
        if i in lvals:
            lefts[i].insert(0,lvals[i])
        else:
            lefts[i].insert(0,0)
            lvals[i]=0

        

        from_=float(lefts[i].get())
        to=float(rights[i].get())
        tickinterval=(to-from_)/10
        resolution=(to-from_)/100

        entries[i]=tk.Scale(root, from_=from_, to=to,tickinterval=tickinterval,resolution=resolution, length=500,orient=tk.HORIZONTAL,command=plot)
        
        if i in vals:
            entries[i].set(vals[i])
        else:
            entries[i].set(0.5)
        entries[i].place(x=735,y=25+count*60)
        rights[i].place(x=1250,y=65+count*60)
        lefts[i].place(x=710,y=65+count*60) 
        rights[i].bind("<Return>", updateparamfield)
        lefts[i].bind("<Return>", updateparamfield)
        count+=1

def updateparamfield(e):
    updateparam(None)
    plot(None)

def zoom(d):
    global xBounds,yBounds

    cx=sum(xBounds)/2
    cy=sum(yBounds)/2
    dx=(xBounds[1]-cx)
    dy=(yBounds[1]-cy)
    xBounds=[cx-dx*pow(2,-d),cx+dx*pow(2,-d)]
    yBounds=[cy-dy*pow(2,-d),cy+dy*pow(2,-d)]


    xminEntry.delete(0,'end')
    xminEntry.insert(0,xBounds[0])
    xmaxEntry.delete(0,'end')
    xmaxEntry.insert(0,xBounds[1])
    yminEntry.delete(0,'end')
    yminEntry.insert(0,yBounds[0])
    ymaxEntry.delete(0,'end')
    ymaxEntry.insert(0,yBounds[1])
    plot(None)

def zoomIn():
    zoom(1)

def zoomOut():
    zoom(-1)

def modBounds(e):
    global xBounds,yBounds
    xBounds=[float(xminEntry.get()),float(xmaxEntry.get())]
    yBounds=[float(yminEntry.get()),float(ymaxEntry.get())]
    plot(None)


if os.path.exists("autosave"):
    f=open("autosave","r")
    logs=json.load(f)
    f.close()

for i in range(nbfunction):
    tk.Label(root, text="Function  y"+str(i)+"=").place(x=20,y=5+i*25)
    functions.append(tk.Entry(root,name='function'+str(i),width=70))
    functions[i].place(x=100,y=5+i*25)
    functions[i].bind("<Return>", plot)
    if "f"+str(i) in logs:
        functions[i].insert(0,logs["f"+str(i)])
    else:
        functions[i].insert(0,"$a*pow(x,"+str(i+1)+")+$b")

tk.Label(root, text="Parameters").place(x=700,y=5)
parameters=tk.Entry(root,name='parameters',width=70)
parameters.place(x=780,y=5)
parameters.bind("<Return>", updateparam)

if "param" in logs:
    parameters.insert(0,logs["param"])
else:
    parameters.insert(0,"a,b")


updateparam(None)
# print (logs)
for k,v in enumerate(entries):
    if v in logs:
        # print ('set ',v)

        lefts[v].delete(0,'end')
        lefts[v].insert(0,logs[v][1])
        rights[v].delete(0,'end')
        rights[v].insert(0,logs[v][2])
updateparam(None)
for k,v in enumerate(entries):
    if v in logs:
        entries[v].set(float(logs[v][0]))
    


if "xBounds" in logs:
    xBounds=[float(logs["xBounds"][0]),float(logs["xBounds"][1])]

if "yBounds" in logs:
    yBounds=[float(logs["yBounds"][0]),float(logs["yBounds"][1])]


butPlus=tk.Button(root,text="+",command=zoomIn,width=2,)
butPlus.place(x=600,y=150)
butMoins=tk.Button(root,text="-",command=zoomOut,width=2)
butMoins.place(x=600,y=175)

tk.Label(root, text="Xmin").place(x=558,y=155)
xminEntry=tk.Entry(root,name='xminEntry',width=6)
xminEntry.place(x=558,y=175)
xminEntry.bind("<Return>", modBounds,'xmin')
xminEntry.insert(0,xBounds[0])

tk.Label(root, text="Xmax").place(x=625,y=155)
xmaxEntry=tk.Entry(root,name='xmaxEntry',width=6)
xmaxEntry.place(x=625,y=175)
xmaxEntry.bind("<Return>", modBounds,'xmax')
xmaxEntry.insert(0,xBounds[1])

tk.Label(root, text="Ymin").place(x=565,y=205)
yminEntry=tk.Entry(root,name='yminEntry',width=6)
yminEntry.place(x=600,y=205)
yminEntry.bind("<Return>", modBounds,'ymin')
yminEntry.insert(0,yBounds[0])

tk.Label(root, text="Ymax").place(x=565,y=128)
ymaxEntry=tk.Entry(root,name='ymaxnEntry',width=6)
ymaxEntry.place(x=600,y=128)
ymaxEntry.bind("<Return>", modBounds,'ymax')
ymaxEntry.insert(0,yBounds[1])

root.mainloop() 
