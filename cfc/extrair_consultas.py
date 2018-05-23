qtde = 1

file = open('cfquery','r',encoding='ISO-8859-1')
text = file.read()
file.close()
text = text.split("\n\n")
print(len(text))
for t in text:
	file = open("consultas_cfc/"+str(qtde),"w")
	file.write(t)
	file.close()
	qtde = qtde + 1

print("Quatidade="+str(qtde-1))
