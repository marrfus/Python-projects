from skimage import io, color
from skimage.filters import gaussian
import matplotlib.pyplot as plt
from os import path

#Pfade Einrichtung
current_dir = path.dirname(path.abspath(__file__))
filename = path.join(current_dir,"schnecke.jpg")

fig, ax  = plt.subplots(1,3, figsize=(12,5))

#image laden
image = io.imread(filename)

#Schritt 1. image Vorverabeitung
if image.ndim == 3:
    image = color.rgb2gray(image)

#Schritt 2. Image Glätterung
#reduziert Rauschen und macht die Bildverarbeitung robuster  
image_smooth = gaussian(image, sigma=1.0)

#Schritt 3 Höher Kontrast setzen

# Kantendetektion (Canny)
from skimage.feature import canny

edges = canny(
    image_smooth,
    sigma=1.5,
    low_threshold=0.1,
    high_threshold=0.3,
    use_quantiles=True
)

# Segmentierung (Chan_Vese)
from skimage.segmentation import chan_vese

segmentation = chan_vese(
    image_smooth,
    mu=0.4,
    lambda1=1.0,
    lambda2=1.0,
    init_level_set="checkerboard",
    max_num_iter=100
)

# Feature-Extraktion : Erzeuge numerische Features für ML
import numpy as np

features = {
    "edge_density":edges.mean(), # kantig
    "segmant_area":segmentation.sum(), # Größe
    "mean_intensity_segment":image[segmentation].mean(),# Material
    "std_intensity_segment":image[segmentation].std()#Texturehinweise
}
X = np.array(list(features.values()))
print(X)

# Vorbereitung für sklearn
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X.reshape(1,-1))


#io.imshow(image)
ax[0].imshow(image, cmap="gray")
ax[0].set_title("Original")

ax[1].imshow(edges, cmap="gray")
ax[1].set_title("Canny")

ax[2].imshow(segmentation, cmap="gray")
ax[2].contour(segmentation, color="r")
ax[2].set_title("Chan_Vese")

plt.show()

