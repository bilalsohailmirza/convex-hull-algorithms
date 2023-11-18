import plotly.graph_objects as go
import pandas as pd
import os



data_frame = pd.read_csv('BruteForce.csv', sep=',')



data_frame_sorted = data_frame.sort_values(by='Size')



fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=data_frame_sorted['Size'],
        y=data_frame_sorted['Time'],
        name = ''     
    ))

fig.update_layout(title = 'Coparison Between all sorting algorithms', xaxis_title='Trial',yaxis_title='Time(seconds)')

fig.show()