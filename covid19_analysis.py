# Data analysis and manipulation
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
import pandas as pd

# Data visualization
import matplotlib.pyplot as plt

# Importing plotly
import plotly.offline as py
# py.init_notebook_mode(connected = True)

# Initializing plotly
# pio.renderers.default = 'colab'
pio.renderers.default = 'browser'

# Importing Dataset 1
dataset1 = pd.read_csv("covid.csv")
#print (dataset1.head()) #returns first 5 rows

# returns tuple of shape (Rows, columns)
#print(dataset1.shape)

# returns size of dataframe
#print(dataset1.size)

# returns concise info about the dataframe
#print(dataset1.info())

dataset2 = pd.read_csv("covid_grouped.csv")

dataset3 = pd.read_csv("coviddeath.csv")

