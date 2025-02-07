import os
from PIL import Image
import time

# Chemin du dossier contenant les images
image_dir = os.getcwd()  # Utilise le répertoire courant

# Créer un dossier de sortie avec un nom basé sur le timestamp
timestamp = time.strftime("%Y%m%d%H%M%S")
output_dir = f"rescaled-{timestamp}"
os.makedirs(output_dir, exist_ok=True)

new_scale = 0.05 # 5% de l'original

# Parcourir toutes les images PNG dans le répertoire
for filename in os.listdir(image_dir):
    if filename.endswith(".png"):
        file_path = os.path.join(image_dir, filename)
        # Ouvrir l'image
        with Image.open(file_path) as img:
            width, height = img.size
            new_size = (int(width * new_scale), int(height * new_scale))
            
            # Redimensionner l'image en utilisant l'interpolation nearest neighbor
            img_resized = img.resize(new_size, Image.NEAREST)
            
            # Sauvegarder l'image redimensionnée dans le nouveau dossier
            img_resized.save(os.path.join(output_dir, filename))
            print(f"Redimensionné : {filename}")

print(f"Tous les fichiers ont été redimensionnés et sauvegardés dans le dossier '{output_dir}'.")
