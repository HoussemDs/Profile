import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests
import json
import time
from PIL import Image
import matplotlib.pyplot as plt
import altair as alt

# Page configuration
st.set_page_config(
    page_title="My Interactive Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for animations and colors
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #FF4B4B;
        --secondary-color: #7E57C2;
        --background-color: #0E1117;
        --text-color: #FAFAFA;
        --accent-color: #00C0F2;
    }
    
    /* Animated header */
    .main-header {
        background: linear-gradient(45deg, var(--primary-color), var(--secondary-color), var(--accent-color));
        background-size: 200% 200%;
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 30px;
        animation: gradient 8s ease infinite;
        text-align: center;
    }
    
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    
    /* Card styling */
    .card {
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: rgba(255, 255, 255, 0.05);
        border-left: 5px solid var(--accent-color);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }
    
    /* Animated progress bars */
    .skill-bar {
        height: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        background-size: 200% 200%;
        animation: gradient 3s ease infinite;
    }
    
    /* Animated buttons */
    .stButton>button {
        background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
        color: white;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    }
    
    /* Animated text */
    @keyframes fadeIn {
        0% {opacity: 0; transform: translateY(20px);}
        100% {opacity: 1; transform: translateY(0);}
    }
    
    .fade-in-text {
        animation: fadeIn 1.5s ease forwards;
    }
    
    /* Section dividers */
    hr {
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color), var(--accent-color));
        height: 3px;
        border: none;
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

# Function to load Lottie animations
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Sidebar navigation
def sidebar():
    with st.sidebar:
        st.markdown("# Navigation")
        
        # Profile picture with animation
        st.markdown("""
        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <div style="width: 150px; height: 150px; border-radius: 50%; overflow: hidden; 
                 border: 3px solid #FF4B4B; animation: pulse 2s infinite;">
                <img src="https://avatars.githubusercontent.com/u/placeholder" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
        </div>
        <style>
            @keyframes pulse {
                0% {box-shadow: 0 0 0 0 rgba(255, 75, 75, 0.7);}
                70% {box-shadow: 0 0 0 15px rgba(255, 75, 75, 0);}
                100% {box-shadow: 0 0 0 0 rgba(255, 75, 75, 0);}
            }
        </style>
        """, unsafe_allow_html=True)
        
        # Navigation options with icons
        page = st.radio(
            "Go to",
            ["🏠 Home", "👨‍💻 Projects", "📊 Skills", "📝 Experience", "📞 Contact"],
            label_visibility="collapsed"
        )
        
        # Social media links with hover effects
        st.markdown("""
        <div style="display: flex; justify-content: space-around; margin-top: 30px;">
            <a href="https://github.com/" target="_blank" style="color: #FF4B4B; font-size: 24px; transition: transform 0.3s;">
                <i class="fab fa-github"></i>
            </a>
            <a href="https://linkedin.com/" target="_blank" style="color: #7E57C2; font-size: 24px; transition: transform 0.3s;">
                <i class="fab fa-linkedin"></i>
            </a>
            <a href="https://twitter.com/" target="_blank" style="color: #00C0F2; font-size: 24px; transition: transform 0.3s;">
                <i class="fab fa-twitter"></i>
            </a>
        </div>
        <style>
            a:hover {
                transform: scale(1.2);
            }
        </style>
        """, unsafe_allow_html=True)
        
        return page

# Home page
def home():
    # Animated header
    st.markdown('<div class="main-header"><h1>Welcome to My Portfolio</h1></div>', unsafe_allow_html=True)
    
    # Load and display a Lottie animation
    lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
    if lottie_coding:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_lottie(lottie_coding, height=300, key="coding")
    
    # Introduction with animated text
    st.markdown('<div class="fade-in-text">', unsafe_allow_html=True)
    st.markdown("""
    ## Hello, I'm [Your Name]! 👋
    
    I'm a data scientist and developer passionate about creating interactive visualizations and applications.
    This portfolio showcases my projects, skills, and experience in an interactive format.
    
    > "The best way to predict the future is to create it." - Abraham Lincoln
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Animated statistics
    st.markdown("### Quick Stats")
    col1, col2, col3, col4 = st.columns(4)
    
    # Function for animated counter
    def animated_counter(label, end_value, prefix="", suffix=""):
        counter_placeholder = st.empty()
        for i in range(1, end_value + 1):
            counter_placeholder.markdown(f"""
            <div style="text-align: center;">
                <h2 style="color: #FF4B4B; margin-bottom: 5px;">{prefix}{i}{suffix}</h2>
                <p>{label}</p>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.01)  # Adjust speed of animation
    
    with col1:
        animated_counter("Projects Completed", 15)
    with col2:
        animated_counter("Years Experience", 5)
    with col3:
        animated_counter("Happy Clients", 20)
    with col4:
        animated_counter("Coffee Consumed", 999, suffix="+")
    
    # Featured project with animation
    st.markdown("### Featured Project")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Create sample data for visualization
    dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
    values = np.cumsum(np.random.randn(30)) + 20
    df = pd.DataFrame({'date': dates, 'value': values})
    
    # Create an animated chart
    chart = alt.Chart(df).mark_line(
        color='#FF4B4B',
        point=alt.OverlayMarkDef(color='#7E57C2', size=100)
    ).encode(
        x='date',
        y='value',
        tooltip=['date', 'value']
    ).properties(
        width=700,
        height=400,
        title='Interactive Data Visualization'
    ).interactive()
    
    st.altair_chart(chart, use_container_width=True)
    st.markdown("**Data Visualization Dashboard**: An interactive dashboard for exploring trends and patterns in financial data.")
    st.markdown('</div>', unsafe_allow_html=True)

# Projects page
def projects():
    st.markdown('<div class="main-header"><h1>My Projects</h1></div>', unsafe_allow_html=True)
    
    # Project filters with animation
    st.markdown('<div class="fade-in-text">', unsafe_allow_html=True)
    st.markdown("### Filter Projects")
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("Category", ["All", "Data Science", "Web Development", "Machine Learning", "Visualization"])
    with col2:
        sort_by = st.selectbox("Sort By", ["Newest First", "Oldest First", "Most Popular"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project cards with animations
    st.markdown("## Project Gallery")
    
    # Function to create project cards
    def project_card(title, description, image_url=None, tags=None, link=None):
        st.markdown(f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{description}</p>
            <div style="display: flex; flex-wrap: wrap; margin-top: 10px;">
        """, unsafe_allow_html=True)
        
        if tags:
            for tag in tags:
                st.markdown(f"""
                <span style="background-color: rgba(126, 87, 194, 0.2); color: #7E57C2; 
                      padding: 5px 10px; border-radius: 15px; margin-right: 5px; margin-bottom: 5px; 
                      font-size: 0.8em;">
                    {tag}
                </span>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        if image_url:
            st.image(image_url, use_column_width=True)
        
        if link:
            st.markdown(f"""
            <a href="{link}" target="_blank" style="text-decoration: none;">
                <button style="background: linear-gradient(45deg, #FF4B4B, #7E57C2); 
                       color: white; border: none; padding: 8px 15px; 
                       border-radius: 5px; cursor: pointer; margin-top: 10px;
                       transition: all 0.3s ease;">
                    View Project
                </button>
            </a>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Display projects in a grid
    col1, col2 = st.columns(2)
    
    with col1:
        project_card(
            "Interactive Data Dashboard",
            "A comprehensive dashboard for visualizing and analyzing sales data across different regions and product categories.",
            "https://via.placeholder.com/400x200",
            ["Python", "Streamlit", "Plotly", "Data Analysis"],
            "https://github.com/"
        )
        
        project_card(
            "Natural Language Processing Tool",
            "A tool that uses NLP techniques to analyze sentiment and extract key information from customer reviews.",
            "https://via.placeholder.com/400x200",
            ["Python", "NLTK", "Transformers", "Machine Learning"],
            "https://github.com/"
        )
    
    with col2:
        project_card(
            "Predictive Analytics Model",
            "A machine learning model that predicts customer churn with 85% accuracy using historical transaction data.",
            "https://via.placeholder.com/400x200",
            ["Python", "Scikit-learn", "XGBoost", "Feature Engineering"],
            "https://github.com/"
        )
        
        project_card(
            "Interactive Web Application",
            "A full-stack web application for tracking personal fitness goals and visualizing progress over time.",
            "https://via.placeholder.com/400x200",
            ["React", "Node.js", "D3.js", "MongoDB"],
            "https://github.com/"
        )
    
    # Animated project timeline
    st.markdown("## Project Timeline")
    
    # Sample data for timeline
    timeline_data = {
        'Project': ['Project A', 'Project B', 'Project C', 'Project D', 'Project E'],
        'Start': ['2022-01', '2022-03', '2022-06', '2022-09', '2023-01'],
        'End': ['2022-03', '2022-05', '2022-08', '2022-12', '2023-03'],
        'Category': ['Data Science', 'Web Development', 'Machine Learning', 'Data Science', 'Visualization']
    }
    
    df = pd.DataFrame(timeline_data)
    
    # Convert dates to datetime
    df['Start'] = pd.to_datetime(df['Start'])
    df['End'] = pd.to_datetime(df['End'])
    
    # Create a Gantt chart
    fig = px.timeline(
        df, 
        x_start="Start", 
        x_end="End", 
        y="Project",
        color="Category",
        color_discrete_map={
            "Data Science": "#FF4B4B",
            "Web Development": "#7E57C2",
            "Machine Learning": "#00C0F2",
            "Visualization": "#FFD166"
        }
    )
    
    fig.update_layout(
        title="Project Timeline",
        xaxis_title="Date",
        yaxis_title="Project",
        legend_title="Category",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#FAFAFA")
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Skills page
def skills():
    st.markdown('<div class="main-header"><h1>My Skills</h1></div>', unsafe_allow_html=True)
    
    # Load and display a Lottie animation
    lottie_skills = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_v4isjbj5.json")
    if lottie_skills:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_lottie(lottie_skills, height=250, key="skills")
    
    # Technical skills with animated progress bars
    st.markdown("## Technical Skills")
    
    # Function to create animated skill bars
    def skill_bar(skill, percentage):
        st.markdown(f"""
        <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                <span>{skill}</span>
                <span>{percentage}%</span>
            </div>
            <div style="background-color: rgba(255, 255, 255, 0.1); border-radius: 5px; height: 10px;">
                <div class="skill-bar" style="width: {percentage}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        skill_bar("Python", 95)
        skill_bar("Data Analysis", 90)
        skill_bar("Machine Learning", 85)
        skill_bar("SQL", 80)
    
    with col2:
        skill_bar("Streamlit", 90)
        skill_bar("Data Visualization", 85)
        skill_bar("Web Development", 75)
        skill_bar("Cloud Services", 70)
    
    # Skills radar chart
    st.markdown("## Skills Overview")
    
    # Sample data for radar chart
    categories = ['Data Science', 'Programming', 'Visualization', 
                 'Machine Learning', 'Web Development', 'Database']
    values = [9, 8, 9, 8, 7, 8]
    
    # Create radar chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(255, 75, 75, 0.3)',
        line=dict(color='#FF4B4B', width=2),
        name='Skills'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        ),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#FAFAFA")
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Certifications with animation
    st.markdown("## Certifications")
    
    # Function to create certificate cards
    def certificate_card(title, issuer, date, image_url=None):
        st.markdown(f"""
        <div class="card" style="display: flex; align-items: center;">
            <div style="flex: 1;">
                <h3>{title}</h3>
                <p><strong>Issuer:</strong> {issuer}</p>
                <p><strong>Date:</strong> {date}</p>
            </div>
            <div style="flex: 0 0 100px; text-align: center;">
                <div style="width: 80px; height: 80px; background-color: #7E57C2; 
                     border-radius: 50%; display: flex; align-items: center; 
                     justify-content: center; margin: 0 auto;">
                    <span style="color: white; font-size: 30px;">🏆</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    certificate_card(
        "Data Science Professional Certificate",
        "IBM",
        "January 2023"
    )
    
    certificate_card(
        "Machine Learning Specialization",
        "Stanford Online",
        "June 2022"
    )
    
    certificate_card(
        "Full Stack Web Development",
        "Udacity",
        "December 2021"
    )

# Experience page
def experience():
    st.markdown('<div class="main-header"><h1>My Experience</h1></div>', unsafe_allow_html=True)
    
    # Animated work experience timeline
    st.markdown("## Work Experience")
    
    # Function to create experience cards
    def experience_card(title, company, period, description, color="#FF4B4B"):
        st.markdown(f"""
        <div class="card" style="border-left: 5px solid {color};">
            <h3>{title}</h3>
            <p style="color: {color}; font-weight: bold;">{company} | {period}</p>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)
    
    experience_card(
        "Senior Data Scientist",
        "Tech Innovations Inc.",
        "2021 - Present",
        """
        • Led a team of 5 data scientists in developing predictive models for customer behavior
        • Implemented machine learning pipelines that improved forecast accuracy by 35%
        • Created interactive dashboards for executive decision-making
        • Mentored junior data scientists and conducted technical workshops
        """,
        "#FF4B4B"
    )
    
    experience_card(
        "Data Analyst",
        "Data Insights Co.",
        "2018 - 2021",
        """
        • Analyzed large datasets to identify trends and patterns in customer behavior
        • Built automated reporting systems that saved 20 hours of manual work weekly
        • Collaborated with cross-functional teams to implement data-driven solutions
        • Presented findings to non-technical stakeholders
        """,
        "#7E57C2"
    )
    
    experience_card(
        "Web Developer",
        "Creative Solutions",
        "2016 - 2018",
        """
        • Developed responsive web applications using modern JavaScript frameworks
        • Implemented data visualization components for interactive user experiences
        • Collaborated with designers to create intuitive user interfaces
        • Maintained and optimized existing web applications
        """,
        "#00C0F2"
    )
    
    # Education with animation
    st.markdown("## Education")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Master of Science in Data Science</h3>
            <p style="color: #FF4B4B; font-weight: bold;">University of Data Science | 2016 - 2018</p>
            <p>Specialized in machine learning and statistical analysis. Thesis on predictive modeling for financial markets.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Bachelor of Science in Computer Science</h3>
            <p style="color: #7E57C2; font-weight: bold;">Tech University | 2012 - 2016</p>
            <p>Focused on algorithms, data structures, and software development. Graduated with honors.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Publications with animation
    st.markdown("## Publications & Talks")
    
    st.markdown("""
    <div class="card">
        <h3>"Advances in Predictive Analytics for Customer Retention"</h3>
        <p style="color: #00C0F2; font-weight: bold;">Journal of Data Science | 2022</p>
        <p>Research paper on novel approaches to predicting customer churn using machine learning techniques.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3>"Interactive Data Visualization for Business Intelligence"</h3>
        <p style="color: #00C0F2; font-weight: bold;">Data Conference | 2021</p>
        <p>Presented techniques for creating effective interactive visualizations for business stakeholders.</p>
    </div>
    """, unsafe_allow_html=True)

# Contact page
def contact():
    st.markdown('<div class="main-header"><h1>Get In Touch</h1></div>', unsafe_allow_html=True)
    
    # Load and display a Lottie animation
    lottie_contact = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_u25cckyh.json")
    if lottie_contact:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_lottie(lottie_contact, height=300, key="contact")
    
    # Contact form with animation
    st.markdown("## Send Me a Message")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Name")
        email = st.text_input("Email")
        subject = st.text_input("Subject")
    
    with col2:
        message = st.text_area("Message", height=150)
        submit = st.button("Send Message")
    
    if submit:
        st.success("Thank you for your message! I'll get back to you soon.")
        
        # Animated success message
        st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <div style="font-size: 50px; margin-bottom: 10px; animation: bounce 1s infinite;">
                ✅
            </div>
            <p>Your message has been sent successfully!</p>
        </div>
        <style>
            @keyframes bounce {
                0%, 100% {transform: translateY(0);}
                50% {transform: translateY(-20px);}
            }
        </style>
        """, unsafe_allow_html=True)
    
    # Contact information with animation
    st.markdown("## Contact Information")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card" style="text-align: center;">
            <div style="font-size: 40px; margin-bottom: 10px; color: #FF4B4B;">
                📧
            </div>
            <h3>Email</h3>
            <p>contact@example.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card" style="text-align: center;">
            <div style="font-size: 40px; margin-bottom: 10px; color: #7E57C2;">
                📱
            </div>
            <h3>Phone</h3>
            <p>+1 (123) 456-7890</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card" style="text-align: center;">
            <div style="font-size: 40px; margin-bottom: 10px; color: #00C0F2;">
                📍
            </div>
            <h3>Location</h3>
            <p>San Francisco, CA</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Availability calendar
    st.markdown("## My Availability")
    
    # Sample data for availability
    dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
    availability = np.random.choice(['Available', 'Busy', 'Limited'], size=30, p=[0.6, 0.3, 0.1])
    df = pd.DataFrame({'date': dates, 'availability': availability})
    
    # Create a color map
    color_map = {'Available': '#4CAF50', 'Busy': '#F44336', 'Limited': '#FF9800'}
    df['color'] = df['availability'].map(color_map)
    
    # Create a calendar heatmap
    fig = px.scatter(
        df,
        x=df.date.dt.day,
        y=df.date.dt.isocalendar().week,
        color='availability',
        color_discrete_map=color_map,
        size=[10] * len(df),
        hover_data=['date', 'availability']
    )
    
    fig.update_layout(
        title="January 2023 Availability",
        xaxis_title="Day of Month",
        yaxis_title="Week",
        xaxis=dict(tickmode='linear', tick0=1, dtick=1),
        yaxis=dict(autorange="reversed"),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#FAFAFA")
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Main function
def main():
    # Load Font Awesome for icons
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)
    
    # Get the current page from sidebar
    page = sidebar()
    
    # Display the appropriate page
    if page == "🏠 Home":
        home()
    elif page == "👨‍💻 Projects":
        projects()
    elif page == "📊 Skills":
        skills()
    elif page == "📝 Experience":
        experience()
    elif page == "📞 Contact":
        contact()
    
    # Footer with animation
    st.markdown("""
    <hr>
    <div style="text-align: center; padding: 20px; animation: fadeIn 1.5s ease;">
        <p>© 2023 My Portfolio. Created with Streamlit and ❤️</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()