qtde = 1
for i in range(74,80):
	file = open('cf'+str(i),'r',encoding='ISO-8859-1')
	text = file.read()
	file.close()
	text = text.split("\n\n")
	print(len(text))
	for t in text:
		file = open("arquivos/"+str(qtde),"w")
		file.write(t)
		file.close()
		qtde = qtde + 1

print("Quatidade="+str(qtde-1))
