from cli import get_filepath #we go into the CLI file and retrieve the get_filepath function
from analyzer import analyze_file

def main(): #we create the main function
    filepath = get_filepath()

    try:
        levels = analyze_file(filepath)
        if not levels:
            print("Aucun niveau trouvé dans le fichier")
        else:
            print("-----Résumé-----")
            for lvl, count in levels.items(): #value key pair
                print(f"{lvl}: {count}")

    except FileNotFoundError:
        print("Fichier introuvable")

if __name__=="__main__": #guard
    main()
