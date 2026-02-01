import kagglehub
import pandas as pd 
import seaborn as sns 
from os import path


# Download latest version
path = kagglehub.dataset_download("adarsh2626/old-art-style-images-with-captions-dataset")

print("Path to dataset files:", path)

