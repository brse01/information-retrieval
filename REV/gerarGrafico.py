from ManipulateFile import ManipulateFile
import matplotlib.pyplot as plt

'''
com stemmer
c2 = p2
sem stemmer
c = p
'''
#sem stemmer
c1 = ManipulateFile().read_file('c')
p1 = ManipulateFile().read_file('p')

#com stemmer
c2 = ManipulateFile().read_file('c2')
p2 = ManipulateFile().read_file('p2')

#"Cobertura","Precisão","Precisão Média")
#plt.plot(c1,p1,'-','g')
plt.plot(c1, p1, linestyle='-', color='red', label=u"sem stemmer")
#plt.plot(c2,p2,'--','b')
plt.plot(c2, p2, linestyle='-', color='blue', label=u"com stemmer")
plt.legend(loc='upper right')
plt.ylabel("Precisão")
plt.xlabel("Cobertura")
plt.title("Precisão Média")
plt.savefig('comparativo.png')
plt.show()


