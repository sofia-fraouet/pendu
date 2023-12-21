import pygame
import random
import sys

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600
couleur_fond = (255, 255, 255)
couleur_texte = (0, 0, 0)
police = pygame.font.Font(None, 36)

def choisir_mot():
    with open("mots.txt", "r", encoding="utf-8") as fichier:
        mots = fichier.readlines()
    return random.choice(mots).strip()

def afficher_mot_cache(mot, lettres_trouvees):
    mot_affiche = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_affiche += lettre
        else:
            mot_affiche += "_"
    return mot_affiche

def jouer():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = set()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    lettre = event.unicode.lower()
                    lettres_trouvees.add(lettre)

        background = pygame.image.load("imagependu/fondecran.jpg")
        background = pygame.transform.smoothscale(background, fenetre.get_size())

        fenetre.blit(background, (0,0))
        pygame.display.flip()

        mot_affiche = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
        texte_mot = police.render(mot_affiche, True, couleur_texte)
        fenetre.blit(texte_mot, (200, 300))

        pygame.display.flip()

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu de devinette de mot")

# Positions et dimensions des boutons
bouton_jouer = pygame.Rect(200, 300, 200, 50)
bouton_inserer = pygame.Rect(200, 400, 200, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                x, y = event.pos
                if bouton_jouer.collidepoint(x, y):
                    jouer()
                elif bouton_inserer.collidepoint(x, y):
                    # Code pour insérer un mot dans le fichier mots.txt
                    pass
                
                
    


    # Affichage des boutons
    pygame.draw.rect(fenetre, couleur_texte, bouton_jouer)
    pygame.draw.rect(fenetre, couleur_texte, bouton_inserer)

    texte_jouer = police.render("Jouer", True, couleur_fond)
    texte_inserer = police.render("Insérer un mot", True, couleur_fond)

    fenetre.blit(texte_jouer, (bouton_jouer.x + 50, bouton_jouer.y + 15))
    fenetre.blit(texte_inserer, (bouton_inserer.x + 10, bouton_inserer.y + 15))

    pygame.display.flip()








nombre_max_erreurs = 6
erreurs_actuelles = 0




def afficher_pendu(erreurs):
   
   if erreurs >= 1:
    if erreurs >= 2:
        
   
        pygame.display.flip()

def lettre_correcte(lettre, mot_secret):
    

    while True:
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not lettre_correcte(lettre_choisie, mot_secret):
                erreurs_actuelles += 1


afficher_pendu(erreurs_actuelles)

while True:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 800, 600

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Affichage d'une image")

# Chargement de l'image
image = pygame.image.load("imagependu/pendu8.jpg")
image = pygame.image.load("imagependu/pendu9.jpg")
image = pygame.image.load("imagependu/pendu11.jpg")
image = pygame.image.load("imagependu/pendu13.jpg")
  # Remplacez le chemin par le chemin de votre image

# Position de l'image sur l'écran
position_image = (100, 100)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    fenetre.fill((255, 255, 255))  # Fond blanc

    # Afficher l'image à la position spécifiée
    fenetre.blit(image, position_image)

    # Rafraîchir l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
