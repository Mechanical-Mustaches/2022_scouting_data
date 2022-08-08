```python
# Bokeh Libraries
import bokeh.io
from bokeh.plotting import figure, show

bokeh.io.reset_output()
bokeh.io.output_notebook()

import main
from pprint import pprint
```


<div class="bk-root">
        <a href="https://bokeh.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
        <span id="1002">Loading BokehJS ...</span>
    </div>





    Congrats line 5 ran
    __name__ is  main
    


```python
#matches = main.load_folder('CIL_matches')
matches = main.load_folder('Midwest Regional')
```

    match-2022ilch-1-111.json
    match-2022ilch-1-2830.json
    match-2022ilch-1-3734.json
    match-2022ilch-1-7460.json
    match-2022ilch-1-8802.json
    match-2022ilch-1-8880.json
    match-2022ilch-10-2062.json
    match-2022ilch-10-2451.json
    match-2022ilch-10-2830.json
    match-2022ilch-10-4241.json
    match-2022ilch-10-5553.json
    match-2022ilch-10-6651.json
    match-2022ilch-11-111.json
    match-2022ilch-11-3695.json
    match-2022ilch-11-5822.json
    match-2022ilch-11-8122.json
    match-2022ilch-11-8880.json
    match-2022ilch-12-1739.json
    match-2022ilch-12-1781.json
    match-2022ilch-12-4292.json
    match-2022ilch-12-7237.json
    match-2022ilch-12-8802.json
    match-2022ilch-13-112.json
    match-2022ilch-13-3067.json
    match-2022ilch-13-3352.json
    match-2022ilch-13-4096.json
    match-2022ilch-13-4787.json
    match-2022ilch-14-2338.json
    match-2022ilch-14-3734.json
    match-2022ilch-14-4645.json
    match-2022ilch-14-677.json
    match-2022ilch-14-7560.json
    match-2022ilch-14-8096.json
    match-2022ilch-15-1625.json
    match-2022ilch-15-3110.json
    match-2022ilch-15-3488.json
    match-2022ilch-15-4145.json
    match-2022ilch-15-4702.json
    match-2022ilch-15-5125.json
    match-2022ilch-16-1732.json
    match-2022ilch-16-2062.json
    match-2022ilch-16-2151.json
    match-2022ilch-16-2358.json
    match-2022ilch-16-48.json
    match-2022ilch-16-6651.json
    match-2022ilch-17-1739.json
    match-2022ilch-17-2451.json
    match-2022ilch-17-3695.json
    match-2022ilch-17-5553.json
    match-2022ilch-17-5822.json
    match-2022ilch-17-5847.json
    match-2022ilch-18-3061.json
    match-2022ilch-18-4096.json
    match-2022ilch-18-4241.json
    match-2022ilch-18-6381.json
    match-2022ilch-18-7460.json
    match-2022ilch-18-8880.json
    match-2022ilch-19-2338.json
    match-2022ilch-19-2830.json
    match-2022ilch-19-3067.json
    match-2022ilch-19-7237.json
    match-2022ilch-19-8122.json
    match-2022ilch-19-8868.json
    match-2022ilch-2-101.json
    match-2022ilch-2-112.json
    match-2022ilch-2-2451.json
    match-2022ilch-2-4241.json
    match-2022ilch-2-8029.json
    match-2022ilch-2-8868.json
    match-2022ilch-20-3110.json
    match-2022ilch-20-3352.json
    match-2022ilch-20-677.json
    match-2022ilch-20-7560.json
    match-2022ilch-20-8029.json
    match-2022ilch-20-8802.json
    match-2022ilch-21-111.json
    match-2022ilch-21-2022.json
    match-2022ilch-21-4292.json
    match-2022ilch-21-4787.json
    match-2022ilch-21-48.json
    match-2022ilch-21-5125.json
    match-2022ilch-22-101.json
    match-2022ilch-22-2151.json
    match-2022ilch-22-2220.json
    match-2022ilch-22-4645.json
    match-2022ilch-22-4702.json
    match-2022ilch-22-8096.json
    match-2022ilch-23-112.json
    match-2022ilch-23-1625.json
    match-2022ilch-23-2358.json
    match-2022ilch-23-3734.json
    match-2022ilch-23-4145.json
    match-2022ilch-23-5934.json
    match-2022ilch-24-1732.json
    match-2022ilch-24-1781.json
    match-2022ilch-24-3067.json
    match-2022ilch-24-3488.json
    match-2022ilch-24-4241.json
    match-2022ilch-24-5822.json
    match-2022ilch-25-2338.json
    match-2022ilch-25-3110.json
    match-2022ilch-25-3695.json
    match-2022ilch-25-4096.json
    match-2022ilch-25-6651.json
    match-2022ilch-25-8122.json
    match-2022ilch-26-2062.json
    match-2022ilch-26-4292.json
    match-2022ilch-26-677.json
    match-2022ilch-26-7237.json
    match-2022ilch-26-8029.json
    match-2022ilch-26-8880.json
    match-2022ilch-27-101.json
    match-2022ilch-27-111.json
    match-2022ilch-27-2151.json
    match-2022ilch-27-3061.json
    match-2022ilch-27-3352.json
    match-2022ilch-27-8868.json
    match-2022ilch-28-112.json
    match-2022ilch-28-2022.json
    match-2022ilch-28-4145.json
    match-2022ilch-28-4702.json
    match-2022ilch-28-4787.json
    match-2022ilch-28-8802.json
    match-2022ilch-29-1732.json
    match-2022ilch-29-1739.json
    match-2022ilch-29-3734.json
    match-2022ilch-29-5125.json
    match-2022ilch-29-5847.json
    match-2022ilch-29-8096.json
    match-2022ilch-3-1781.json
    match-2022ilch-3-2022.json
    match-2022ilch-3-2220.json
    match-2022ilch-3-3061.json
    match-2022ilch-3-5847.json
    match-2022ilch-3-6651.json
    match-2022ilch-30-1625.json
    match-2022ilch-30-1781.json
    match-2022ilch-30-2451.json
    match-2022ilch-30-48.json
    match-2022ilch-30-6381.json
    match-2022ilch-30-7560.json
    match-2022ilch-31-2220.json
    match-2022ilch-31-3488.json
    match-2022ilch-31-4645.json
    match-2022ilch-31-5553.json
    match-2022ilch-31-5934.json
    match-2022ilch-31-7460.json
    match-2022ilch-32-101.json
    match-2022ilch-32-2358.json
    match-2022ilch-32-2830.json
    match-2022ilch-32-3352.json
    match-2022ilch-32-4096.json
    match-2022ilch-32-4292.json
    match-2022ilch-33-2338.json
    match-2022ilch-33-3061.json
    match-2022ilch-33-4241.json
    match-2022ilch-33-4702.json
    match-2022ilch-33-5822.json
    match-2022ilch-33-8802.json
    match-2022ilch-34-111.json
    match-2022ilch-34-1739.json
    match-2022ilch-34-2062.json
    match-2022ilch-34-3067.json
    match-2022ilch-34-4145.json
    match-2022ilch-34-8868.json
    match-2022ilch-35-1732.json
    match-2022ilch-35-1781.json
    match-2022ilch-35-2022.json
    match-2022ilch-35-2451.json
    match-2022ilch-35-8096.json
    match-2022ilch-35-8880.json
    match-2022ilch-36-4645.json
    match-2022ilch-36-4787.json
    match-2022ilch-36-5125.json
    match-2022ilch-36-6651.json
    match-2022ilch-36-7460.json
    match-2022ilch-36-7560.json
    match-2022ilch-37-2151.json
    match-2022ilch-37-3110.json
    match-2022ilch-37-5553.json
    match-2022ilch-37-5934.json
    match-2022ilch-37-6381.json
    match-2022ilch-37-8122.json
    match-2022ilch-38-1625.json
    match-2022ilch-38-2220.json
    match-2022ilch-38-2830.json
    match-2022ilch-38-3695.json
    match-2022ilch-38-3734.json
    match-2022ilch-38-8029.json
    match-2022ilch-39-112.json
    match-2022ilch-39-2358.json
    match-2022ilch-39-48.json
    match-2022ilch-39-5847.json
    match-2022ilch-39-677.json
    match-2022ilch-39-7237.json
    match-2022ilch-4-2062.json
    match-2022ilch-4-3488.json
    match-2022ilch-4-3695.json
    match-2022ilch-4-4645.json
    match-2022ilch-4-6381.json
    match-2022ilch-4-7237.json
    match-2022ilch-40-111.json
    match-2022ilch-40-2022.json
    match-2022ilch-40-3488.json
    match-2022ilch-40-4096.json
    match-2022ilch-40-8096.json
    match-2022ilch-40-8802.json
    match-2022ilch-41-1739.json
    match-2022ilch-41-2451.json
    match-2022ilch-41-4645.json
    match-2022ilch-41-4702.json
    match-2022ilch-41-6651.json
    match-2022ilch-41-8880.json
    match-2022ilch-42-1781.json
    match-2022ilch-42-2062.json
    match-2022ilch-42-2338.json
    match-2022ilch-42-3061.json
    match-2022ilch-42-4787.json
    match-2022ilch-42-5934.json
    match-2022ilch-43-2220.json
    match-2022ilch-43-3110.json
    match-2022ilch-43-3734.json
    match-2022ilch-43-5822.json
    match-2022ilch-43-6381.json
    match-2022ilch-43-8868.json
    match-2022ilch-44-1625.json
    match-2022ilch-44-2830.json
    match-2022ilch-44-3352.json
    match-2022ilch-44-4241.json
    match-2022ilch-44-5125.json
    match-2022ilch-44-7237.json
    match-2022ilch-45-112.json
    match-2022ilch-45-1732.json
    match-2022ilch-45-4292.json
    match-2022ilch-45-5553.json
    match-2022ilch-45-7560.json
    match-2022ilch-45-8122.json
    match-2022ilch-46-101.json
    match-2022ilch-46-3067.json
    match-2022ilch-46-3695.json
    match-2022ilch-46-48.json
    match-2022ilch-46-677.json
    match-2022ilch-46-7460.json
    match-2022ilch-47-2151.json
    match-2022ilch-47-2358.json
    match-2022ilch-47-3488.json
    match-2022ilch-47-4145.json
    match-2022ilch-47-5847.json
    match-2022ilch-47-8029.json
    match-2022ilch-48-2062.json
    match-2022ilch-48-4096.json
    match-2022ilch-48-5822.json
    match-2022ilch-48-5934.json
    match-2022ilch-48-8868.json
    match-2022ilch-48-8880.json
    match-2022ilch-49-111.json
    match-2022ilch-49-2022.json
    match-2022ilch-49-3110.json
    match-2022ilch-49-4241.json
    match-2022ilch-49-4645.json
    match-2022ilch-49-7237.json
    match-2022ilch-5-2338.json
    match-2022ilch-5-3352.json
    match-2022ilch-5-4145.json
    match-2022ilch-5-48.json
    match-2022ilch-5-5553.json
    match-2022ilch-5-5822.json
    match-2022ilch-50-112.json
    match-2022ilch-50-1739.json
    match-2022ilch-50-3352.json
    match-2022ilch-50-6381.json
    match-2022ilch-50-6651.json
    match-2022ilch-50-7560.json
    match-2022ilch-51-1732.json
    match-2022ilch-51-2220.json
    match-2022ilch-51-2830.json
    match-2022ilch-51-3695.json
    match-2022ilch-51-5125.json
    match-2022ilch-51-8802.json
    match-2022ilch-52-2151.json
    match-2022ilch-52-4787.json
    match-2022ilch-52-48.json
    match-2022ilch-52-7460.json
    match-2022ilch-52-8029.json
    match-2022ilch-52-8096.json
    match-2022ilch-53-101.json
    match-2022ilch-53-1625.json
    match-2022ilch-53-1781.json
    match-2022ilch-53-4145.json
    match-2022ilch-53-677.json
    match-2022ilch-53-8122.json
    match-2022ilch-54-2338.json
    match-2022ilch-54-3067.json
    match-2022ilch-54-4292.json
    match-2022ilch-54-4702.json
    match-2022ilch-54-5553.json
    match-2022ilch-54-5847.json
    match-2022ilch-55-2358.json
    match-2022ilch-55-2451.json
    match-2022ilch-55-3061.json
    match-2022ilch-55-3488.json
    match-2022ilch-55-3734.json
    match-2022ilch-55-7237.json
    match-2022ilch-56-2022.json
    match-2022ilch-56-2830.json
    match-2022ilch-56-5822.json
    match-2022ilch-56-5934.json
    match-2022ilch-56-6651.json
    match-2022ilch-56-7560.json
    match-2022ilch-57-1739.json
    match-2022ilch-57-3352.json
    match-2022ilch-57-4096.json
    match-2022ilch-57-4241.json
    match-2022ilch-57-4645.json
    match-2022ilch-57-48.json
    match-2022ilch-58-101.json
    match-2022ilch-58-112.json
    match-2022ilch-58-1781.json
    match-2022ilch-58-2062.json
    match-2022ilch-58-3110.json
    match-2022ilch-58-7460.json
    match-2022ilch-59-1625.json
    match-2022ilch-59-2151.json
    match-2022ilch-59-2220.json
    match-2022ilch-59-2338.json
    match-2022ilch-59-3067.json
    match-2022ilch-59-8880.json
    match-2022ilch-6-2358.json
    match-2022ilch-6-3067.json
    match-2022ilch-6-5125.json
    match-2022ilch-6-5934.json
    match-2022ilch-6-8096.json
    match-2022ilch-6-8122.json
    match-2022ilch-60-2451.json
    match-2022ilch-60-3061.json
    match-2022ilch-60-3695.json
    match-2022ilch-60-4145.json
    match-2022ilch-60-4292.json
    match-2022ilch-60-8096.json
    match-2022ilch-61-3488.json
    match-2022ilch-61-4787.json
    match-2022ilch-61-5125.json
    match-2022ilch-61-5553.json
    match-2022ilch-61-677.json
    match-2022ilch-61-8868.json
    match-2022ilch-62-111.json
    match-2022ilch-62-1732.json
    match-2022ilch-62-2358.json
    match-2022ilch-62-4702.json
    match-2022ilch-62-6381.json
    match-2022ilch-62-8029.json
    match-2022ilch-63-2062.json
    match-2022ilch-63-3352.json
    match-2022ilch-63-3734.json
    match-2022ilch-63-5847.json
    match-2022ilch-63-8122.json
    match-2022ilch-63-8802.json
    match-2022ilch-64-1739.json
    match-2022ilch-64-2220.json
    match-2022ilch-64-2830.json
    match-2022ilch-64-3110.json
    match-2022ilch-64-48.json
    match-2022ilch-64-8880.json
    match-2022ilch-65-112.json
    match-2022ilch-65-4241.json
    match-2022ilch-65-4292.json
    match-2022ilch-65-5822.json
    match-2022ilch-65-7460.json
    match-2022ilch-65-8096.json
    match-2022ilch-66-1781.json
    match-2022ilch-66-2151.json
    match-2022ilch-66-2451.json
    match-2022ilch-66-4096.json
    match-2022ilch-66-4145.json
    match-2022ilch-66-5125.json
    match-2022ilch-67-111.json
    match-2022ilch-67-1732.json
    match-2022ilch-67-2338.json
    match-2022ilch-67-5934.json
    match-2022ilch-67-6381.json
    match-2022ilch-67-677.json
    match-2022ilch-68-2022.json
    match-2022ilch-68-3061.json
    match-2022ilch-68-3067.json
    match-2022ilch-68-4645.json
    match-2022ilch-68-8029.json
    match-2022ilch-68-8122.json
    match-2022ilch-69-3488.json
    match-2022ilch-69-3695.json
    match-2022ilch-69-4702.json
    match-2022ilch-69-5847.json
    match-2022ilch-69-7560.json
    match-2022ilch-69-8868.json
    match-2022ilch-7-1625.json
    match-2022ilch-7-1739.json
    match-2022ilch-7-2151.json
    match-2022ilch-7-4292.json
    match-2022ilch-7-4702.json
    match-2022ilch-7-677.json
    match-2022ilch-70-101.json
    match-2022ilch-70-2358.json
    match-2022ilch-70-3734.json
    match-2022ilch-70-4787.json
    match-2022ilch-70-5553.json
    match-2022ilch-70-8802.json
    match-2022ilch-71-1625.json
    match-2022ilch-71-4096.json
    match-2022ilch-71-6651.json
    match-2022ilch-71-7237.json
    match-2022ilch-71-7460.json
    match-2022ilch-71-8096.json
    match-2022ilch-72-2451.json
    match-2022ilch-72-3110.json
    match-2022ilch-72-3352.json
    match-2022ilch-72-4292.json
    match-2022ilch-72-5934.json
    match-2022ilch-72-6381.json
    match-2022ilch-73-112.json
    match-2022ilch-73-2151.json
    match-2022ilch-73-2830.json
    match-2022ilch-73-4645.json
    match-2022ilch-73-5822.json
    match-2022ilch-73-677.json
    match-2022ilch-74-1739.json
    match-2022ilch-74-2022.json
    match-2022ilch-74-2062.json
    match-2022ilch-74-2338.json
    match-2022ilch-74-5125.json
    match-2022ilch-74-8029.json
    match-2022ilch-75-1781.json
    match-2022ilch-75-2358.json
    match-2022ilch-75-3695.json
    match-2022ilch-75-4241.json
    match-2022ilch-75-4702.json
    match-2022ilch-75-4787.json
    match-2022ilch-76-3488.json
    match-2022ilch-76-3734.json
    match-2022ilch-76-48.json
    match-2022ilch-76-6651.json
    match-2022ilch-76-8802.json
    match-2022ilch-76-8868.json
    match-2022ilch-77-101.json
    match-2022ilch-77-1732.json
    match-2022ilch-77-4145.json
    match-2022ilch-77-7237.json
    match-2022ilch-77-7560.json
    match-2022ilch-77-8880.json
    match-2022ilch-78-111.json
    match-2022ilch-78-1625.json
    match-2022ilch-78-3061.json
    match-2022ilch-78-3067.json
    match-2022ilch-78-5553.json
    match-2022ilch-78-5847.json
    match-2022ilch-79-1739.json
    match-2022ilch-79-2220.json
    match-2022ilch-79-2451.json
    match-2022ilch-79-4096.json
    match-2022ilch-79-7460.json
    match-2022ilch-79-8122.json
    match-2022ilch-8-1732.json
    match-2022ilch-8-3061.json
    match-2022ilch-8-3110.json
    match-2022ilch-8-4096.json
    match-2022ilch-8-4787.json
    match-2022ilch-8-7560.json
    match-2022ilch-9-101.json
    match-2022ilch-9-2022.json
    match-2022ilch-9-5847.json
    match-2022ilch-9-6381.json
    match-2022ilch-9-7460.json
    match-2022ilch-9-8868.json
    


```python
matches
```




    [{'total_shots': 12, 'shot_high': 9, 'taxi': True, 'climb': 0, 'team': 111},
     {'total_shots': 10, 'shot_high': 7, 'taxi': True, 'climb': 3, 'team': 2830},
     {'total_shots': 9, 'shot_high': 4, 'taxi': True, 'climb': 2, 'team': 3734},
     {'total_shots': 12, 'shot_high': 6, 'taxi': True, 'climb': 5, 'team': 7460},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8802},
     {'total_shots': 3, 'shot_high': 1, 'taxi': False, 'climb': 3, 'team': 8880},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2062},
     {'total_shots': 10, 'shot_high': 3, 'taxi': True, 'climb': 0, 'team': 2451},
     {'total_shots': 5, 'shot_high': 4, 'taxi': False, 'climb': 3, 'team': 2830},
     {'total_shots': 3, 'shot_high': 3, 'taxi': True, 'climb': 4, 'team': 4241},
     {'total_shots': 5, 'shot_high': 1, 'taxi': True, 'climb': 3, 'team': 5553},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 1, 'team': 6651},
     {'total_shots': 17, 'shot_high': 17, 'taxi': True, 'climb': 5, 'team': 111},
     {'total_shots': 10, 'shot_high': 3, 'taxi': True, 'climb': 4, 'team': 3695},
     {'total_shots': 11, 'shot_high': 0, 'taxi': False, 'climb': 5, 'team': 5822},
     {'total_shots': 12, 'shot_high': 6, 'taxi': True, 'climb': 3, 'team': 8122},
     {'total_shots': 5, 'shot_high': 2, 'taxi': True, 'climb': 3, 'team': 8880},
     {'total_shots': 14, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 1739},
     {'total_shots': 5, 'shot_high': 5, 'taxi': True, 'climb': 5, 'team': 1781},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4292},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 7237},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 8802},
     {'total_shots': 16, 'shot_high': 12, 'taxi': True, 'climb': 3, 'team': 112},
     {'total_shots': 6, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 3067},
     {'total_shots': 3, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3352},
     {'total_shots': 12, 'shot_high': 3, 'taxi': True, 'climb': 1, 'team': 4096},
     {'total_shots': 5, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 4787},
     {'total_shots': 4, 'shot_high': 1, 'taxi': True, 'climb': 5, 'team': 2338},
     {'total_shots': 7, 'shot_high': 2, 'taxi': True, 'climb': 2, 'team': 3734},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 4645},
     {'total_shots': 8, 'shot_high': 3, 'taxi': True, 'climb': 0, 'team': 677},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 3, 'team': 7560},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 8096},
     {'total_shots': 12, 'shot_high': 9, 'taxi': True, 'climb': 5, 'team': 1625},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3110},
     {'total_shots': 6, 'shot_high': 6, 'taxi': True, 'climb': 3, 'team': 3488},
     {'total_shots': 5, 'shot_high': 4, 'taxi': True, 'climb': 1, 'team': 4145},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4702},
     {'total_shots': 6, 'shot_high': 0, 'taxi': True, 'climb': 2, 'team': 5125},
     {'total_shots': 19, 'shot_high': 17, 'taxi': True, 'climb': 4, 'team': 1732},
     {'total_shots': 8, 'shot_high': 1, 'taxi': True, 'climb': 3, 'team': 2062},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2151},
     {'total_shots': 10, 'shot_high': 5, 'taxi': True, 'climb': 5, 'team': 2358},
     {'total_shots': 5, 'shot_high': 3, 'taxi': True, 'climb': 1, 'team': 48},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 6651},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 1739},
     {'total_shots': 15, 'shot_high': 11, 'taxi': True, 'climb': 0, 'team': 2451},
     {'total_shots': 8, 'shot_high': 5, 'taxi': True, 'climb': 4, 'team': 3695},
     {'total_shots': 8, 'shot_high': 8, 'taxi': True, 'climb': 2, 'team': 5553},
     {'total_shots': 6, 'shot_high': 0, 'taxi': True, 'climb': 5, 'team': 5822},
     {'total_shots': 7, 'shot_high': 5, 'taxi': True, 'climb': 5, 'team': 5847},
     {'total_shots': 7, 'shot_high': 5, 'taxi': True, 'climb': 5, 'team': 3061},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 4096},
     {'total_shots': 4, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 4241},
     {'total_shots': 12, 'shot_high': 11, 'taxi': True, 'climb': 3, 'team': 6381},
     {'total_shots': 6, 'shot_high': 3, 'taxi': True, 'climb': 3, 'team': 7460},
     {'total_shots': 4, 'shot_high': 1, 'taxi': True, 'climb': 1, 'team': 8880},
     {'total_shots': 11, 'shot_high': 10, 'taxi': True, 'climb': 5, 'team': 2338},
     {'total_shots': 11, 'shot_high': 9, 'taxi': True, 'climb': 3, 'team': 2830},
     {'total_shots': 8, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3067},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 1, 'team': 7237},
     {'total_shots': 9, 'shot_high': 5, 'taxi': True, 'climb': 3, 'team': 8122},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8868},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 101},
     {'total_shots': 10, 'shot_high': 7, 'taxi': False, 'climb': 4, 'team': 112},
     {'total_shots': 10, 'shot_high': 8, 'taxi': True, 'climb': 4, 'team': 2451},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4241},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 4, 'team': 8029},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8868},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3110},
     {'total_shots': 3, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 3352},
     {'total_shots': 7, 'shot_high': 1, 'taxi': True, 'climb': 0, 'team': 677},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 2, 'team': 7560},
     {'total_shots': 8, 'shot_high': 2, 'taxi': True, 'climb': 1, 'team': 8029},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 2, 'team': 8802},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 1, 'team': 111},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 5, 'team': 2022},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4292},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4787},
     {'total_shots': 9, 'shot_high': 8, 'taxi': False, 'climb': 4, 'team': 48},
     {'total_shots': 7, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 5125},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 101},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2151},
     {'total_shots': 6, 'shot_high': 1, 'taxi': True, 'climb': 3, 'team': 2220},
     {'total_shots': 3, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 4645},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4702},
     {'total_shots': 3, 'shot_high': 2, 'taxi': True, 'climb': 3, 'team': 8096},
     {'total_shots': 14, 'shot_high': 11, 'taxi': True, 'climb': 4, 'team': 112},
     {'total_shots': 10, 'shot_high': 8, 'taxi': True, 'climb': 4, 'team': 1625},
     {'total_shots': 10, 'shot_high': 9, 'taxi': True, 'climb': 5, 'team': 2358},
     {'total_shots': 10, 'shot_high': 5, 'taxi': True, 'climb': 0, 'team': 3734},
     {'total_shots': 3, 'shot_high': 1, 'taxi': True, 'climb': 0, 'team': 4145},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 5, 'team': 5934},
     {'total_shots': 20, 'shot_high': 17, 'taxi': True, 'climb': 0, 'team': 1732},
     {'total_shots': 10, 'shot_high': 6, 'taxi': True, 'climb': 5, 'team': 1781},
     {'total_shots': 3, 'shot_high': 1, 'taxi': True, 'climb': 3, 'team': 3067},
     {'total_shots': 4, 'shot_high': 2, 'taxi': True, 'climb': 3, 'team': 3488},
     {'total_shots': 2, 'shot_high': 1, 'taxi': True, 'climb': 5, 'team': 4241},
     {'total_shots': 6, 'shot_high': 0, 'taxi': True, 'climb': 5, 'team': 5822},
     {'total_shots': 14, 'shot_high': 12, 'taxi': True, 'climb': 5, 'team': 2338},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3110},
     {'total_shots': 12, 'shot_high': 4, 'taxi': True, 'climb': 4, 'team': 3695},
     {'total_shots': 13, 'shot_high': 2, 'taxi': True, 'climb': 3, 'team': 4096},
     {'total_shots': 3, 'shot_high': 1, 'taxi': True, 'climb': 1, 'team': 6651},
     {'total_shots': 12, 'shot_high': 3, 'taxi': True, 'climb': 3, 'team': 8122},
     {'total_shots': 12, 'shot_high': 4, 'taxi': True, 'climb': 0, 'team': 2062},
     {'total_shots': 5, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 4292},
     {'total_shots': 4, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 677},
     {'total_shots': 6, 'shot_high': 0, 'taxi': True, 'climb': 4, 'team': 7237},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 8029},
     {'total_shots': 6, 'shot_high': 3, 'taxi': True, 'climb': 3, 'team': 8880},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 101},
     {'total_shots': 21, 'shot_high': 17, 'taxi': True, 'climb': 5, 'team': 111},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2151},
     {'total_shots': 10, 'shot_high': 5, 'taxi': True, 'climb': 5, 'team': 3061},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 3352},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8868},
     {'total_shots': 8, 'shot_high': 4, 'taxi': False, 'climb': 3, 'team': 112},
     {'total_shots': 6, 'shot_high': 2, 'taxi': False, 'climb': 4, 'team': 2022},
     {'total_shots': 11, 'shot_high': 4, 'taxi': True, 'climb': 0, 'team': 4145},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 4702},
     {'total_shots': 4, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 4787},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 8802},
     {'total_shots': 18, 'shot_high': 16, 'taxi': True, 'climb': 4, 'team': 1732},
     {'total_shots': 7, 'shot_high': 1, 'taxi': True, 'climb': 1, 'team': 1739},
     {'total_shots': 8, 'shot_high': 5, 'taxi': True, 'climb': 3, 'team': 3734},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 2, 'team': 5125},
     {'total_shots': 4, 'shot_high': 3, 'taxi': True, 'climb': 5, 'team': 5847},
     {'total_shots': 1, 'shot_high': 1, 'taxi': True, 'climb': 3, 'team': 8096},
     {'total_shots': 8, 'shot_high': 5, 'taxi': True, 'climb': 5, 'team': 1781},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2022},
     {'total_shots': 6, 'shot_high': 4, 'taxi': True, 'climb': 5, 'team': 2220},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 4, 'team': 3061},
     {'total_shots': 5, 'shot_high': 2, 'taxi': True, 'climb': 0, 'team': 5847},
     {'total_shots': 4, 'shot_high': 2, 'taxi': True, 'climb': 1, 'team': 6651},
     {'total_shots': 6, 'shot_high': 3, 'taxi': True, 'climb': 5, 'team': 1625},
     {'total_shots': 6, 'shot_high': 5, 'taxi': True, 'climb': 4, 'team': 1781},
     {'total_shots': 13, 'shot_high': 11, 'taxi': True, 'climb': 0, 'team': 2451},
     {'total_shots': 13, 'shot_high': 12, 'taxi': True, 'climb': 4, 'team': 48},
     {'total_shots': 7, 'shot_high': 6, 'taxi': True, 'climb': 2, 'team': 6381},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 7560},
     {'total_shots': 4, 'shot_high': 2, 'taxi': True, 'climb': 4, 'team': 2220},
     {'total_shots': 3, 'shot_high': 3, 'taxi': True, 'climb': 1, 'team': 3488},
     {'total_shots': 1, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 4645},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 5553},
     {'total_shots': 6, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 5934},
     {'total_shots': 8, 'shot_high': 6, 'taxi': True, 'climb': 1, 'team': 7460},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 101},
     {'total_shots': 11, 'shot_high': 6, 'taxi': True, 'climb': 5, 'team': 2358},
     {'total_shots': 16, 'shot_high': 9, 'taxi': True, 'climb': 2, 'team': 2830},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 3352},
     {'total_shots': 10, 'shot_high': 4, 'taxi': True, 'climb': 0, 'team': 4096},
     {'total_shots': 4, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 4292},
     {'total_shots': 10, 'shot_high': 9, 'taxi': True, 'climb': 5, 'team': 2338},
     {'total_shots': 11, 'shot_high': 5, 'taxi': True, 'climb': 3, 'team': 3061},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 4241},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4702},
     {'total_shots': 1, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 5822},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 8802},
     {'total_shots': 14, 'shot_high': 12, 'taxi': True, 'climb': 5, 'team': 111},
     {'total_shots': 9, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 1739},
     {'total_shots': 3, 'shot_high': 1, 'taxi': True, 'climb': 3, 'team': 2062},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3067},
     {'total_shots': 11, 'shot_high': 9, 'taxi': True, 'climb': 0, 'team': 4145},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8868},
     {'total_shots': 12, 'shot_high': 10, 'taxi': True, 'climb': 3, 'team': 1732},
     {'total_shots': 6, 'shot_high': 5, 'taxi': True, 'climb': 4, 'team': 1781},
     {'total_shots': 7, 'shot_high': 5, 'taxi': True, 'climb': 0, 'team': 2022},
     {'total_shots': 9, 'shot_high': 9, 'taxi': True, 'climb': 0, 'team': 2451},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 8096},
     {'total_shots': 3, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8880},
     {'total_shots': 3, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 4645},
     {'total_shots': 7, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4787},
     {'total_shots': 7, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 5125},
     {'total_shots': 4, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 6651},
     {'total_shots': 10, 'shot_high': 8, 'taxi': True, 'climb': 0, 'team': 7460},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 7560},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2151},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 3110},
     {'total_shots': 3, 'shot_high': 1, 'taxi': True, 'climb': 4, 'team': 5553},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 5, 'team': 5934},
     {'total_shots': 12, 'shot_high': 7, 'taxi': False, 'climb': 0, 'team': 6381},
     {'total_shots': 9, 'shot_high': 2, 'taxi': True, 'climb': 3, 'team': 8122},
     {'total_shots': 12, 'shot_high': 8, 'taxi': True, 'climb': 4, 'team': 1625},
     {'total_shots': 5, 'shot_high': 4, 'taxi': True, 'climb': 5, 'team': 2220},
     {'total_shots': 17, 'shot_high': 13, 'taxi': True, 'climb': 3, 'team': 2830},
     {'total_shots': 8, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 3695},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 1, 'team': 3734},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8029},
     {'total_shots': 8, 'shot_high': 7, 'taxi': True, 'climb': 3, 'team': 112},
     {'total_shots': 8, 'shot_high': 5, 'taxi': True, 'climb': 5, 'team': 2358},
     {'total_shots': 7, 'shot_high': 7, 'taxi': True, 'climb': 4, 'team': 48},
     {'total_shots': 7, 'shot_high': 6, 'taxi': True, 'climb': 4, 'team': 5847},
     {'total_shots': 3, 'shot_high': 3, 'taxi': False, 'climb': 0, 'team': 677},
     {'total_shots': 8, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 7237},
     {'total_shots': 10, 'shot_high': 5, 'taxi': True, 'climb': 3, 'team': 2062},
     {'total_shots': 6, 'shot_high': 2, 'taxi': True, 'climb': 3, 'team': 3488},
     {'total_shots': 13, 'shot_high': 10, 'taxi': True, 'climb': 4, 'team': 3695},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 4645},
     {'total_shots': 12, 'shot_high': 5, 'taxi': True, 'climb': 1, 'team': 6381},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 7237},
     {'total_shots': 16, 'shot_high': 4, 'taxi': True, 'climb': 4, 'team': 111},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 5, 'team': 2022},
     {'total_shots': 5, 'shot_high': 5, 'taxi': True, 'climb': 3, 'team': 3488},
     {'total_shots': 8, 'shot_high': 3, 'taxi': True, 'climb': 3, 'team': 4096},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 2, 'team': 8096},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8802},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 1739},
     {'total_shots': 21, 'shot_high': 14, 'taxi': True, 'climb': 0, 'team': 2451},
     {'total_shots': 2, 'shot_high': 1, 'taxi': False, 'climb': 0, 'team': 4645},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 4702},
     {'total_shots': 10, 'shot_high': 3, 'taxi': True, 'climb': 0, 'team': 6651},
     {'total_shots': 5, 'shot_high': 3, 'taxi': True, 'climb': 2, 'team': 8880},
     {'total_shots': 12, 'shot_high': 9, 'taxi': True, 'climb': 5, 'team': 1781},
     {'total_shots': 5, 'shot_high': 2, 'taxi': True, 'climb': 3, 'team': 2062},
     {'total_shots': 16, 'shot_high': 13, 'taxi': True, 'climb': 5, 'team': 2338},
     {'total_shots': 11, 'shot_high': 10, 'taxi': True, 'climb': 5, 'team': 3061},
     {'total_shots': 7, 'shot_high': 0, 'taxi': False, 'climb': 3, 'team': 4787},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 5934},
     {'total_shots': 8, 'shot_high': 5, 'taxi': True, 'climb': 4, 'team': 2220},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3110},
     {'total_shots': 2, 'shot_high': 1, 'taxi': False, 'climb': 1, 'team': 3734},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 5822},
     {'total_shots': 15, 'shot_high': 10, 'taxi': True, 'climb': 3, 'team': 6381},
     {'total_shots': 1, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 8868},
     {'total_shots': 14, 'shot_high': 7, 'taxi': True, 'climb': 3, 'team': 1625},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 2830},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 3352},
     {'total_shots': 3, 'shot_high': 1, 'taxi': True, 'climb': 1, 'team': 4241},
     {'total_shots': 6, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 5125},
     {'total_shots': 13, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 7237},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 4, 'team': 112},
     {'total_shots': 15, 'shot_high': 15, 'taxi': True, 'climb': 4, 'team': 1732},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4292},
     {'total_shots': 8, 'shot_high': 5, 'taxi': True, 'climb': 4, 'team': 5553},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 7560},
     {'total_shots': 8, 'shot_high': 2, 'taxi': True, 'climb': 3, 'team': 8122},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 101},
     {'total_shots': 3, 'shot_high': 1, 'taxi': True, 'climb': 1, 'team': 3067},
     {'total_shots': 9, 'shot_high': 2, 'taxi': True, 'climb': 4, 'team': 3695},
     {'total_shots': 11, 'shot_high': 11, 'taxi': True, 'climb': 5, 'team': 48},
     {'total_shots': 8, 'shot_high': 5, 'taxi': True, 'climb': 0, 'team': 677},
     {'total_shots': 6, 'shot_high': 5, 'taxi': True, 'climb': 0, 'team': 7460},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2151},
     {'total_shots': 8, 'shot_high': 4, 'taxi': True, 'climb': 5, 'team': 2358},
     {'total_shots': 3, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 3488},
     {'total_shots': 8, 'shot_high': 8, 'taxi': True, 'climb': 5, 'team': 4145},
     {'total_shots': 5, 'shot_high': 5, 'taxi': True, 'climb': 4, 'team': 5847},
     {'total_shots': 5, 'shot_high': 4, 'taxi': True, 'climb': 0, 'team': 8029},
     {'total_shots': 12, 'shot_high': 6, 'taxi': True, 'climb': 3, 'team': 2062},
     {'total_shots': 21, 'shot_high': 13, 'taxi': True, 'climb': 0, 'team': 4096},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 5, 'team': 5822},
     {'total_shots': 9, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 5934},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8868},
     {'total_shots': 3, 'shot_high': 1, 'taxi': True, 'climb': 3, 'team': 8880},
     {'total_shots': 15, 'shot_high': 7, 'taxi': True, 'climb': 5, 'team': 111},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2022},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3110},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 4, 'team': 4241},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 4645},
     {'total_shots': 4, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 7237},
     {'total_shots': 14, 'shot_high': 12, 'taxi': True, 'climb': 5, 'team': 2338},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3352},
     {'total_shots': 5, 'shot_high': 3, 'taxi': True, 'climb': 1, 'team': 4145},
     {'total_shots': 8, 'shot_high': 6, 'taxi': True, 'climb': 3, 'team': 48},
     {'total_shots': 3, 'shot_high': 2, 'taxi': True, 'climb': 3, 'team': 5553},
     {'total_shots': 8, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 5822},
     {'total_shots': 18, 'shot_high': 13, 'taxi': True, 'climb': 4, 'team': 112},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 1739},
     {'total_shots': 3, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 3352},
     {'total_shots': 10, 'shot_high': 9, 'taxi': True, 'climb': 0, 'team': 6381},
     {'total_shots': 7, 'shot_high': 6, 'taxi': True, 'climb': 2, 'team': 6651},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 7560},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 1732},
     {'total_shots': 4, 'shot_high': 3, 'taxi': False, 'climb': 5, 'team': 2220},
     {'total_shots': 10, 'shot_high': 6, 'taxi': True, 'climb': 3, 'team': 2830},
     {'total_shots': 6, 'shot_high': 4, 'taxi': True, 'climb': 4, 'team': 3695},
     {'total_shots': 9, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 5125},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 2, 'team': 8802},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2151},
     {'total_shots': 9, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 4787},
     {'total_shots': 9, 'shot_high': 5, 'taxi': True, 'climb': 4, 'team': 48},
     {'total_shots': 11, 'shot_high': 4, 'taxi': True, 'climb': 2, 'team': 7460},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8029},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 8096},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 101},
     {'total_shots': 9, 'shot_high': 3, 'taxi': True, 'climb': 4, 'team': 1625},
     {'total_shots': 8, 'shot_high': 6, 'taxi': True, 'climb': 1, 'team': 1781},
     {'total_shots': 8, 'shot_high': 4, 'taxi': True, 'climb': 3, 'team': 4145},
     {'total_shots': 9, 'shot_high': 8, 'taxi': True, 'climb': 0, 'team': 677},
     {'total_shots': 11, 'shot_high': 5, 'taxi': True, 'climb': 3, 'team': 8122},
     {'total_shots': 15, 'shot_high': 12, 'taxi': True, 'climb': 4, 'team': 2338},
     {'total_shots': 10, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 3067},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4292},
     {'total_shots': 2, 'shot_high': 2, 'taxi': True, 'climb': 0, 'team': 4702},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 4, 'team': 5553},
     {'total_shots': 10, 'shot_high': 2, 'taxi': True, 'climb': 4, 'team': 5847},
     {'total_shots': 6, 'shot_high': 4, 'taxi': True, 'climb': 5, 'team': 2358},
     {'total_shots': 18, 'shot_high': 15, 'taxi': True, 'climb': 0, 'team': 2451},
     {'total_shots': 12, 'shot_high': 11, 'taxi': True, 'climb': 5, 'team': 3061},
     {'total_shots': 6, 'shot_high': 6, 'taxi': True, 'climb': 3, 'team': 3488},
     {'total_shots': 12, 'shot_high': 7, 'taxi': True, 'climb': 2, 'team': 3734},
     {'total_shots': 7, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 7237},
     {'total_shots': 1, 'shot_high': 1, 'taxi': True, 'climb': 0, 'team': 2022},
     {'total_shots': 14, 'shot_high': 9, 'taxi': True, 'climb': 3, 'team': 2830},
     {'total_shots': 9, 'shot_high': 0, 'taxi': True, 'climb': 5, 'team': 5822},
     {'total_shots': 3, 'shot_high': 0, 'taxi': False, 'climb': 5, 'team': 5934},
     {'total_shots': 9, 'shot_high': 6, 'taxi': True, 'climb': 0, 'team': 6651},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 7560},
     {'total_shots': 4, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 1739},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 3352},
     {'total_shots': 5, 'shot_high': 3, 'taxi': True, 'climb': 3, 'team': 4096},
     {'total_shots': 4, 'shot_high': 1, 'taxi': True, 'climb': 4, 'team': 4241},
     {'total_shots': 3, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 4645},
     {'total_shots': 15, 'shot_high': 14, 'taxi': True, 'climb': 5, 'team': 48},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 101},
     {'total_shots': 10, 'shot_high': 9, 'taxi': True, 'climb': 4, 'team': 112},
     {'total_shots': 11, 'shot_high': 5, 'taxi': True, 'climb': 5, 'team': 1781},
     {'total_shots': 7, 'shot_high': 4, 'taxi': True, 'climb': 1, 'team': 2062},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3110},
     {'total_shots': 7, 'shot_high': 6, 'taxi': True, 'climb': 3, 'team': 7460},
     {'total_shots': 12, 'shot_high': 7, 'taxi': True, 'climb': 4, 'team': 1625},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2151},
     {'total_shots': 3, 'shot_high': 3, 'taxi': True, 'climb': 3, 'team': 2220},
     {'total_shots': 14, 'shot_high': 12, 'taxi': True, 'climb': 4, 'team': 2338},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3067},
     {'total_shots': 5, 'shot_high': 4, 'taxi': True, 'climb': 3, 'team': 8880},
     {'total_shots': 8, 'shot_high': 1, 'taxi': True, 'climb': 5, 'team': 2358},
     {'total_shots': 6, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 3067},
     {'total_shots': 9, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 5125},
     {'total_shots': 6, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 5934},
     {'total_shots': 1, 'shot_high': 0, 'taxi': False, 'climb': 3, 'team': 8096},
     {'total_shots': 14, 'shot_high': 4, 'taxi': True, 'climb': 3, 'team': 8122},
     {'total_shots': 10, 'shot_high': 7, 'taxi': True, 'climb': 4, 'team': 2451},
     {'total_shots': 13, 'shot_high': 9, 'taxi': True, 'climb': 5, 'team': 3061},
     {'total_shots': 11, 'shot_high': 10, 'taxi': True, 'climb': 4, 'team': 3695},
     {'total_shots': 7, 'shot_high': 4, 'taxi': True, 'climb': 5, 'team': 4145},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4292},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 2, 'team': 8096},
     {'total_shots': 6, 'shot_high': 6, 'taxi': True, 'climb': 3, 'team': 3488},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 4787},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 5125},
     {'total_shots': 5, 'shot_high': 3, 'taxi': True, 'climb': 4, 'team': 5553},
     {'total_shots': 5, 'shot_high': 2, 'taxi': True, 'climb': 0, 'team': 677},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8868},
     {'total_shots': 13, 'shot_high': 13, 'taxi': True, 'climb': 0, 'team': 111},
     {'total_shots': 10, 'shot_high': 7, 'taxi': True, 'climb': 4, 'team': 1732},
     {'total_shots': 11, 'shot_high': 7, 'taxi': True, 'climb': 5, 'team': 2358},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4702},
     {'total_shots': 6, 'shot_high': 2, 'taxi': True, 'climb': 3, 'team': 6381},
     {'total_shots': 4, 'shot_high': 4, 'taxi': True, 'climb': 3, 'team': 8029},
     {'total_shots': 13, 'shot_high': 6, 'taxi': True, 'climb': 3, 'team': 2062},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 3352},
     {'total_shots': 8, 'shot_high': 4, 'taxi': True, 'climb': 1, 'team': 3734},
     {'total_shots': 10, 'shot_high': 8, 'taxi': True, 'climb': 5, 'team': 5847},
     {'total_shots': 7, 'shot_high': 3, 'taxi': True, 'climb': 1, 'team': 8122},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 8802},
     {'total_shots': 7, 'shot_high': 1, 'taxi': True, 'climb': 1, 'team': 1739},
     {'total_shots': 6, 'shot_high': 6, 'taxi': True, 'climb': 3, 'team': 2220},
     {'total_shots': 16, 'shot_high': 11, 'taxi': True, 'climb': 3, 'team': 2830},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3110},
     {'total_shots': 14, 'shot_high': 12, 'taxi': True, 'climb': 1, 'team': 48},
     {'total_shots': 5, 'shot_high': 2, 'taxi': True, 'climb': 3, 'team': 8880},
     {'total_shots': 17, 'shot_high': 15, 'taxi': True, 'climb': 0, 'team': 112},
     {'total_shots': 4, 'shot_high': 1, 'taxi': True, 'climb': 3, 'team': 4241},
     {'total_shots': 5, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4292},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 5, 'team': 5822},
     {'total_shots': 6, 'shot_high': 4, 'taxi': True, 'climb': 3, 'team': 7460},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8096},
     {'total_shots': 9, 'shot_high': 6, 'taxi': True, 'climb': 5, 'team': 1781},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2151},
     {'total_shots': 21, 'shot_high': 16, 'taxi': True, 'climb': 4, 'team': 2451},
     {'total_shots': 3, 'shot_high': 1, 'taxi': False, 'climb': 3, 'team': 4096},
     {'total_shots': 4, 'shot_high': 2, 'taxi': True, 'climb': 5, 'team': 4145},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 2, 'team': 5125},
     {'total_shots': 18, 'shot_high': 16, 'taxi': True, 'climb': 5, 'team': 111},
     {'total_shots': 13, 'shot_high': 10, 'taxi': True, 'climb': 4, 'team': 1732},
     {'total_shots': 13, 'shot_high': 13, 'taxi': True, 'climb': 5, 'team': 2338},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 5934},
     {'total_shots': 10, 'shot_high': 5, 'taxi': True, 'climb': 2, 'team': 6381},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 677},
     {'total_shots': 7, 'shot_high': 4, 'taxi': True, 'climb': 4, 'team': 2022},
     {'total_shots': 17, 'shot_high': 14, 'taxi': True, 'climb': 5, 'team': 3061},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3067},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4645},
     {'total_shots': 9, 'shot_high': 3, 'taxi': True, 'climb': 3, 'team': 8029},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 4, 'team': 8122},
     {'total_shots': 8, 'shot_high': 7, 'taxi': True, 'climb': 3, 'team': 3488},
     {'total_shots': 15, 'shot_high': 7, 'taxi': True, 'climb': 4, 'team': 3695},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4702},
     {'total_shots': 13, 'shot_high': 12, 'taxi': True, 'climb': 5, 'team': 5847},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 7560},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8868},
     {'total_shots': 11, 'shot_high': 6, 'taxi': False, 'climb': 4, 'team': 1625},
     {'total_shots': 8, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 1739},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2151},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4292},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 4702},
     {'total_shots': 5, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 677},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 101},
     {'total_shots': 8, 'shot_high': 4, 'taxi': True, 'climb': 5, 'team': 2358},
     {'total_shots': 16, 'shot_high': 6, 'taxi': True, 'climb': 0, 'team': 3734},
     {'total_shots': 6, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4787},
     {'total_shots': 9, 'shot_high': 5, 'taxi': True, 'climb': 0, 'team': 5553},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 8802},
     {'total_shots': 9, 'shot_high': 3, 'taxi': True, 'climb': 0, 'team': 1625},
     {'total_shots': 10, 'shot_high': 4, 'taxi': True, 'climb': 3, 'team': 4096},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 6651},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 3, 'team': 7237},
     {'total_shots': 3, 'shot_high': 1, 'taxi': True, 'climb': 4, 'team': 7460},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 8096},
     {'total_shots': 11, 'shot_high': 8, 'taxi': True, 'climb': 4, 'team': 2451},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 3110},
     {'total_shots': 4, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 3352},
     {'total_shots': 3, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4292},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 5934},
     {'total_shots': 13, 'shot_high': 8, 'taxi': True, 'climb': 3, 'team': 6381},
     {'total_shots': 14, 'shot_high': 9, 'taxi': True, 'climb': 4, 'team': 112},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2151},
     {'total_shots': 5, 'shot_high': 3, 'taxi': True, 'climb': 3, 'team': 2830},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 4645},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 5, 'team': 5822},
     {'total_shots': 5, 'shot_high': 1, 'taxi': True, 'climb': 0, 'team': 677},
     {'total_shots': 10, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 1739},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 2022},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 2062},
     {'total_shots': 5, 'shot_high': 4, 'taxi': True, 'climb': 5, 'team': 2338},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 5125},
     {'total_shots': 4, 'shot_high': 1, 'taxi': True, 'climb': 3, 'team': 8029},
     {'total_shots': 11, 'shot_high': 8, 'taxi': True, 'climb': 5, 'team': 1781},
     {'total_shots': 10, 'shot_high': 8, 'taxi': True, 'climb': 5, 'team': 2358},
     {'total_shots': 12, 'shot_high': 6, 'taxi': True, 'climb': 3, 'team': 3695},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 5, 'team': 4241},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 4702},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 4787},
     {'total_shots': 5, 'shot_high': 5, 'taxi': True, 'climb': 3, 'team': 3488},
     {'total_shots': 7, 'shot_high': 4, 'taxi': True, 'climb': 3, 'team': 3734},
     {'total_shots': 8, 'shot_high': 7, 'taxi': True, 'climb': 5, 'team': 48},
     {'total_shots': 6, 'shot_high': 3, 'taxi': False, 'climb': 1, 'team': 6651},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 8802},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8868},
     {'total_shots': 4, 'shot_high': 1, 'taxi': True, 'climb': 0, 'team': 101},
     {'total_shots': 20, 'shot_high': 15, 'taxi': True, 'climb': 3, 'team': 1732},
     {'total_shots': 1, 'shot_high': 1, 'taxi': True, 'climb': 5, 'team': 4145},
     {'total_shots': 1, 'shot_high': 0, 'taxi': True, 'climb': 2, 'team': 7237},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 7560},
     {'total_shots': 4, 'shot_high': 1, 'taxi': True, 'climb': 3, 'team': 8880},
     {'total_shots': 22, 'shot_high': 19, 'taxi': True, 'climb': 4, 'team': 111},
     {'total_shots': 3, 'shot_high': 2, 'taxi': True, 'climb': 0, 'team': 1625},
     {'total_shots': 15, 'shot_high': 8, 'taxi': True, 'climb': 5, 'team': 3061},
     {'total_shots': 3, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 3067},
     {'total_shots': 3, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 5553},
     {'total_shots': 7, 'shot_high': 4, 'taxi': True, 'climb': 3, 'team': 5847},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 3, 'team': 1739},
     {'total_shots': 6, 'shot_high': 5, 'taxi': True, 'climb': 5, 'team': 2220},
     {'total_shots': 17, 'shot_high': 16, 'taxi': True, 'climb': 0, 'team': 2451},
     {'total_shots': 17, 'shot_high': 14, 'taxi': True, 'climb': 0, 'team': 4096},
     {'total_shots': 6, 'shot_high': 4, 'taxi': True, 'climb': 3, 'team': 7460},
     {'total_shots': 13, 'shot_high': 4, 'taxi': True, 'climb': 1, 'team': 8122},
     {'total_shots': 18, 'shot_high': 17, 'taxi': True, 'climb': 1, 'team': 1732},
     {'total_shots': 12, 'shot_high': 10, 'taxi': True, 'climb': 4, 'team': 3061},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 3110},
     {'total_shots': 4, 'shot_high': 1, 'taxi': True, 'climb': 0, 'team': 4096},
     {'total_shots': 2, 'shot_high': 0, 'taxi': True, 'climb': 1, 'team': 4787},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 7560},
     {'total_shots': 0, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 101},
     {'total_shots': 0, 'shot_high': 0, 'taxi': False, 'climb': 0, 'team': 2022},
     {'total_shots': 8, 'shot_high': 5, 'taxi': True, 'climb': 1, 'team': 5847},
     {'total_shots': 8, 'shot_high': 6, 'taxi': True, 'climb': 3, 'team': 6381},
     {'total_shots': 7, 'shot_high': 6, 'taxi': True, 'climb': 5, 'team': 7460},
     {'total_shots': 4, 'shot_high': 0, 'taxi': True, 'climb': 0, 'team': 8868}]




```python
team_list = {match['team'] for match in matches}
print(team_list)
```

    {4096, 5125, 7560, 2830, 2062, 4241, 2451, 3734, 3352, 8096, 3488, 2338, 7460, 4645, 677, 3110, 8868, 2220, 5934, 8880, 5553, 4145, 4787, 48, 2358, 8122, 5822, 4292, 7237, 1732, 3067, 1739, 5847, 1625, 8029, 4702, 8802, 101, 2022, 2151, 6381, 111, 3695, 112, 1781, 3061, 6651}
    


```python
# regional = {team: {shot_percentage: val, climb_lvl: val}}
# regional['team']['shot_percentage']
# regional = {dothis for each in what}
regional = {team: {} for team in team_list}
```


```python
def shot_percentage(team: int) -> float:
    total = 0
    total_made = 0
    for each_match in matches:
        if each_match['team'] == team:
            total = total + each_match['total_shots']
            total_made = total_made + each_match['shot_high']
    return total_made/total, total, total_made

shot_percentage(111)
```




    (0.7702702702702703, 148, 114)




```python
for team in regional:
    percent, total, made = shot_percentage(team)
    regional[team]['shot_percentage'] = percent
    regional[team]['total'] = total
    regional[team]['total_made'] = made
    
regional
```




    {4096: {'shot_percentage': 0.46601941747572817,
      'total': 103,
      'total_made': 48},
     5125: {'shot_percentage': 0.0, 'total': 47, 'total_made': 0},
     7560: {'shot_percentage': 0.0, 'total': 1, 'total_made': 0},
     2830: {'shot_percentage': 0.6826923076923077, 'total': 104, 'total_made': 71},
     2062: {'shot_percentage': 0.4084507042253521, 'total': 71, 'total_made': 29},
     4241: {'shot_percentage': 0.28, 'total': 25, 'total_made': 7},
     2451: {'shot_percentage': 0.7612903225806451,
      'total': 155,
      'total_made': 118},
     3734: {'shot_percentage': 0.4810126582278481, 'total': 79, 'total_made': 38},
     3352: {'shot_percentage': 0.0, 'total': 17, 'total_made': 0},
     8096: {'shot_percentage': 0.6, 'total': 5, 'total_made': 3},
     3488: {'shot_percentage': 0.8076923076923077, 'total': 52, 'total_made': 42},
     2338: {'shot_percentage': 0.8448275862068966, 'total': 116, 'total_made': 98},
     7460: {'shot_percentage': 0.6463414634146342, 'total': 82, 'total_made': 53},
     4645: {'shot_percentage': 0.0625, 'total': 16, 'total_made': 1},
     677: {'shot_percentage': 0.42592592592592593, 'total': 54, 'total_made': 23},
     3110: {'shot_percentage': 0.0, 'total': 1, 'total_made': 0},
     8868: {'shot_percentage': 0.0, 'total': 8, 'total_made': 0},
     2220: {'shot_percentage': 0.6875, 'total': 48, 'total_made': 33},
     5934: {'shot_percentage': 0.0, 'total': 26, 'total_made': 0},
     8880: {'shot_percentage': 0.4186046511627907, 'total': 43, 'total_made': 18},
     5553: {'shot_percentage': 0.5434782608695652, 'total': 46, 'total_made': 25},
     4145: {'shot_percentage': 0.6349206349206349, 'total': 63, 'total_made': 40},
     4787: {'shot_percentage': 0.0, 'total': 40, 'total_made': 0},
     48: {'shot_percentage': 0.8585858585858586, 'total': 99, 'total_made': 85},
     2358: {'shot_percentage': 0.5888888888888889, 'total': 90, 'total_made': 53},
     8122: {'shot_percentage': 0.35789473684210527, 'total': 95, 'total_made': 34},
     5822: {'shot_percentage': 0.0, 'total': 44, 'total_made': 0},
     4292: {'shot_percentage': 0.0, 'total': 23, 'total_made': 0},
     7237: {'shot_percentage': 0.0, 'total': 39, 'total_made': 0},
     1732: {'shot_percentage': 0.8435374149659864,
      'total': 147,
      'total_made': 124},
     3067: {'shot_percentage': 0.046511627906976744, 'total': 43, 'total_made': 2},
     1739: {'shot_percentage': 0.03333333333333333, 'total': 60, 'total_made': 2},
     5847: {'shot_percentage': 0.6842105263157895, 'total': 76, 'total_made': 52},
     1625: {'shot_percentage': 0.5714285714285714, 'total': 98, 'total_made': 56},
     8029: {'shot_percentage': 0.42424242424242425, 'total': 33, 'total_made': 14},
     4702: {'shot_percentage': 0.5, 'total': 4, 'total_made': 2},
     8802: {'shot_percentage': 0.0, 'total': 1, 'total_made': 0},
     101: {'shot_percentage': 0.16666666666666666, 'total': 6, 'total_made': 1},
     2022: {'shot_percentage': 0.5454545454545454, 'total': 22, 'total_made': 12},
     2151: {'shot_percentage': 0.0, 'total': 3, 'total_made': 0},
     6381: {'shot_percentage': 0.6571428571428571, 'total': 105, 'total_made': 69},
     111: {'shot_percentage': 0.7702702702702703, 'total': 148, 'total_made': 114},
     3695: {'shot_percentage': 0.49038461538461536,
      'total': 104,
      'total_made': 51},
     112: {'shot_percentage': 0.7565217391304347, 'total': 115, 'total_made': 87},
     1781: {'shot_percentage': 0.6976744186046512, 'total': 86, 'total_made': 60},
     3061: {'shot_percentage': 0.7129629629629629, 'total': 108, 'total_made': 77},
     6651: {'shot_percentage': 0.4883720930232558, 'total': 43, 'total_made': 21}}




```python

# My x-y coordinate data
x = [1, 2, 1]
y = [1, 1, 3]

# Output the visualization directly in the notebook
# output_file('first_glyphs.html', title='First Glyphs')

# Create a figure with no toolbar and axis ranges of [0,3]
fig = figure(title='My Coordinates',
             plot_height=300, plot_width=300,
             x_range=(0, 3), y_range=(0, 3),
             toolbar_location="right")

# Draw the coordinates as circles
fig.circle(x=x, y=y,
           color='saddlebrown', size=50, alpha=0.75)

# Show plot|
show(fig)
```



<div class="bk-root" id="7cf783e9-3326-43da-a37f-62b8bfdad400" data-root-id="1003"></div>






```python
tp = [[team, regional[team]['shot_percentage']] for team in regional]
tp.sort(reverse=True, key=lambda sort:sort[1])
pprint(tp[:10])
```

    [[48, 0.8585858585858586],
     [2338, 0.8448275862068966],
     [1732, 0.8435374149659864],
     [3488, 0.8076923076923077],
     [111, 0.7702702702702703],
     [2451, 0.7612903225806451],
     [112, 0.7565217391304347],
     [3061, 0.7129629629629629],
     [1781, 0.6976744186046512],
     [2220, 0.6875]]
    


```python
pprint(regional.items())
```

    dict_items([(4096, {'shot_percentage': 0.46601941747572817, 'total': 103, 'total_made': 48}), (5125, {'shot_percentage': 0.0, 'total': 47, 'total_made': 0}), (7560, {'shot_percentage': 0.0, 'total': 1, 'total_made': 0}), (2830, {'shot_percentage': 0.6826923076923077, 'total': 104, 'total_made': 71}), (2062, {'shot_percentage': 0.4084507042253521, 'total': 71, 'total_made': 29}), (4241, {'shot_percentage': 0.28, 'total': 25, 'total_made': 7}), (2451, {'shot_percentage': 0.7612903225806451, 'total': 155, 'total_made': 118}), (3734, {'shot_percentage': 0.4810126582278481, 'total': 79, 'total_made': 38}), (3352, {'shot_percentage': 0.0, 'total': 17, 'total_made': 0}), (8096, {'shot_percentage': 0.6, 'total': 5, 'total_made': 3}), (3488, {'shot_percentage': 0.8076923076923077, 'total': 52, 'total_made': 42}), (2338, {'shot_percentage': 0.8448275862068966, 'total': 116, 'total_made': 98}), (7460, {'shot_percentage': 0.6463414634146342, 'total': 82, 'total_made': 53}), (4645, {'shot_percentage': 0.0625, 'total': 16, 'total_made': 1}), (677, {'shot_percentage': 0.42592592592592593, 'total': 54, 'total_made': 23}), (3110, {'shot_percentage': 0.0, 'total': 1, 'total_made': 0}), (8868, {'shot_percentage': 0.0, 'total': 8, 'total_made': 0}), (2220, {'shot_percentage': 0.6875, 'total': 48, 'total_made': 33}), (5934, {'shot_percentage': 0.0, 'total': 26, 'total_made': 0}), (8880, {'shot_percentage': 0.4186046511627907, 'total': 43, 'total_made': 18}), (5553, {'shot_percentage': 0.5434782608695652, 'total': 46, 'total_made': 25}), (4145, {'shot_percentage': 0.6349206349206349, 'total': 63, 'total_made': 40}), (4787, {'shot_percentage': 0.0, 'total': 40, 'total_made': 0}), (48, {'shot_percentage': 0.8585858585858586, 'total': 99, 'total_made': 85}), (2358, {'shot_percentage': 0.5888888888888889, 'total': 90, 'total_made': 53}), (8122, {'shot_percentage': 0.35789473684210527, 'total': 95, 'total_made': 34}), (5822, {'shot_percentage': 0.0, 'total': 44, 'total_made': 0}), (4292, {'shot_percentage': 0.0, 'total': 23, 'total_made': 0}), (7237, {'shot_percentage': 0.0, 'total': 39, 'total_made': 0}), (1732, {'shot_percentage': 0.8435374149659864, 'total': 147, 'total_made': 124}), (3067, {'shot_percentage': 0.046511627906976744, 'total': 43, 'total_made': 2}), (1739, {'shot_percentage': 0.03333333333333333, 'total': 60, 'total_made': 2}), (5847, {'shot_percentage': 0.6842105263157895, 'total': 76, 'total_made': 52}), (1625, {'shot_percentage': 0.5714285714285714, 'total': 98, 'total_made': 56}), (8029, {'shot_percentage': 0.42424242424242425, 'total': 33, 'total_made': 14}), (4702, {'shot_percentage': 0.5, 'total': 4, 'total_made': 2}), (8802, {'shot_percentage': 0.0, 'total': 1, 'total_made': 0}), (101, {'shot_percentage': 0.16666666666666666, 'total': 6, 'total_made': 1}), (2022, {'shot_percentage': 0.5454545454545454, 'total': 22, 'total_made': 12}), (2151, {'shot_percentage': 0.0, 'total': 3, 'total_made': 0}), (6381, {'shot_percentage': 0.6571428571428571, 'total': 105, 'total_made': 69}), (111, {'shot_percentage': 0.7702702702702703, 'total': 148, 'total_made': 114}), (3695, {'shot_percentage': 0.49038461538461536, 'total': 104, 'total_made': 51}), (112, {'shot_percentage': 0.7565217391304347, 'total': 115, 'total_made': 87}), (1781, {'shot_percentage': 0.6976744186046512, 'total': 86, 'total_made': 60}), (3061, {'shot_percentage': 0.7129629629629629, 'total': 108, 'total_made': 77}), (6651, {'shot_percentage': 0.4883720930232558, 'total': 43, 'total_made': 21})])
    


```python

```
