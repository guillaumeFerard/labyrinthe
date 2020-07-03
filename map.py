
def carte():
for i in range(len(carte)):
    ligne = ""
    for o in range(len(carte[0])):
        ligne = ligne + carte[i][o]
    print(ligne)
