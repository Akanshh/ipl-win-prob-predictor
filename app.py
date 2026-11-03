import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
         'Mumbai Indians',
         'Royal Challengers Bangalore',
         'Kolkata Knight Riders',
         'Kings XI Punjab',
         'Chennai Super Kings',
         'Rajasthan Royals',
         'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore',
          'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur',
          'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
          'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Dharamsala', 'Pune',
          'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah',
          'Cuttack', 'Visakhapatnam', 'Mohali',
          'Bengaluru']

pipe = pickle.load(open('pipe.pkl', 'rb'))
st.title("IPL Win Predictor")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("select batting team", sorted(teams))
with col2:
    bowling_team = st.selectbox("select bowling team", sorted(teams))

selected_city = st.selectbox('select host city', sorted(cities))

target = st.number_input("Target", min_value=0.0)

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('score', min_value=0.0)

with col4:
    overs = st.number_input('overs_completed', min_value=0.0, max_value=20.0)
with col5:
    wickets = st.number_input('wickets', min_value=0.0, max_value=10.0)


if st.button('predict_probability'):
    if batting_team == bowling_team:
        st.warning("Batting team and bowling team must be different.")
    elif target <= 0:
        st.warning("Please enter a target greater than 0.")
    elif overs <= 0:
        st.warning("Overs completed must be greater than 0.")
    elif score > target:
        st.success(batting_team + " has won the match! 🎉")
    elif overs >= 20 or wickets >= 10:
        # innings is over, so show the final result
        if score == target:
            st.info("Match tied! It goes to a Super Over. 🤝")
        else:
            st.error(bowling_team + " has won the match! 🎉")
    else:
        runs_left = target - score
        balls_left = 120 - (overs) * 6
        wickets = 10 - wickets
        crr = score / overs
        rrr = (runs_left * 6) / balls_left

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        st.header(batting_team + "-" + str(round(win * 100)) + "%")
        st.header(bowling_team + "-" + str(round(loss * 100)) + "%")
