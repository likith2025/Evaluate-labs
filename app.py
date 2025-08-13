from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'  # Change this in production

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for projects page
@app.route('/projects')
def projects():
    # Sample projects data - replace with your actual projects
    projects = [
        {
            'title': 'E-commerce Website',
            'description': 'A full-stack e-commerce platform built with Flask and SQLite.',
            'technologies': ['Python', 'Flask', 'SQLite', 'HTML/CSS', 'JavaScript'],
            'github_link': 'https://github.com/likith2025?tab=repositories'
        },
        {
            'title': 'Data Analytics Dashboard',
            'description': 'Interactive dashboard for visualizing sales data using Python and Plotly.',
            'technologies': ['Python', 'Pandas', 'Plotly', 'Flask'],
            'github_link': 'https://github.com/yourusername/analytics-dashboard'
        },
        {
            'title': 'Task Management API',
            'description': 'RESTful API for task management with user authentication.',
            'technologies': ['Python', 'Flask', 'JWT', 'PostgreSQL'],
            'github_link': 'https://github.com/yourusername/task-api'
        }
    ]
    return render_template('projects.html', projects=projects)

# Route for contact page (GET and POST)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic validation
        if not name or not email or not message:
            flash('Please fill in all fields.', 'error')
            return render_template('contact.html')
        
        # In a real application, you would:
        # 1. Save to database
        # 2. Send email notification
        # 3. Implement proper validation
        
        # For now, just show a success message
        flash(f'Thank you, {name}! Your message has been sent successfully.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)