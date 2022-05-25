import plotly_express as pe
import pandas as pd
df = pd.read_csv('Student Marks vs Days Present.csv')
mean = df.groupby(['Marks In Percentage', 'Roll No'], as_index = False)['Days Present'].mean()
fig = pe.scatter(mean, x = 'Roll No', y = 'Days Present', color = 'Marks In Percentage', size = 'Marks In Percentage')
fig.show()