import numpy as np

s1 = np.array([168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,242, 331, 251, 323, 106, 1055, 170])
s2 = np.array([168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,242, 331, 251, 180, 106, 1055, 200])

dist_euclidiana = np.sqrt(((s1-s2)**2).sum())

media = (s1+s2)/2

max = np.fmax(s1,s2)

min = np.fmin(s1,s2)

print("Distância euclidiana: ", dist_euclidiana)
print("Vetor de valores médios: \n", media)
print("Vetor de valores máximos: \n", max)
print("Vetor de valores mínimos: \n", min)
