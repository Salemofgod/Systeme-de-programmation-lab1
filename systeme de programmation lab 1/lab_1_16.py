import os
import sys

def copier_avec_progression(src: str, dst: str) -> None:
    try:
        taille = os.path.getsize(src)
    except FileNotFoundError:
        print(f"Erreur : le fichier '{src}' n'a pas été trouvé.")
        return
    except OSError as e:
        print(f"Erreur lors de l'accès au fichier : {e}")
        return

    try:
        with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
            copie = 0
            taille_mb = taille / (1024 * 1024)  # Convertir en MB
            
            print("Copie en cours...")
            
            while True:
                donnees = fsrc.read(4096)  # Lire par blocs de 4KB
                if not donnees:
                    break
                fdst.write(donnees)
                copie += len(donnees)
                
                # Afficher la progression
                pourcentage = (copie / taille) * 100
                copie_mb = copie / (1024 * 1024)
                sys.stdout.write(f"\rProgression: {pourcentage:.1f}% ({copie_mb:.1f} MB / {taille_mb:.1f} MB)")
                sys.stdout.flush()
            
            print(f"\nFichier copié avec succès vers '{dst}'")
            print(f"Taille totale : {taille_mb:.2f} MB")
            
    except OSError as e:
        print(f"Erreur lors de la copie : {e}")


if __name__ == "__main__":
    chemin_fichier = input("Entrez le chemin du fichier à copier : ").strip()

    print("\nTâche 16")

    if not os.path.exists(chemin_fichier):
        print("Erreur : Le fichier source n'existe pas.")
        exit(1)

    base, ext = os.path.splitext(chemin_fichier)  
    chemin_destination = f"{base}_copie{ext}" 

    copier_avec_progression(chemin_fichier, chemin_destination)