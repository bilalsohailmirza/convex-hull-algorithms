import plotly.graph_objects as go
import pandas as pd
import os


def Plot(Paths):

    fig = go.Figure()

    for path in Paths:
        data_frame = pd.read_csv('../CSVs/' + path, sep=',')
        data_frame_sorted = data_frame.sort_values(by='Size')

        fig.add_trace(
            go.Scatter(
                x=data_frame_sorted['Size'],
                y=data_frame_sorted['Time'],
                name = path[0:11]     
            ))

    fig.update_layout(title = 'Coparison Between all Convex Hull algorithms', xaxis_title='Trial',yaxis_title='Time(seconds)')

    fig.show()

if __name__ == '__main__':

    Paths = [
        'GrahamScan.csv', 'JarvisMarch.csv', 'PointElimination.csv', 'QuickHull.csv'
    ]
    Plot(['BruteForce.csv'])
    Plot(Paths)