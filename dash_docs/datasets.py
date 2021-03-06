import pandas as pd
import numpy as np
from collections import OrderedDict
import os

data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)
df_regions = pd.DataFrame(data)

df_datatypes = df_regions
df_datatypes['Delivery'] = [
    "2015-01-02", "2015-10-24", "2016-05-15",
    "2017-01-14", "2018-05-10", "2018-08-11"
]

data_election = OrderedDict(
    [
        (
            "Date",
            [
                "July 12th, 2013 - July 25th, 2013",
                "July 12th, 2013 - August 25th, 2013",
                "July 12th, 2014 - August 25th, 2014",
            ],
        ),
        (
            "Election Polling Organization",
            ["The New York Times", "Pew Research", "The Washington Post"],
        ),
        ("Rep", [1, -20, 3.512]),
        ("Dem", [10, 20, 30]),
        ("Ind", [2, 10924, 3912]),
        (
            "Region",
            [
                "Northern New York State to the Southern Appalachian Mountains",
                "Canada",
                "Southern Vermont",
            ],
        ),
    ]
)

df_election = pd.DataFrame(data_election)
df_long = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
)
df_long_columns = pd.DataFrame(
    {
        "This is Column {} Data".format(i): [1, 2]
        for i in range(10)
    }
)
wide_data = [
    {'Firm': 'Acme', '2017': 13, '2018': 5, '2019': 10, '2020': 4},
    {'Firm': 'Olive', '2017': 3, '2018': 3, '2019': 13, '2020': 3},
    {'Firm': 'Barnwood', '2017': 6, '2018': 7, '2019': 3, '2020': 6},
    {'Firm': 'Henrietta', '2017': -3, '2018': -10, '2019': -5, '2020': -6},
]
df_wide = pd.DataFrame(wide_data)

data_with_none = [
    {'Firm': 'Acme', '2017': '', '2018': 5, '2019': 10, '2020': 4},
    {'Firm': 'Olive', '2017': None, '2018': 3, '2019': 13, '2020': 3},
    {'Firm': 'Barnwood', '2017': np.NaN, '2018': 7, '2019': 3, '2020': 6},
    {'Firm': 'Henrietta', '2017': 14, '2018': 1, '2019': 13, '2020': 1},
]
df_with_none = pd.DataFrame(data_with_none)
df_gapminder = pd.read_csv('datasets/gapminderDataFiveYear.csv' if 'DASH_DOCS_URL_PREFIX' in os.environ else 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

many_columns = OrderedDict(
    [
        ('Column {}'.format(i+1), [51231.431, 3124.31, 1234.124, 122412.31])
        for i in range(15)
    ]
)
df_15_columns = pd.DataFrame(many_columns)
data_numeric = pd.DataFrame(OrderedDict(
    [
        [
            'Column {}'.format(i + 1), list(range(30))
        ] for i in range(15)
    ]
))
moby_dick_text = [
    'Call me Ishmael. ',
    ''.join([
        'Some years ago- never mind how long precisely- having little or no money ',
        'in my purse, and nothing particular to interest me on shore, ',
        'I thought I would sail about a little and see the watery part of the world. ',
    ]),
    'It is a way I have of driving off the spleen and regulating the circulation.'
]

moby_dick = OrderedDict(
    [
        (
            'Sentence Number', [i+1 for i in range(len(moby_dick_text))],
        ),
        (
            'Text', [i for i in moby_dick_text]
        )
    ]
)
df_moby_dick = pd.DataFrame(moby_dick)
df_numeric = pd.DataFrame(data_numeric)
