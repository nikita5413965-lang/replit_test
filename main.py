# Вариант 6
Cv = 100000
Tv = 15

# Контейнер расчета
from sympy import symbols

k, T, C, L = symbols('k T C L')

# 1 способ
C_ost = Cv
Am_lst = []
C_ost_lst = []

for i in range(Tv):
  Am = (C - L) / T
  C_ost -= Am.subs({C: Cv, T: Tv, L: 0})
  Am_lst.append(round(Am.subs({C: Cv, T: Tv, L: 0}), 2))
  C_ost_lst.append(round(C_ost, 2))

print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

# 2 способ
Aj = 0
C_ost = Cv
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(Tv):
  Am = k * 1 / T * (C - Aj)
  C_ost -= Am.subs({C: Cv, T: Tv, k: 2})
  Am_lst_2.append(round(Am.subs({C: Cv, T: Tv, k: 2}), 2))
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2))

print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

# Контейнер табличного выводы
import pandas as pd

Y = range(1, Tv + 1)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tfame)
print(tfame2)

# Контейнер визуализации
from matplotlib import pyplot as plt

plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am_2')

vals = Am_lst_2
labels = list(range(1, Tv + 1))
explode = [0.1 for i in range(Tv)]
fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       autopct='%1.1f%%',
       explode=explode,
       shadow=True,
       rotatelabels=True,
       wedgeprops={
           'edgecolor': 'k',
           'lw': 1,
           'ls': '--'
       })
ax.axis("equal")
plt.show()

# Гистограмма
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y','Am_lst_2'])

plt.bar(tfame['Y'], tfame['Am_lst'])
plt.show()

plt.bar(tfame2['Y'], tfame2['Am_lst_2'])
plt.show()


