```python
# Bokeh Libraries
import bokeh.io
from bokeh.plotting import figure, show

bokeh.io.reset_output()
bokeh.io.output_notebook()

import main
from pprint import pprint
from IPython.display import display, HTML

```


<div class="bk-root">
        <a href="https://bokeh.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
        <span id="1002">Loading BokehJS ...</span>
    </div>





    Congrats line 5 ran
    __name__ is  main
    


```python
#matches = main.load_folder('CIL_matches')
matches, regional = main.load_folder('Midwest Regional')

```


```python
pprint(regional[8122])
```

    {'climb_average': 2.7,
     'climbs': [3, 3, 3, 3, 3, 3, 3, 1, 4, 1],
     'shot_percentage': 0.36,
     'shots_high': [6, 5, 3, 2, 2, 5, 4, 3, 0, 4],
     'shots_in_regional': 34,
     'taxis': [True, True, True, True, True, True, True, True, True, True],
     'total_shots': [12, 9, 12, 9, 8, 11, 14, 7, 0, 13]}
    


```python
team_num = 8122
team = regional[team_num]
shots_high = team['shots_high']

# My x-y coordinate data
match_num = [i+1 for i in range(len(shots_high))] # -> [1,2,3,4...]


# Output the visualization directly in the notebook
# output_file('first_glyphs.html', title='First Glyphs')

# Create a figure with no toolbar and axis ranges of [0,3]
fig = figure(title='Shots made in each match',
             plot_height=300, plot_width=500,
             x_range=(0, max(match_num)+1), y_range=(-2, max(shots_high)+1),
             toolbar_location="right")

# shot_percent = [made/total/2 if total else 0 for made, total in zip(team['shots_high'], team['total_shots'])]
# Draw the coordinates as circles
fig.circle(x=match_num, y=shots_high,
           color='saddlebrown', size=20, alpha=0.75)


fig.square(x=match_num,y=team['climbs'],
          color= 'blue', size=20, alpha=0.75)

taxi = ['green' if taxi else 'red' for taxi in team['taxis']]
fig.plus(x=match_num, y=-2,
        color=taxi,  size=20, alpha=0.75)



html = f'''
<h1>{team_num}</h1><br><strong>
shots in regional: {team['shots_in_regional']}<br>
max shots in single match: {max(shots_high)}<br>
regional shot percentage: {team['shot_percentage']*100}%<br>
average climb level: {team['climb_average']}<br>
taxi percentage: {sum(team['taxis'])/len(team['taxis'])*100}%
</strong>'''

# Show plot|
display(HTML(html))
show(fig)
print(html)

```



<h1>8122</h1><br><strong>
shots in regional: 34<br>
max shots in single match: 6<br>
regional shot percentage: 36.0%<br>
average climb level: 2.7<br>
taxi percentage: 100.0%
</strong>




<div class="bk-root" id="036b325d-23d9-4a2f-92d5-583c7832aa40" data-root-id="5539"></div>





    
    <h1>8122</h1><br><strong>
    shots in regional: 34<br>
    max shots in single match: 6<br>
    regional shot percentage: 36.0%<br>
    average climb level: 2.7<br>
    taxi percentage: 100.0%
    </strong>
    


```python
tp = [[team, regional[team]['shot_percentage']] for team in regional]
tp.sort(reverse=True, key=lambda sort:sort[1])
pprint(tp[:10])
```

    [[48, 0.86],
     [2338, 0.84],
     [1732, 0.84],
     [3488, 0.81],
     [111, 0.77],
     [2451, 0.76],
     [112, 0.76],
     [3061, 0.71],
     [1781, 0.7],
     [2220, 0.69]]
    


```python
pprint(regional.items())
```

    dict_items([(4096, {'shots_high': [3, 0, 2, 4, 3, 13, 3, 1, 4, 14, 1], 'total_shots': [12, 0, 13, 10, 8, 21, 5, 3, 10, 17, 4], 'climbs': [1, 3, 3, 0, 3, 0, 3, 3, 3, 0, 0], 'taxis': [True, True, True, True, True, True, True, False, True, True, True], 'shots_in_regional': 48, 'shot_percentage': 0.47, 'climb_average': 1.7272727272727273}), (5125, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [6, 7, 2, 7, 6, 9, 9, 0, 0, 1], 'climbs': [2, 3, 2, 3, 0, 3, 3, 3, 2, 3], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 0, 'shot_percentage': 0.0, 'climb_average': 2.4}), (7560, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'climbs': [3, 2, 3, 3, 3, 3, 1, 0, 3, 0], 'taxis': [False, False, True, True, True, True, True, True, True, False], 'shots_in_regional': 0, 'shot_percentage': 0.0, 'climb_average': 2.1}), (2830, {'shots_high': [7, 4, 9, 9, 13, 0, 6, 9, 11, 3], 'total_shots': [10, 5, 11, 16, 17, 0, 10, 14, 16, 5], 'climbs': [3, 3, 3, 2, 3, 3, 3, 3, 3, 3], 'taxis': [True, False, True, True, True, True, True, True, True, True], 'shots_in_regional': 71, 'shot_percentage': 0.68, 'climb_average': 2.9}), (2062, {'shots_high': [0, 1, 4, 1, 5, 2, 6, 4, 6, 0], 'total_shots': [0, 8, 12, 3, 10, 5, 12, 7, 13, 1], 'climbs': [0, 3, 0, 3, 3, 3, 3, 1, 3, 3], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 29, 'shot_percentage': 0.41, 'climb_average': 2.2}), (4241, {'shots_high': [3, 0, 0, 1, 0, 1, 0, 1, 1, 0], 'total_shots': [3, 4, 2, 2, 0, 3, 1, 4, 4, 2], 'climbs': [4, 3, 0, 5, 3, 1, 4, 4, 3, 5], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 7, 'shot_percentage': 0.28, 'climb_average': 3.2}), (2451, {'shots_high': [3, 11, 8, 11, 9, 14, 15, 7, 16, 8, 16], 'total_shots': [10, 15, 10, 13, 9, 21, 18, 10, 21, 11, 17], 'climbs': [0, 0, 4, 0, 0, 0, 0, 4, 4, 4, 0], 'taxis': [True, True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 118, 'shot_percentage': 0.76, 'climb_average': 1.4545454545454546}), (3734, {'shots_high': [4, 2, 5, 5, 0, 1, 7, 4, 6, 4], 'total_shots': [9, 7, 10, 8, 0, 2, 12, 8, 16, 7], 'climbs': [2, 2, 0, 3, 1, 1, 2, 1, 0, 3], 'taxis': [True, True, True, True, False, False, True, True, True, True], 'shots_in_regional': 38, 'shot_percentage': 0.48, 'climb_average': 1.5}), (3352, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [3, 3, 2, 0, 0, 0, 3, 0, 2, 4], 'climbs': [0, 3, 3, 3, 3, 0, 3, 3, 3, 3], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 0, 'shot_percentage': 0.0, 'climb_average': 2.4}), (8096, {'shots_high': [0, 2, 1, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [0, 3, 1, 0, 0, 0, 1, 0, 0, 0], 'climbs': [3, 3, 3, 1, 2, 3, 3, 2, 0, 3], 'taxis': [True, True, True, True, True, True, False, True, True, True], 'shots_in_regional': 3, 'shot_percentage': 0.6, 'climb_average': 2.3}), (3488, {'shots_high': [6, 2, 3, 2, 5, 0, 6, 6, 7, 5], 'total_shots': [6, 4, 3, 6, 5, 3, 6, 6, 8, 5], 'climbs': [3, 3, 1, 3, 3, 3, 3, 3, 3, 3], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 42, 'shot_percentage': 0.81, 'climb_average': 2.8}), (2338, {'shots_high': [1, 10, 12, 9, 13, 12, 12, 12, 13, 4], 'total_shots': [4, 11, 14, 10, 16, 14, 15, 14, 13, 5], 'climbs': [5, 5, 5, 5, 5, 5, 4, 4, 5, 5], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 98, 'shot_percentage': 0.84, 'climb_average': 4.8}), (7460, {'shots_high': [6, 3, 6, 8, 5, 4, 6, 4, 1, 4, 6], 'total_shots': [12, 6, 8, 10, 6, 11, 7, 6, 3, 6, 7], 'climbs': [5, 3, 1, 0, 0, 2, 3, 3, 4, 3, 5], 'taxis': [True, True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 53, 'shot_percentage': 0.65, 'climb_average': 2.6363636363636362}), (4645, {'shots_high': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 'total_shots': [0, 3, 1, 3, 0, 2, 0, 3, 2, 2], 'climbs': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'taxis': [False, False, False, False, False, False, False, False, True, True], 'shots_in_regional': 1, 'shot_percentage': 0.06, 'climb_average': 0}), (677, {'shots_high': [3, 1, 0, 3, 5, 8, 2, 0, 0, 1], 'total_shots': [8, 7, 4, 3, 8, 9, 5, 0, 5, 5], 'climbs': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'taxis': [True, True, True, False, True, True, True, True, True, True], 'shots_in_regional': 23, 'shot_percentage': 0.43, 'climb_average': 0}), (3110, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 'climbs': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'taxis': [True, True, True, False, True, True, True, True, False, True], 'shots_in_regional': 0, 'shot_percentage': 0.0, 'climb_average': 0}), (8868, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [0, 0, 1, 1, 1, 1, 0, 0, 0, 4], 'climbs': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'taxis': [True, True, True, True, False, True, True, True, True, True], 'shots_in_regional': 0, 'shot_percentage': 0.0, 'climb_average': 0}), (2220, {'shots_high': [1, 4, 2, 4, 5, 3, 3, 6, 5], 'total_shots': [6, 6, 4, 5, 8, 4, 3, 6, 6], 'climbs': [3, 5, 4, 5, 4, 5, 3, 3, 5], 'taxis': [True, True, True, True, True, False, True, True, True], 'shots_in_regional': 33, 'shot_percentage': 0.69, 'climb_average': 4.111111111111111}), (5934, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [0, 6, 1, 0, 9, 3, 6, 0, 1], 'climbs': [5, 0, 5, 0, 3, 5, 1, 3, 3], 'taxis': [True, True, True, True, True, False, True, True, True], 'shots_in_regional': 0, 'shot_percentage': 0.0, 'climb_average': 2.7777777777777777}), (8880, {'shots_high': [1, 2, 1, 3, 0, 3, 1, 4, 2, 1], 'total_shots': [3, 5, 4, 6, 3, 5, 3, 5, 5, 4], 'climbs': [3, 3, 1, 3, 0, 2, 3, 3, 3, 3], 'taxis': [False, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 18, 'shot_percentage': 0.42, 'climb_average': 2.4}), (5553, {'shots_high': [1, 8, 0, 1, 5, 2, 0, 3, 5, 0], 'total_shots': [5, 8, 0, 3, 8, 3, 2, 5, 9, 3], 'climbs': [3, 2, 0, 4, 4, 3, 4, 4, 0, 1], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 25, 'shot_percentage': 0.54, 'climb_average': 2.5}), (4145, {'shots_high': [4, 1, 4, 9, 8, 3, 4, 4, 2, 1], 'total_shots': [5, 3, 11, 11, 8, 5, 8, 7, 4, 1], 'climbs': [1, 0, 0, 0, 5, 1, 3, 5, 5, 5], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 40, 'shot_percentage': 0.63, 'climb_average': 2.5}), (4787, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [5, 0, 4, 7, 7, 9, 0, 6, 0, 2], 'climbs': [3, 0, 0, 0, 3, 3, 1, 0, 3, 1], 'taxis': [True, True, False, True, False, True, True, True, True, True], 'shots_in_regional': 0, 'shot_percentage': 0.0, 'climb_average': 1.4}), (48, {'shots_high': [3, 8, 12, 7, 11, 6, 5, 14, 12, 7], 'total_shots': [5, 9, 13, 7, 11, 8, 9, 15, 14, 8], 'climbs': [1, 4, 4, 4, 5, 3, 4, 5, 1, 5], 'taxis': [True, False, True, True, True, True, True, True, True, True], 'shots_in_regional': 85, 'shot_percentage': 0.86, 'climb_average': 3.6}), (2358, {'shots_high': [5, 9, 6, 5, 4, 4, 1, 7, 4, 8], 'total_shots': [10, 10, 11, 8, 8, 6, 8, 11, 8, 10], 'climbs': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 53, 'shot_percentage': 0.59, 'climb_average': 5}), (8122, {'shots_high': [6, 5, 3, 2, 2, 5, 4, 3, 0, 4], 'total_shots': [12, 9, 12, 9, 8, 11, 14, 7, 0, 13], 'climbs': [3, 3, 3, 3, 3, 3, 3, 1, 4, 1], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 34, 'shot_percentage': 0.36, 'climb_average': 2.7}), (5822, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [11, 6, 6, 1, 0, 1, 8, 9, 0, 2], 'climbs': [5, 5, 5, 0, 0, 5, 0, 5, 5, 5], 'taxis': [False, True, True, False, True, True, True, True, True, True], 'shots_in_regional': 0, 'shot_percentage': 0.0, 'climb_average': 3.5}), (4292, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [1, 0, 5, 4, 2, 1, 2, 5, 0, 3], 'climbs': [0, 0, 3, 3, 0, 0, 0, 0, 0, 0], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 0, 'shot_percentage': 0.0, 'climb_average': 0.6}), (7237, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [0, 0, 6, 8, 0, 13, 4, 7, 0, 1], 'climbs': [0, 1, 4, 3, 0, 0, 0, 3, 3, 2], 'taxis': [False, False, True, True, False, True, True, True, False, True], 'shots_in_regional': 0, 'shot_percentage': 0.0, 'climb_average': 1.6}), (1732, {'shots_high': [17, 17, 16, 10, 15, 0, 7, 10, 15, 17], 'total_shots': [19, 20, 18, 12, 15, 2, 10, 13, 20, 18], 'climbs': [4, 0, 4, 3, 4, 3, 4, 4, 3, 1], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 124, 'shot_percentage': 0.84, 'climb_average': 3}), (3067, {'shots_high': [0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 'total_shots': [6, 8, 3, 2, 3, 10, 2, 6, 0, 3], 'climbs': [1, 0, 3, 0, 1, 3, 0, 3, 0, 3], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 2, 'shot_percentage': 0.05, 'climb_average': 1.4}), (1739, {'shots_high': [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 'total_shots': [14, 0, 7, 9, 1, 0, 4, 7, 8, 10, 0], 'climbs': [3, 3, 1, 1, 1, 3, 3, 1, 1, 0, 3], 'taxis': [True, True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 2, 'shot_percentage': 0.03, 'climb_average': 1.8181818181818181}), (5847, {'shots_high': [5, 3, 2, 6, 5, 2, 8, 12, 4, 5], 'total_shots': [7, 4, 5, 7, 5, 10, 10, 13, 7, 8], 'climbs': [5, 5, 0, 4, 4, 4, 5, 5, 3, 1], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 52, 'shot_percentage': 0.68, 'climb_average': 3.6}), (1625, {'shots_high': [9, 8, 3, 8, 7, 3, 7, 6, 3, 2], 'total_shots': [12, 10, 6, 12, 14, 9, 12, 11, 9, 3], 'climbs': [5, 4, 5, 4, 3, 4, 4, 4, 0, 0], 'taxis': [True, True, True, True, True, True, True, False, True, True], 'shots_in_regional': 56, 'shot_percentage': 0.57, 'climb_average': 3.3}), (8029, {'shots_high': [0, 2, 0, 0, 4, 0, 4, 3, 1], 'total_shots': [0, 8, 2, 1, 5, 0, 4, 9, 4], 'climbs': [4, 1, 3, 0, 0, 0, 3, 3, 3], 'taxis': [True, True, True, True, True, True, True, True, True], 'shots_in_regional': 14, 'shot_percentage': 0.42, 'climb_average': 1.8888888888888888}), (4702, {'shots_high': [0, 0, 0, 0, 0, 2, 0, 0, 0, 0], 'total_shots': [0, 0, 0, 1, 0, 2, 0, 0, 1, 0], 'climbs': [0, 0, 3, 0, 3, 0, 0, 0, 3, 3], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 2, 'shot_percentage': 0.5, 'climb_average': 1.2}), (8802, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 'climbs': [0, 3, 2, 3, 3, 0, 2, 1, 3, 0], 'taxis': [True, True, True, True, True, True, True, True, True, False], 'shots_in_regional': 0, 'shot_percentage': 0.0, 'climb_average': 1.7}), (101, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 'total_shots': [0, 0, 0, 0, 2, 0, 0, 0, 4, 0], 'climbs': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 1, 'shot_percentage': 0.17, 'climb_average': 0}), (2022, {'shots_high': [0, 2, 0, 5, 0, 0, 1, 4, 0, 0], 'total_shots': [0, 6, 0, 7, 0, 1, 1, 7, 0, 0], 'climbs': [5, 4, 0, 0, 5, 0, 0, 4, 0, 0], 'taxis': [True, False, True, True, False, True, True, True, True, False], 'shots_in_regional': 12, 'shot_percentage': 0.55, 'climb_average': 1.8}), (2151, {'shots_high': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'total_shots': [0, 1, 0, 0, 0, 0, 0, 0, 2, 0], 'climbs': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 0, 'shot_percentage': 0.0, 'climb_average': 0}), (6381, {'shots_high': [11, 6, 7, 5, 10, 9, 2, 5, 8, 6], 'total_shots': [12, 7, 12, 12, 15, 10, 6, 10, 13, 8], 'climbs': [3, 2, 0, 1, 3, 0, 3, 2, 3, 3], 'taxis': [True, True, False, True, True, True, True, True, True, True], 'shots_in_regional': 69, 'shot_percentage': 0.66, 'climb_average': 2}), (111, {'shots_high': [9, 17, 0, 17, 12, 4, 7, 13, 16, 19], 'total_shots': [12, 17, 0, 21, 14, 16, 15, 13, 18, 22], 'climbs': [0, 5, 1, 5, 5, 4, 5, 0, 5, 4], 'taxis': [True, True, False, True, True, True, True, True, True, True], 'shots_in_regional': 114, 'shot_percentage': 0.77, 'climb_average': 3.4}), (3695, {'shots_high': [3, 5, 4, 0, 10, 2, 4, 10, 7, 6], 'total_shots': [10, 8, 12, 8, 13, 9, 6, 11, 15, 12], 'climbs': [4, 4, 4, 1, 4, 4, 4, 4, 4, 3], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 51, 'shot_percentage': 0.49, 'climb_average': 3.6}), (112, {'shots_high': [12, 7, 11, 4, 7, 0, 13, 9, 15, 9], 'total_shots': [16, 10, 14, 8, 8, 0, 18, 10, 17, 14], 'climbs': [3, 4, 4, 3, 3, 4, 4, 4, 0, 4], 'taxis': [True, False, True, False, True, True, True, True, True, True], 'shots_in_regional': 87, 'shot_percentage': 0.76, 'climb_average': 3.3}), (1781, {'shots_high': [5, 6, 5, 5, 5, 9, 6, 5, 6, 8], 'total_shots': [5, 10, 8, 6, 6, 12, 8, 11, 9, 11], 'climbs': [5, 5, 5, 4, 4, 5, 1, 5, 5, 5], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 60, 'shot_percentage': 0.7, 'climb_average': 4.4}), (3061, {'shots_high': [5, 5, 0, 5, 10, 11, 9, 14, 8, 10], 'total_shots': [7, 10, 0, 11, 11, 12, 13, 17, 15, 12], 'climbs': [5, 5, 4, 3, 5, 5, 5, 5, 5, 4], 'taxis': [True, True, True, True, True, True, True, True, True, True], 'shots_in_regional': 77, 'shot_percentage': 0.71, 'climb_average': 4.6}), (6651, {'shots_high': [0, 0, 1, 2, 0, 3, 6, 6, 0, 3], 'total_shots': [0, 0, 3, 4, 4, 10, 7, 9, 0, 6], 'climbs': [1, 1, 1, 1, 0, 0, 2, 0, 0, 1], 'taxis': [False, True, True, True, False, True, True, True, False, False], 'shots_in_regional': 21, 'shot_percentage': 0.49, 'climb_average': 0.7})])
    


```python

```
