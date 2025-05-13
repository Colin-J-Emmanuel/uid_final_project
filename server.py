from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from markupsafe import Markup
import re

app = Flask(__name__)

# Custom filter to convert newlines to HTML line breaks
def nl2br(value):
    if not value:
        return value
    # Convert newlines to <br> tags, handle different line endings
    value = value.replace('\r\n', '<br>').replace('\r', '<br>').replace('\n', '<br>')
    # Convert markdown-style bullet points to HTML
    value = re.sub(r'•\s*(.*?)(?=<br>|$)', r'&bull; \1', value)
    # Convert markdown-style bold text **text** to <strong>text</strong>
    value = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', value)
    return Markup(value)

# Register the custom filter
app.jinja_env.filters['nl2br'] = nl2br


learn_data = {
  "1": {
    "id": "1",
    "title": "The Soccer Field and Basic Positions (Goalkeeper (GK))",
    "image": "/static/images/soccer_field_gk.svg",
    "description": "The last line of defense. Can use hands within the penalty area. Responsible for organizing the defense and preventing goals."
  },
  "2": {
    "id": "2",
    "title": "The Soccer Field and Basic Positions (Defenders (DEF))",
    "image": "/static/images/soccer_field_def.svg",
    "description": "Primarly focused on preventing the opposition from scoring. Includes center-backs and full-backs/wing-backs. Strong in tackling and positioning."
  },
  "3": {
    "id": "3",
    "title": "The Soccer Field and Basic Positions (Midfielders (MID))",
    "image": "/static/images/soccer_field_mid.svg",
    "description": "The engine of the team, connecting defense and attack. Responsible for ball distribution, creating chances, and sometimes defensive duties."
  },
  "4": {
    "id": "4",
    "title": "The Soccer Field and Basic Positions (Forwards (FWD))",
    "image": "/static/images/soccer_field_fwd.svg",
    "description": "Main goal scorers. Includes strikers and wingers. Focus on creating and finishing goal-scoring opportunities in the final third of the pitch."
  },
  "5": {
    "id": "5",
    "title": "Introduction to Soccer Formations",
    "image": "/static/images/soccer_field_generic.svg",
    "description": "Soccer formations define how players are positioned on the field. Each formation has its own tactical advantages and is chosen based on the team's strategy and the opposition they're facing."
  },
  "6": {
    "id": "6",
    "title": "The 4-4-2 Formation",
    "image": "/static/images/formation_4_4_2.svg",
    "description": "The 4-4-2 soccer formation is a classic setup with four defenders, four midfielders, and two forwards. It's known for its balance, allowing teams to adapt to both attacking and defensive situations.",
    "detailed_description": """
Detailed Breakdown:
• **Defenders:**
  - **Two Center-backs:** Coordinate the defense and are responsible for defending the area in front of the box.
  - **Two Full-backs:** Provide width on the flanks, overlapping with midfielders in attack and dropping back to defend when necessary.
• **Midfielders:**
  - **Defensive Midfielder:** Acts as the anchor in the midfield, protecting the back four and breaking up opposition attacks.
  - **Two Central Midfielders:** Control the tempo of the game, distribute the ball, and provide support to both attack and defense.
  - **Attacking Midfielder:** Operates in the half-space, linking play between midfield and attack, and creating chances for the forwards.
• **Forwards:**
  - **Two Strikers:** One may play as a target man, holding up play and linking with the midfielders, while the other may operate off the target man, cutting in from the wings or taking advantage of spaces in the box.
""",
    "advantages_disadvantages": """
**Advantages of 4-4-2:**
• **Balanced Structure:** Offers a good balance between defense and attack, allowing teams to be solid defensively while also having sufficient numbers in attack.
• **Flexibility:** Can be adapted to different playing styles, from controlling possession to counter-attacking.
• **Compact Defensive Shape:** The formation naturally creates a compact defensive shape, making it difficult for opponents to penetrate the back four.

**Potential Weaknesses:**
• **Midfield Overrun:** The two central midfielders may struggle to control the midfield against a three-man midfield.
• **Wide Midfielders:** The wide midfielders need to be able to quickly mount counter-attacks and carry the ball forward with pace.
• **Stamina:** The roles of wide midfielders and one of the strikers can be strenuous, requiring them to contribute defensively and then push forward, potentially leading to a decline in stamina as the game progresses.
"""
  },
  "7": {
    "id": "7",
    "title": "The 5-4-1 Formation",
    "image": "/static/images/formation_5_4_1.svg",
    "description": "The 5-4-1 soccer formation is a defensive-oriented setup with five defenders, four midfielders, and one striker. It emphasizes defensive solidity, midfield dominance, and counter-attacking opportunities.",
    "detailed_description": """
**Detailed Description:**
• **Defenders:** The five defenders form a solid backline, typically with three center backs and two fullbacks. The fullbacks often play a crucial role in both defending and supporting attacks, potentially overlapping or tucking inside to create passing options.
• **Midfielders:** The four midfielders are organized in a diamond shape, providing a strong presence in the center of the field. This allows for control of the ball, quick transitions, and effective counter-attacks.
• **Forward:** The lone striker acts as the primary attacking point, receiving passes and creating opportunities to score.
""",
    "advantages_disadvantages": """
**Strategic Benefits:**
• **Defensive Stability:** The five-man defense is highly effective at preventing opposition attacks and creating a strong defensive wall.
• **Midfield Dominance:** The four midfielders allow for effective control of the ball and passing options, enabling the team to dictate the pace of the game.
• **Counter-attacking:** The formation allows for quick transitions from defense to attack, utilizing the midfield and the lone striker to capitalize on counter-attacking opportunities.

**Variations and Adaptations:**
• **Attacking Fullbacks:** The fullbacks can move forward to create attacking opportunities, shifting the formation to resemble a 3-6-1 when attacking.
• **Fluid Midfield:** The midfield can be flexible, with players moving into the half-space or stretching the play to create space for counter-attacks.
• **"False 9" or Two Strikers:** In some cases, a "false 9" player may be utilized, moving between midfield and forward, or a team may choose to play with two strikers to increase attacking threat.
"""
  },
  "8": {
    "id": "8",
    "title": "The 5-3-2 Formation",
    "image": "/static/images/formation_5_3_2.svg",
    "description": "The 5-3-2 soccer formation is a defensive-minded setup with a focus on solidifying the back line and creating counter-attacking opportunities. It features five defenders, three central midfielders, and two strikers.",
    "detailed_description": """
**Detailed Description:**
• **Back Line:** The back five is comprised of three center backs and two wing-backs, who are essentially fullbacks with the freedom to push forward and support the attack.
• **Midfield:** The midfield is usually a tight unit of three, often with a double pivot (two defensive midfielders) to provide solidity and cover for the back line, and one central attacking midfielder with more creative responsibilities.
• **Attack:** The two strikers operate at the front, providing a direct attacking threat and the ability to exploit spaces left by the opposition during counter-attacks.
""",
    "advantages_disadvantages": """
**Key Characteristics:**
• **Defensive Focus:** The formation prioritizes defensive solidity, with the back five and midfield three creating a strong defensive core.
• **Counter-Attacking:** The 5-3-2 is well-suited for teams that want to maintain a strong defensive base while being ready to exploit counter-attacking opportunities.
• **Flexibility:** While primarily defensive, the 5-3-2 can be adapted to be more attacking by pushing the wing-backs higher and using more offensive-minded midfielders.

**Key Considerations:**
• **Wing-backs:** The performance of the wing-backs is crucial. They must be able to provide width and support the attack, while also being able to quickly drop back and defend.
• **Midfield:** The midfield's role is crucial for controlling the game, dictating the pace, and providing a link between defense and attack.
• **Strikers:** The strikers should be able to exploit the spaces left by the opposition and create scoring opportunities.
"""
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
    global score
    # Reset score when starting the quiz (question 1)
    if my_id == "1":
        score = 0
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