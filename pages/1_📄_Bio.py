import streamlit as st

# Page config
st.set_page_config(page_title="Bio", page_icon="📄", layout="wide")

st.title("📄 About Me")

# Professional Summary
st.markdown("## Professional Summary")

col1, col2 = st.columns([1, 2])

with col1:
    # Optional: Add your profile photo
    # st.image("assets/profile_photo.jpg", caption="Your Name", width=200)
    st.markdown("### Contact")
    st.write("📧 **Email:** ngroshek@msudenver.edu")
    st.write("💼 **LinkedIn:** [Your LinkedIn](https://linkedin.com/in/yourprofile)")
    st.write("🐙 **GitHub:** [Your GitHub](https://github.com/Grosh024)")

with col2:
    st.write("""
    I'm an undergraduate student at MSU Denver pursuing a degree in Computer Science with a focus 
    on Data Science and Machine Learning. I'm passionate about using data visualization and 
    predictive modeling to uncover insights from complex datasets. My interests span financial 
    markets, time-series forecasting, and building interactive web applications that make data 
    accessible and insightful.
    
    This portfolio showcases my ability to perform exploratory data analysis, create meaningful 
    visualizations, and build interactive dashboards using modern data science tools.
    """)

st.markdown("---")

# Highlights
st.markdown("## 🌟 Highlights")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎓 Education")
    st.write("**MSU Denver** - Data Science")
    st.write("- Relevant Coursework:")
    st.write("  - Data Science & Visualization")
    st.write("  - Machine Learning")
    st.write("  - Software Development Methods")

with col2:
    st.markdown("### 🛠️ Technical Skills")
    st.write("**Languages & Tools:**")
    st.write("- Python (pandas, NumPy, scikit-learn)")
    st.write("- Data Viz (Plotly, Matplotlib, Seaborn)")
    st.write("- Web Apps (Streamlit)")
    st.write("- Version Control (Git, GitHub)")

with col3:
    st.markdown("### 📊 Projects")
    st.write("- S&P 500 Stock Analysis (this app)")
    st.write("- Cryptocurrency Price Prediction")
    st.write("- Machine Learning Model Selection")

st.markdown("---")

# Visualization Philosophy
st.markdown("## 🎨 My Data Visualization Philosophy")

st.write("""
I believe effective data visualization should be:

1. **Clear and Accessible** - Charts should be easy to understand at a glance, with proper labels, 
   legends, and explanations that guide the viewer.

2. **Honest and Ethical** - Visualizations must accurately represent the data without misleading scales, 
   cherry-picked ranges, or deceptive visual encodings. When working with data about people, 
   I acknowledge limitations and potential biases.

3. **Interactive and Engaging** - Modern tools like Streamlit and Plotly enable viewers to explore 
   data themselves, filtering and drilling down to discover their own insights.

4. **Purposeful** - Every chart should answer a specific question or support a clear analytical goal. 
   Visualization is a tool for understanding, not just decoration.

5. **Inclusive** - I use color-blind-safe palettes, provide text alternatives, and ensure sufficient 
   contrast so that visualizations are accessible to all users.
""")

st.markdown("---")

# Personal Interests (Optional)
st.markdown("## Personal Hobbies & Interests")

st.write("""
When I'm not digging into data or on my computer, you'll find me:
- Skiing and snowboarding in Colorado's mountains
- Hiking and exploring outdoor trails
- On the golf course.
""")

st.markdown("---")

st.caption("📄 Professional Bio | S&P 500 Portfolio App")
