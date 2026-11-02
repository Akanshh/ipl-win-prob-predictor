# 🏏 IPL Win Predictor

A machine learning web app that predicts the live win probability of an IPL team during a run chase.

🔗 **Live app:** https://ipl-win-predictor20.streamlit.app

> If the app is asleep, click **"Yes, get this app back up!"** and wait about a minute.

## How it works

You enter the match situation, and the model returns the win and loss probability for both teams.

**Inputs:**
- Batting team and bowling team
- Host city
- Target score
- Current score
- Overs completed
- Wickets fallen

**Features calculated from the inputs:**
- Runs left
- Balls left
- Wickets remaining
- Current run rate (CRR)
- Required run rate (RRR)

## Tech stack

- Python
- Pandas, NumPy
- Scikit-learn pipeline with [Logistic Regression]
- Streamlit (UI and deployment)

## Run locally

```bash
git clone https://github.com/Akanshh/ipl-win-prob-predictor.git
cd ipl-win-prob-predictor
pip install -r requirements.txt
streamlit run app.py
```

## Project files

- `app.py`: Streamlit app
- `pipe.pkl`: trained model pipeline
- `requirements.txt`: dependencies

## Dataset

IPL match and ball-by-ball data [Kaggle].

## Author

**Akansh Gangwar**
B.Tech CSE (AI & ML), GRD-IMT Dehradun
[LinkedIn:https://www.linkedin.com/in/akansh-gangwar-221559400?utm_source=share_via&utm_content=profile&utm_medium=member_ios]
