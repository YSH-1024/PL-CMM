#批量重命名文件

import os

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
        print("文件重命名完成")
        input("输入Enter键关闭程序")

def C(E):
    D = str("\\")
    J = str("Outputs")
    F = E + D + J
    return F

def K(L):
    M = str("\\")
    N = L + M
    return N

G = input("输入文件路径：")
H = input("输入前缀名：")
CMM(G,H)