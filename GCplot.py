import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-01', Resource='Apple'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource='Grape'),
      dict(Task="Job C", Start='2009-04-20', Finish='2009-09-30', Resource='Banana')]

colors = ['#7a0504', (0.2, 0.7, 0.3), 'rgb(210, 60, 180)']

fig = ff.create_gantt(df, colors=colors, index_col='Resource', reverse_colors=True,
                      show_colorbar=True)
fig.show()