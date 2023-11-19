import cv2

#Lire une image en niveaux de gris
image = cv2.imread('test1.png', 0)

#Trouver le point blanc le plus haut à gauche
for j in range(image.shape[0]):
    for i in range(image.shape[1]):
        if image[j, i] == 255:
            x_high_left, y_high_left = i, j
            break
    else:
        continue
    break

#Trouver le point blanc le plus bas à droite
for j in range(image.shape[0]-1, -1, -1):
    for i in range(image.shape[1]-1, -1, -1):
        if image[j, i] == 255:
            x_low_right, y_low_right = i, j
            break
    else:
        continue
    break

image_colored = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

#Dessiner un cercle autour des points trouvés
radius = 1
color = (0, 0, 255)  # Rouge en BGR
thickness = 1  # épaisseur du cercle


cv2.circle(image_colored, (x_high_left, y_high_left), radius, color, thickness)
cv2.circle(image_colored, (x_low_right, y_low_right), radius, color, thickness)

#afficher les coordoonnees des 2 points
print('Le point blanc le plus haut à gauche a les coordonnées', x_high_left, y_high_left)
print('Le point blanc le plus bas à droite a les coordonnées', x_low_right, y_low_right)


#Afficher l'image modifiée
cv2.imshow('Image avec les points', image_colored)
cv2.waitKey(0)
cv2.destroyAllWindows()