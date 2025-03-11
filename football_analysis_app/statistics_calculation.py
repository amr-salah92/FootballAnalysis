import pandas as pd

def calculate_statistics(analysis_results):
    statistics = {
        'summary': {},
        'defensive': {},
        'offensive': {},
        'passing': {},
        'expected_goals': {},
        'shots': {},
        'tackles': {},
        'saves': {},
        'goals': {},
        'dribbles': {},
        'possession_lost': {},
        'aerial_battles': {},
        'passes': {},
        'key_passes': {},
        'assists': {}
    }
    
    # Example data - replace with actual analysis results processing
    total_minutes = 90 * 10  # Example: 90 minutes per game, 10 games
    statistics['summary'] = {
        'Apps': 10,
        'Mins': total_minutes,
        'Goals': 5,
        'Assists': 3,
        'Yel': 2,
        'Red': 0,
        'SpG': 3.5,
        'PS%': 85.2,
        'AerialsWon': 15,
        'MotM': 2,
        'Rating': 7.8
    }
    statistics['defensive'] = {
        'Tackles': 20,
        'Interceptions': 10,
        'Fouls': 5,
        'Offsides': 3,
        'Clearances': 8,
        'Dribbles': 12,
        'Blocks': 4,
        'Own Goals': 1
    }
    statistics['offensive'] = {
        'Goals': 5,
        'Assists': 3,
        'Shots per Game': 3.5,
        'Key Passes': 7,
        'Dribbles': 12,
        'Fouled': 4,
        'Offsides': 3,
        'Dispossessed': 6,
        'Unsuccessful Touches': 5
    }
    statistics['passing'] = {
        'Assists': 3,
        'Key Passes': 7,
        'Average Passes per Game': 50,
        'Pass Success Percentage': 85.2,
        'Crosses': 10,
        'Long Balls': 8,
        'Through Balls': 5
    }
    statistics['expected_goals'] = {
        'xG': 4.5,
        'Goals': 5,
        'xG Difference': 0.5,
        'xG per 90 minutes': 0.45,
        'Shots': 35,
        'xG per Shot': 0.13
    }
    statistics['shots'] = {
        'Total': 35,
        'Out of Box': 10,
        'Six Yard Box': 5,
        'Penalty Area': 20,
        'Off Target': 15,
        'On Post': 2,
        'On Target': 18,
        'Blocked': 6,
        'Open Play': 25,
        'Counter': 5,
        'Set Piece': 3,
        'Penalty Taken': 2,
        'Right Foot': 20,
        'Left Foot': 10,
        'Head': 5,
        'Other': 0
    }
    statistics['tackles'] = {
        'Total Tackles': 20,
        'Dribbled Past': 5,
        'Total Attempted Tackles': 25,
        'Total Interceptions': 10,
        'Fouled': 4,
        'Fouls': 5,
        'Caught Offside': 3,
        'Total Clearances': 8,
        'Shots Blocked': 6,
        'Crosses Blocked': 4,
        'Passes Blocked': 5
    }
    statistics['saves'] = {
        'Total': 10,
        'Six Yard Box': 3,
        'Penalty Area': 5,
        'Out of Box': 2
    }
    statistics['goals'] = {
        'Open Play': 3,
        'Counter Attack': 1,
        'Set Piece': 1,
        'Penalty Scored': 2,
        'Own Goal': 1,
        'Normal': 4,
        'Right Foot': 3,
        'Left Foot': 1,
        'Head': 1,
        'Other': 0
    }
    statistics['dribbles'] = {
        'Unsuccessful': 5,
        'Successful': 12,
        'Total Dribbles': 17
    }
    statistics['possession_lost'] = {
        'Unsuccessful Touches': 5,
        'Dispossessed': 6
    }
    statistics['aerial_battles'] = {
        'Total': 20,
        'Won': 15,
        'Lost': 5
    }
    statistics['passes'] = {
        'Accurate Crosses': 8,
        'Inaccurate Crosses': 2,
        'Accurate Corners': 3,
        'Inaccurate Corners': 1,
        'Accurate Free Kicks': 4,
        'Inaccurate Free Kicks': 1,
        'Accurate Long Balls': 7,
        'Inaccurate Long Balls': 1,
        'Accurate Short Passes': 45,
        'Inaccurate Short Passes': 5
    }
    statistics['key_passes'] = {
        'Total': 7,
        'Long': 2,
        'Short': 3,
        'Cross': 1,
        'Corner': 1,
        'Through Ball': 2,
        'Free Kick': 1,
        'Throwin': 0,
        'Other': 0
    }
    statistics['assists'] = {
        'Cross': 2,
        'Corner': 1,
        'Through Ball': 1,
        'Free Kick': 1,
        'Throwin': 0,
        'Other': 0,
        'Total Assists': 3
    }
    
    return statistics