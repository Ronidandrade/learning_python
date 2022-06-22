import matplotlib.pyplot as plt;

fig, ax = plt.subplots();
circle = plt.Circle((0,0), 0.55, color='white');
lbls = ['Codar', 'Estudar', 'Comer', 'Dormir', 'Acordar', 'Banhar'];

ax.pie([7,4,2,8, 1, 0.1], labels = lbls, autopct = '%1.1f%%', pctdistance = 0.86);
ax.add_artist(circle);
ax.set_title('Horários', fontsize=16);
plt.savefig('times.png');
plt.show();
