from cli import get_filepath #on va dans le fichier cli et on recup la fct get_filepath
from analyzer import analyze_file

def main(): #on crée la fcton main
    filepath = get_filepath()

    try:
        levels = analyze_file(filepath)
        print("-----Résumé-----")
        for lvl, count in levels.items(): #paire clé valeur
            print(f"{lvl}: {count}")

    except FileNotFoundError:
        print("Fichier introuvable")

if __name__=="__main__":
    main()
