from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


learn_data = {
  "1": {
    "id": "1",
    "title": "The Soccer Field and Basic Positions (Goalkeeper (GK)",
    "image": "/static/images/soccer_field_gk.svg",
    "description": "The last line of defense. Can use hands within the penalty area. Responsible for organizing the defense and preventing goals."
  },
  "2": {
    "id": "2",
    "title": "The Soccer Field and Basic Positions (Defenders (DEF)",
    "image": "/static/images/soccer_field_def.svg",
    "description": "Primarly focused on preventing the opposition from scoring. Includes center-backs and full-backs/wing-backs. Strong in tackling and positioning."
  },
  "3": {
    "id": "3",
    "title": "The Soccer Field and Basic Positions (Midfielders (MID)",
    "image": "/static/images/soccer_field_mid.svg",
    "description": "The engine of the team, connecting defense and attack. Responsible for ball distribution, creating chances, and sometimes defensive duties."
  },
  "4": {
    "id": "4",
    "title": "Common Soccer Formations",
    "image": "/static/images/soccer_formations.svg",
    "description": "Soccer teams use different formations based on their tactical approach. Common formations include 4-4-2, 4-3-3, 3-5-2, and 5-3-2. The numbers represent defenders-midfielders-forwards."
  },
  
  "5": {
    "id": "5",
    "title": "The Soccer Field and Basic Positions (Forwards (FWD)",
    "image": "/static/images/soccer_field_fwd.svg",
    "description": "Main goal scorers. Includes strikers and wingers. Focus on creating and finishing goal-scoring opportunities in the final third of the pitch."
  }
}
quiz_data = {
  "1": {
    "id": "1",
    "title": "Soccer Formations",
    "image": "/static/images/soccer_formations.svg",
    "question": "Which formation is shown below?",
    "answers": ["4-3-3", "4-4-2", "3-5-2","5-3-2"
    ],
    #correct index of the answers:
    "correct": 1
  },
  "2": {
    "id": "2",
    "title": "Offside Situation",
    "image": "/static/images/offside_situation.svg",
    "question": "Player A3 has the ball and is about to pass to Player A2. Will A2 be offside if they recieve the ball?",
    "answers": ["Yes, A2 will be offside", "No, A2 is not offside"],
    #correct index of the answers:
    "correct": 1
  },
  "3": {
    "id": "3",
    "title": "Player Positioning",
    "image": "/static/images/positioning_quiz.svg",
    "question": "Which player is positioned correctly for a defensive midfielder role?",
    "answers": [
      "Player A", "Player B", "Player C", "Player D"
    ],
    #correct index of the answers:
    "correct": 1
  },
  "4": {
    "id": "4",
    "title": "Field Zones",
    "image": "/static/images/field_zones.svg",
    "question": "Which zone on the field is considered the 'final third'?",
    "answers": [
      "Zone A", "Zone B", "Zone C", "Zone D"
    ],
    #correct index of the answers:
    "correct": 2
  },
  
  "5": {
    "id": "5",
    "title": "Tactical Understanding",
    "image": "/static/images/tactical_quiz.svg",
    "question": "In a counter-attack scenario, where should the wingers position themselves?",
    "answers": [
      "Deep in defense", "Wide on the flanks", "Central behind the striker", "In the midfield"
    ],
    #correct index of the answers:
    "correct": 1
  }
}
score = 0

# ROUTES


@app.route('/')
def welcome():
   return render_template('homepage.html')
 
@app.route('/results')
def add():
   return render_template('results.html', score=score)


@app.route('/learn/<my_id>')
def view(my_id=None):
    item = learn_data[my_id]
    return render_template('learn.html', item=item)
  
@app.route('/quiz/<my_id>')
def edit(my_id=None):
    item = quiz_data[my_id]
    return render_template('quiz.html', item=item)

# AJAX FUNCTIONS

#for increasing score by 1
@app.route('/score_increase', methods=['POST'])
def score_increase():
    global score
    score += 1
    return jsonify({"score": score})



if __name__ == '__main__':
   app.run(debug = True, port=5001)