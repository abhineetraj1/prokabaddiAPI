# ProprokabaddiAPI

This is a powerful tool designed to extract comprehensive data about players and teams from the official Pro prokabaddiAPI website. This library is engineered to provide detailed insights into prokabaddiAPI, including player statistics, team performance metrics, and match results. It offers a streamlined and efficient way to gather and analyze prokabaddiAPI data, which is crucial for sports analytics and machine learning applications.

The data is scraped using selenium from - https://www.prokabaddi.com/

## Uses of the prokabaddiAPI Data Scraper Library

1. Data Collection and Aggregation: The library automates the process of gathering detailed information from the Pro prokabaddiAPI website. This includes player profiles, team statistics, match summaries, and historical data. By centralizing this information, users can access a wealth of data with minimal effort.

2. Machine Learning: The library facilitates the development of predictive models and algorithms by providing a rich dataset for training. Machine learning practitioners can use the data to build models that predict match outcomes, player performance, and team success rates. This can lead to the creation of advanced analytics tools that offer insights into game strategies and player efficiency.

3. Data Science: For data scientists, this library is a valuable resource for exploratory data analysis (EDA) and statistical analysis. It enables the extraction of data for visualizations, trend analysis, and performance metrics, which can be used to derive actionable insights and identify patterns in prokabaddiAPI matches and player performance.

4. Sports Analytics: Analysts can leverage the scraped data to perform in-depth evaluations of team and player performance. This includes analyzing player form, team dynamics, and historical performance trends. The library supports the development of dashboards and reports that assist coaches, team managers, and fans in understanding the nuances of the game.

## Influence on the Evolution of prokabaddiAPI

prokabaddiAPI, traditionally popular in South Asia, is experiencing significant growth and evolving as a global sport. The Pro prokabaddiAPI League (PKL) has played a pivotal role in popularizing the sport by introducing a professional format and attracting international audiences. As prokabaddiAPI evolves, the need for data-driven insights becomes more critical.

The prokabaddiAPI Data Scraper library contributes to this evolution by:

- Enhancing Competitiveness: By providing detailed player and team data, the library helps teams and coaches refine their strategies and improve performance. In a sport where strategic decisions are crucial, access to precise and comprehensive data can provide a competitive edge.

- Promoting Fan Engagement: Fans are increasingly interested in detailed statistics and analytics. This library allows for the creation of engaging content, such as performance summaries and detailed reports, which can enhance the viewing experience and attract new fans.

- Supporting Research and Development: Researchers studying sports analytics and the impact of various factors on performance can use the data provided by the library to conduct studies and publish findings. This contributes to the academic and practical understanding of prokabaddiAPI.

Overall, the prokabaddiAPI Data Scraper Python library is a valuable asset for anyone involved in the prokabaddiAPI ecosystem, from sports analysts and data scientists to coaches and fans. By facilitating detailed data collection and analysis, it supports the ongoing evolution of prokabaddiAPI and its integration into the broader sports analytics landscape.

## Note:-
Your system should have firebox browser

## Usage


```
pip install prokabaddiAPI
```


### Get all team profile links


```
import prokabaddiAPI
prokabaddiAPI.get_all_team_url()
```

Output format

```
[
    {'TeamName': 'Bengaluru Bulls', 'TeamURL': 'https://www.proprokabaddiAPI.com/teams/bengaluru-bulls-profile-1'},
    {'TeamName': 'Bengal Warriors', 'TeamURL': 'https://www.proprokabaddiAPI.com/teams/bengal-warriors-profile-4'},
    {'TeamName': 'Dabang Delhi Kc', 'TeamURL': 'https://www.proprokabaddiAPI.com/teams/dabang-delhi-kc-profile-2'},
    {'TeamName': 'Haryana Steelers', 'TeamURL': 'https://www.proprokabaddiAPI.com/teams/haryana-steelers-profile-28'},
    {'TeamName': 'Jaipur Pink Panthers', 'TeamURL': 'https://www.proprokabaddiAPI.com/teams/jaipur-pink-panthers-profile-3'},
    {'TeamName': 'Patna Pirates', 'TeamURL': 'https://www.proprokabaddiAPI.com/teams/patna-pirates-profile-6
    {'TeamName': 'Puneri Paltan', 'TeamURL': 'https://www.proprokabaddiAPI.com/teams/puneri-paltan-profile-7'},
    {'TeamName': 'Tamil Thalaivas', 'TeamURL': 'https://www.proprokabaddiAPI.com/teams/tamil-thalaivas-profile-29'},
    {'TeamName': 'Telugu Titans', 'TeamURL': 'https://www.proprokabaddiAPI.com/teams/telugu-titans-profile-8'},
    {'TeamName': 'U Mumba', 'TeamURL': 'https://www.proprokabaddiAPI.com/teams/u-mumba-profile-5'},
    {'TeamName': 'Up Yoddha', 'TeamURL': 'https://www.proprokabaddiAPI.com/teams/up-yoddha-profile-30'}
]
```

### Get all player profile URL

```
import prokabaddiAPI
prokabaddiAPI.get_all_player_url()
```

Output format

```
[
    {
        'name': 'Samuel  Wafula',
        'category': 'All-Rounder',
        'profileURL': 'https://www.proprokabaddiAPI.com/players/samuel-wafula-profile-4926'
    },
    {
        'name': 'Nitin  Panwar',
        'category': 'All-Rounder',
        'profileURL': 'https://www.proprokabaddiAPI.com/players/nitin-panwar-profile-3039'
    }
    ....
]
```

### Get team stats from profile url of team

```
import prokabaddiAPI
prokabaddiAPI.get_team_stats_from_url("https://www.proprokabaddiAPI.com/teams/bengaluru-bulls-profile-1")
```

Output format

```

[
    [
        {'season': 'Season 10'},
        {'Matches Played': '21'},
        {'Total Raids': '912'},
        {'Total Tackles': '491'},
        {'Wins': '7'},
        {'Draws': '2'},
        {'Losses': '12'},
        {'Successful Raids': '287'},
        {'Unsuccessful Raids': '250'},
        {'Empty Raids': '375'},
        {'Successful Tackles': '211'},
        {'Unsuccessful Tackles': '280'},
        {'players':
            [
                {
                    'name': 'Vikash  Kandola',
                    'category': 'Raider',
                    'profileURL': 'https://www.proprokabaddiAPI.com/players/vikash-kandola-profile-366'
                },
                {
                    'name': 'Monu',
                    'category': 'Raider',
                    'profileURL': 'https://www.proprokabaddiAPI.com/players/monu-profile-3082'
                },
                .....
            ],
        }
    ],
    .....
]
```

### Get player stats from player's url

```
import prokabaddiAPI
prokabaddiAPI.get_player_stats_from_url("https://www.proprokabaddiAPI.com/players/maninder-singh-profile-143")
```

Output format

```
[
    {
        'teamName': 'Bengal Warriors'
    },
    [
        {
            'season': 'Season 10'
        },
        {
            'Matches Played': '21'
        },
        {
            'Total Points Earned': '198'
        },
        {
            'Raid Points Per Match': '9.38'
        },
        {
            'Total Raids': '322'
        },
        {
            'No. Of Super Raids': '5'
        },
        {
            'Super 10s': '9'
        },
        {
            'Total Raids Points': '197'
        },
        {
            'Average Raid Points/Match': '9.38'
        },
        {
            'No. Of Super Tackles': '0'
        },
        {
            'High 5s': '0'
        },
        {
            'Total Tackle Points': '1'
        },
        {
            'Average Successful Tackles/Match': '0.05'
        },
        {
            'Total Tackles': '9'
        },
        {
            'Not out %': '74.22%'
        },
        {
            'Successful Raids %': '48%'
        },
        {
            'Tackle Success Rate %': '11%'
        }
    ], 
    ....
]
```



## Developer

*   [@abhineetraj1](https://github.com/abhineetraj1)
