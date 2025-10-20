import os
import json
import logging
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Personal Information
PERSONAL_INFO = {
    "name": "Houssem Eddine",
    "title": "AI Engineer | Data Scientist",
    "location": "El Menzah 6, Ariana, Tunisia",
    "email": "houssemeddineds@gmail.com",
    "phone": "+216 46210801",
    "linkedin": "https://www.linkedin.com/in/houssemeddineds/",
    "github": "https://github.com/HoussemDs",
    "summary": "AI Engineer specializing in medical imaging, geospatial intelligence, and agentic AI. Experienced in building and deploying real-world systems with Python, PyTorch, MONAI, LangChain, and LangGraph. Proven track record in developing 3D segmentation pipelines, AI-driven diagnostics, and intelligent automation across healthcare and enterprise applications."
}

# Load project data from JSON file
def load_projects():
    try:
        with open('data/projects.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error loading projects: {e}")
        # Return default projects if file not found or invalid
        return [
            {
                "id": 1,
                "title": "AI Image Classification Model",
                "description": "A deep learning model that classifies images using a custom CNN architecture with PyTorch.",
                "image": "img/project1.jpg",
                "tags": ["Deep Learning", "PyTorch", "Computer Vision"],
                "github_url": "https://github.com/alex/image-classifier",
                "demo_url": "",
                "youtube_id": "dQw4w9WgXcQ"  # Example YouTube video ID
            },
            {
                "id": 2,
                "title": "Interactive Data Visualization Dashboard",
                "description": "A Plotly Dash application that visualizes complex datasets with interactive elements.",
                "image": "img/project2.jpg",
                "tags": ["Data Visualization", "Plotly", "Dash", "Python"],
                "github_url": "https://github.com/alex/data-viz-dashboard",
                "demo_url": "https://data-viz-demo.herokuapp.com",
                "youtube_id": ""
            },
            {
                "id": 3,
                "title": "NLP Text Classification System",
                "description": "A natural language processing system that categorizes text using transformer models.",
                "image": "img/project3.jpg",
                "tags": ["NLP", "Transformers", "HuggingFace", "BERT"],
                "github_url": "https://github.com/alex/nlp-classifier",
                "demo_url": "",
                "youtube_id": ""
            }
        ]

# Routes
@app.route('/')
def home():
    projects_data = load_projects()
    return render_template('index.html', projects=projects_data, personal=PERSONAL_INFO)

@app.route('/projects')
def projects():
    projects_data = load_projects()
    return render_template('projects.html', projects=projects_data, personal=PERSONAL_INFO)

@app.route('/contact')
def contact():
    return render_template('contact.html', personal=PERSONAL_INFO)

# API Endpoints
@app.route('/api/contact', methods=['POST'])
def api_contact():
    data = request.json
    
    # Validate required fields
    required_fields = ['name', 'email', 'message']
    for field in required_fields:
        if field not in data or not data[field].strip():
            return jsonify({
                'success': False,
                'message': f'Missing required field: {field}'
            }), 400
    
    # Log the contact form submission (in a real app, you might save to a database or send an email)
    logger.info(f"Contact form submission: {data['name']} ({data['email']}): {data['message']}")
    
    return jsonify({
        'success': True,
        'message': 'Thank you for your message, I\'ll reach out soon!'
    })

# Example of how another API endpoint could be added
@app.route('/api/predict', methods=['POST'])
def api_predict():
    # This is just a placeholder to demonstrate how additional API endpoints could be added
    return jsonify({
        'success': True,
        'message': 'This is a placeholder for a future ML prediction API endpoint.',
        'prediction': 'Sample prediction result'
    })

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Ensure directories exist
    os.makedirs('static/img', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    
    # Create projects.json if it doesn't exist
    if not os.path.exists('data/projects.json'):
        with open('data/projects.json', 'w') as f:
            json.dump(load_projects(), f, indent=4)
    
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))