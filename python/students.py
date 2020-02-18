import csv
import json

if __name__ == "__main__":

    filename = 'students.csv'
    file=open(filename,"r")
    file_csv=csv.reader(file)
    tab=[]
    for row in file_csv:
        tab.append(row)
    # Ecrivez une fonction permettant de récupérer toutes les lignes
    # du fichier CSV dans une list() `data`
    rows = tab 
    print(f'\nLe fichier brut contient {len(rows)} lignes')

    # Les étudiants ont chacun un diplôme qui leur est attribué
    # La variable `degrees` contient la liste des diplômes
    tab2=[]
    for i in range(len(rows)):
        tab2.append(rows[i][4])
    
    tab3=list(set(tab2))
    
    degrees = tab3
    print(f'\nLe fichier contient {len(degrees)} diplômes uniques')

    # Donnez, dans un dict, pour chaque diplôme le nombre d'étudiant
    # par catégorie d'utilisateur (student, alumni, ...)
    
    dict= {}
    for degree in range(len(degrees)):
        c=0
        for i in range(len(rows)):
            if rows[i][4]==degrees[degree]:
                c=c+1
        dict[degrees[degree]] = c
    users_per_degree = dict# TODO
    print(f'\nLa répartition des diplômes est la suivante :')
    for degree in users_per_degree.keys():
        print(f' - {degree}, {users_per_degree[degree]} étudiants')


    # Enregistrez le dictionnaire dans un nouveau fichier `degree_count.json`
    
    with open('degree_count.json', 'w') as fp:
        json.dump(dict, fp)
    print(f'\nFichier `degree_count.json` enregistré !')
