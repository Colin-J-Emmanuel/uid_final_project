# UI Design Final Project

## Soccer Positioning & Offside Rules Tutorial
This project provides a web-based tutorial on soccer positions and the offside rule. It consists of a learning section where users can understand the basics of soccer positions, and a quiz section to test their knowledge.

## Features
- Interactive learning modules covering soccer positions and formations
- Visual diagrams and explanations
- Comprehensive quiz section to test knowledge
- Progress tracking throughout the tutorial
- Responsive design for mobile and desktop

## Project Structure
```
/
├── server.py            # Main Flask application
├── static/
│   ├── main.css         # CSS styles
│   ├── quiz.js          # JavaScript for quiz functionality 
│   └── images/          # SVG images for soccer positions and quiz scenarios
│       ├── field_zones.svg
│       ├── formation_4_4_2.svg
│       ├── formation_5_3_2.svg
│       ├── formation_5_4_1.svg
│       ├── offside_situation.svg
│       ├── offside.jpeg
│       ├── positioning_quiz.svg
│       ├── soccer_field_def.svg
│       ├── soccer_field_fwd.svg
│       ├── soccer_field_generic.svg
│       ├── soccer_field_gk.svg
│       ├── soccer_field_mid.svg
│       ├── soccer_formations.svg
│       └── tactical_quiz.svg
└── templates/
    ├── layout.html      # Base template
    ├── homepage.html    # Landing page
    ├── learn.html       # Learning page template
    ├── quiz.html        # Quiz page template
    └── results.html     # Quiz results page
```

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### 1. Clone the Repository
```bash
git clone https://github.com/Colin-J-Emmanuel/uid_final_project.git
cd uid_final_project
```

### 2. Create a Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Required Packages
```bash
pip install Flask
```

### 4. Create Required Directories
```bash
mkdir -p static/images
```

### 5. Add Images to Your Project
Save all the image files in the `static/images` directory with the following names:
- `field_zones.svg`
- `formation_4_4_2.svg`
- `formation_5_3_2.svg`
- `formation_5_4_1.svg`
- `offside_situation.svg`
- `offside.jpeg`
- `positioning_quiz.svg`
- `soccer_field_def.svg`
- `soccer_field_fwd.svg`
- `soccer_field_generic.svg`
- `soccer_field_gk.svg`
- `soccer_field_mid.svg`
- `soccer_formations.svg`
- `tactical_quiz.svg`

### 6. Run the Application
```bash
python server.py
```

### 7. Access the Application
Open your web browser and visit: `http://localhost:5001`

## Usage

1. The application flow starts at the homepage with a "Start" button
2. Users proceed through the learning modules about soccer positions
3. After completing the learning section, users can take a quiz to test their knowledge
4. The quiz tracks correct answers and displays a final score at the end

## Quiz Structure
The quiz asks questions about:
- Soccer formations
- Offside rules
- Player positioning
- Field zones
- Tactical scenarios

Correct answers increment the score, which is displayed at the end of the quiz.

## Technologies Used
- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5
- **Icons**: Font Awesome
- **Templating**: Jinja2

## Contributing
If you'd like to contribute to this project:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License
This project is open source and available under the MIT License.

## Contact
For questions or suggestions, please open an issue on the GitHub repository.