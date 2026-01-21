#PL-CMM

import tkinter
from tkinter import ttk
from tkinter import filedialog
import sv_ttk
import os
from datetime import datetime

def CMM(A,B):
    AD = str("\\")
    AE = str(">>>")
    X = os.listdir(A)
    I = C(A)
    os.makedirs(I)
    P = K(I)
    Q = str(".txt")
    R = B + Q
    S = P + R
    U = str("\n")
    with open(S,"x",encoding = "UTF-8") as T:
        T.write(R)
        T.write(U)
    V = 0
    for Y in X:
        V = V + 1
        Z = os.path.splitext(Y)[1]
        AA = str("_")
        AB = str(P) + str(B) + str(AA) + str(V) + str(Z)
        AC = str(A) + str(AD) + str(Y)
        with open(S,"a",encoding = "UTF-8") as AF:
            AF.write(AC)
            AF.write(AE)
            AF.write(AB)
            AF.write(U)
        os.rename(AC,AB)
    BQ = str("文件重命名完成")
    BR = AZ()
    AV.insert("end",BR + BQ)
    BF()
    AV.see("end")

def BE():
    AQ()
    BN = AZ()
    BO = str("前缀名称：")
    BP = AP[0]
    BM = AS[0]
    AV.insert("end",BN + BO + BM)
    BF()
    AV.see("end")
    CMM(BP,BM)

def BF():
    BG = "\n"
    AV.insert("end",BG)

def AQ():
    AR = AT.get()
    AS.clear()
    AS.append(AR)

def C(E):
    D = str("\\")
    J = str("Outputs")
    F = E + D + J
    return F

def K(L):
    M = str("\\")
    N = L + M
    return N

def AZ():
    BK = datetime.now()
    BA = BK.hour
    if BA < 10:
        BA = str("0") + str(BA)
    BH = BK.minute
    if BH < 10:
        BH = str("0") + str(BH)
    BI = BK.second
    if BI < 10:
        BI = str("0") + str(BI)
    BJ = str(":")
    BL = str(BA) + str(BJ) + str(BH) + str(BJ) + str(BI)
    BB = str("：")
    BC = str(BL) + str(BB)
    return BC

def AN():
    AM = filedialog.askdirectory()
    return AM

def AL():
    AO = AN()
    AP.clear()
    AP.append(AO)
    BH = "当前选择的目录为："
    BI = AZ()
    AV.insert("end",BI + BH + AO)
    BF()
    AV.see("end")

AP = []
AS = []

AH = tkinter.Tk()

AH.geometry("1200x700")
AH.resizable(width = False, height = False)
AH.title("PL-CMM_V-2.0.0")

sv_ttk.set_theme("light")

AK = ttk.Button(AH,text = "选择文件夹",command = AL)
AK.place(x = 125,y = 25)
BD = ttk.Button(AH,text = "开始",command = BE)
BD.place(x = 500,y = 600)

AT = ttk.Entry(AH,width = 20)
AT.place(x = 125,y = 77)

AU = ttk.Label(AH,text = "前缀名称：",font = ("",15))
AU.place(x = 25,y = 80)
AX = ttk.Label(AH,text = "文件路径：",font = ("",15))
AX.place(x = 25,y = 30)


AV = tkinter.Text(AH,width = 55,height = 33,font = ("",15))
AV.place(x = 600,y = 10)

AH.mainloop()