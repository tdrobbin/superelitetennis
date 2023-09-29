import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title(':tennis: Super Elite Tennis League :tennis:')

home_tab, matches_tab, players_tab, rules_tab, stats_tab = st.tabs(['Home', 'Matches', 'Players', 'Rules', 'Stats'])

with home_tab:
    st.header('Home')
    st.markdown('Welcome to the homepage for the __super elite tennis leauge__ run by the one and only __Mike A__ (and built by the one and only __Tyler D__)')

    st.markdown('This league is only for the __most elite players__ from the tri-state area.')

    st.markdown('Winner gets his name enscribed in the entrance to the Billy Jean King Tennis Center in Queens (_one way or another_ :wink:)')

    st.markdown('GOOD LUCK AND GODSPEED GENTLEMEN.')

    st.header('Overall Leaderboard')
    df = pd.DataFrame(np.random.randn(20, 3), columns=['Rank', 'Player', 'Score']).set_index('Rank')
    st.dataframe(df, use_container_width=True)
    
    col1, col2 = st.columns(2)

    with col1:
        st.header('Singles Leaderboard')
        df = pd.DataFrame(np.random.randn(20, 3), columns=['Rank', 'Player', 'Score']).set_index('Rank')
        st.dataframe(df, use_container_width=True)
    
    with col2:
        st.header('Doubles leaderboard')
        df = pd.DataFrame(np.random.randn(20, 3), columns=['Rank', 'Player', 'Score']).set_index('Rank')
        st.dataframe(df, use_container_width=True)


with matches_tab:
    st.header('Matches')
    st.markdown('Enter completed matches below')

    st.header('Singles Match Scores')
    df = pd.DataFrame(np.random.randn(20, 7), columns=['Date', 'Player 1', 'Player 2', 'Player 1 Set 1', 'Player 2 Set 1', 'Player 1 Set 2', 'Player 2 Set 2'])
    st.dataframe(df, use_container_width=True)

    st.header('Doubles Match Scores')
    df = pd.DataFrame(np.random.randn(20, 7), columns=['Date', 'Team 1 Player A', 'Team 1 Player B', 'Team 1 Set 1', 'Team 2 Set 1', 'Team 1 Set 2', 'Team 2 Set 2'])
    st.dataframe(df, use_container_width=True)


with players_tab:
    st.header('Players')
    df = pd.DataFrame(np.random.randn(20, 5), columns=['Name', 'Hometown', 'Height', 'Handed', 'Backhand'])
    st.dataframe(df, use_container_width=True)


with rules_tab:
    st.header('Rules')

    st.markdown("""

    Matches must be played before the 28th day of the month scheduled.

    Players book the court date, time and place once agreed upon between all players. If a player/s cannot agree to play, I can offer a substitute Player if requested, if not then it's a Forfeit and points will be given to the walkover.

    Court time to be booked is 2 hours. Clay or hard court is at player's discretion.

    Balls are brought by one or both of the Players. Please discuss before you arrive to court.

    15 minute warmup (maximum). 1st to serve decided between players

    2 sets to be played. T/B to 10 points to decide.

    If 2nd set not completed by the 2hr mark. Then winner of 1st set gets 50% of match score points. Whoever has the most games in 2nd set gets 25% of match score points. If you time out in the middle of a TB, than whoever has the most points in the TB gets 25% of the match score points.

    All ball calling must be honored by both sides. If both sides are not sure of a call than receiving side loses the point. If not adhered to, match cancelled and no points for any player.

    You cannot delay time in order to win a match that is close to ending. Players must be honorable and play at normal pace to start each point. If not adhered to, match cancelled and no points will be given to any player.

    Maximum is 2 hours unless you ALL agree in advance to play to finish. Otherwise above rules apply.

    Player score

    Singles winners -20 points

    Doubles winners -10 points each player

    1st set winner -incomplete match singles -10 points doubles -5 points

    2nd set highest game count-incomplete match singles- 5points doubles -2.5 points

    Side with highest points in unfinished TB singles- 5points doubles- 2.5 points

    1st month of league (October) I will schedule all the matches based on the skill level I know of. After that (November and on) I will use highest points players and skill level to schedule matches.
    """)



    # col1, col2 = st.columns(2)

    # with col1:
    #     st.header('Singles Matches')
    #     df = pd.DataFrame(np.random.randn(20, 3), columns=['Rank', 'Player', 'Score']).set_index('Rank')
    #     st.dataframe(df, use_container_width=True)
    
    # with col2:
    #     st.header('Doubles leaderboard')
    #     df = pd.DataFrame(np.random.randn(20, 3), columns=['Rank', 'Player', 'Score']).set_index('Rank')
    #     st.dataframe(df, use_container_width=True)

