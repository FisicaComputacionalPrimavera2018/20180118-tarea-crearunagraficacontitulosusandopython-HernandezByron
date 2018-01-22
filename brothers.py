import matplotlib.pyplot as plt
plt.plot ([2,4,5,5,6,6,8,8,8,15,15,15,16,18,18,18,21,21,21,24,24,26])
plt.xlabel(['Anos de vida'])
plt.ylabel(['primos y hermanos por ano'])
plt.title ('Hermanos y primos x ano')
plt.savefig('temp.png')
plt.show()


