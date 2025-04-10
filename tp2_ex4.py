import matplotlib.pyplot as plt


labels = ['Modernes', 'Traditionelle', 'Rudimentaires']
data_1989 = [81.72, 260.64, 17.64]
data_1999 = [138.6, 217.08, 4.32]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))


ax1.pie(data_1989, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.set_title('Logements en 1989')

ax2.pie(data_1999, labels=labels, autopct='%1.1f%%', startangle=90)
ax2.set_title('Logements en 1999')

plt.tight_layout()
plt.show()