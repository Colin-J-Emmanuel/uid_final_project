UI Design Final Project

Soccer Positioning & Offside Rules Tutorial
This project provides a web-based tutorial on soccer positions and the offside rule. It consists of a learning section where users can understand the basics of soccer positions, and a quiz section to test their knowledge.
Project Structure
/
├── server.py            # Main Flask application
├── static/
│   ├── main.css         # CSS styles
│   ├── quiz.js          # JavaScript for quiz functionality 
│   └── images/          # SVG images for soccer positions and quiz scenarios
│       ├── soccer_field_gk.svg
│       ├── soccer_field_def.svg
│       ├── soccer_field_mid.svg
│       ├── soccer_field_fwd.svg
│       ├── soccer_formations.svg
│       ├── formation_quiz.svg
│       ├── offside_situation.svg
│       ├── positioning_quiz.svg
│       ├── field_zones.svg
│       └── tactical_quiz.svg
└── templates/
    ├── layout.html      # Base template
    ├── homepage.html    # Landing page
    ├── learn.html       # Learning page template
    ├── quiz.html        # Quiz page template
    └── results.html     # Quiz results page
Setup Instructions

Make sure you have Python and Flask installed
Create a static/images directory and save all SVG files there
Run the application with:
python server.py

Visit http://localhost:5001 in your browser

Usage

The application flow starts at the homepage with a "Start" button
Users proceed through the learning modules about soccer positions
After completing the learning section, users can take a quiz to test their knowledge
The quiz tracks correct answers and displays a final score at the end

Adding Images to Your Project

Create a static/images directory if it doesn't exist:
mkdir -p static/images

Save all the SVG files in this directory with the names specified in server.py:

soccer_field_gk.svg
soccer_field_def.svg
soccer_field_mid.svg
soccer_field_fwd.svg
soccer_formations.svg
formation_quiz.svg
offside_situation.svg
positioning_quiz.svg
field_zones.svg
tactical_quiz.svg


Make sure the image paths in server.py match where you saved the files

Quiz Structure
The quiz asks questions about:

Soccer formations
Offside rules
Player positioning
Field zones
Tactical scenarios

Correct answers increment the score, which is displayed at the end of the quiz.
