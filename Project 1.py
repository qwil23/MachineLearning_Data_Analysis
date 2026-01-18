# Step 1: You are importing the essential Python libraries for data analysis (oandas, numpy) and visualization (matplotlib, seaborn).
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
print(sys.executable)

#set plot style for better aesthetics
sns.set(style="whitegrid")

# Step 2 Data Loading and Inital Inspection
import seaborn as sns
df = sns.load_dataset("tips")
print(df.head())