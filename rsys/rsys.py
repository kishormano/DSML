import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("/content/anime.csv")

#data.head()

df = data.dropna()

df['description'] = df['name']+ ' '+df['genre']+ ' '+df['type']+ ' '+df['episodes'].astype(str)+ ' '+df['rating'].astype(str)+ ' '+df['members'].astype(str)