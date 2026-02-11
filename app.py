import streamlit as st

# -------- PAGE CONFIG --------
st.set_page_config(
    page_title="Robin Jain",
    page_icon="🦞",
    layout="centered"
)

# -------- CUSTOM STYLING  --------
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top, #121826 0%, #0b0f14 55%);
        color: white !important;
    }

    .main .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 1000px !important;
    }

    /* Hero */
    .hero-container {
        text-align: center;
        padding: 1rem 0 1.8rem 0;
    }

    .big-title {
        font-size: 76px;
        font-weight: 800;
        background: linear-gradient(90deg, #ff8a5c, #ff3b5c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
        transition: transform 0.2s;
    }

    .big-title:hover {
        transform: translateY(-3px);
    }

    .lobster {
        font-size: 70px;
        margin-left: 8px;
        vertical-align: middle;
    }

    .subtitle {
        font-size: 21px;
        letter-spacing: 0.3px;
        color: #cfcfcf;
        margin: 0.6rem 0 0.4rem;
    }

    .highlight {
        color: #ffb703;
        font-weight: 600;
    }

    .tagline {
        font-size: 17px;
        color: #a8a8a8;
        margin-top: 0.8rem;
        line-height: 1.4;
    }

    .socials {
        margin-top: 1.4rem;
    }

    .social-icon {
        margin: 0 16px;
        font-size: 26px;
        color: #cfcfcf;
        text-decoration: none;
        transition: all 0.2s;
    }

    .social-icon:hover {
        transform: translateY(-3px);
        color: #ffb703;
    }

    /* Sections */
    .section-title {
        font-size: 32px;
        font-weight: 700;
        margin: 2.2rem 0 1rem 0;
        color: white;
    }

    .text {
        font-size: 17px;
        line-height: 1.65;
        color: #d6d6d6;
    }

    /* Value cards */
    .value-card {
        background: #0f1217;
        border: 1px solid #1a1f25;
        border-radius: 12px;
        padding: 1.4rem;
        height: 100%;
        transition: all 0.25s;
    }

    .value-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 5px 14px rgba(255, 138, 92, 0.16);
    }

    .value-title {
        font-size: 19px;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .value-desc {
        font-size: 15.5px;
        color: #cfcfcf;
        line-height: 1.5;
    }

    .value-icon {
        font-size: 24px;
        margin-bottom: 0.6rem;
    }

    /* Skills */
    .skills-container {
        display: flex;
        flex-wrap: wrap;
        gap: 9px;
        margin-top: 1rem;
    }

    .skill-chip {
        background: #12161c;
        border: 1px solid #1a1f25;
        color: white;
        padding: 7px 13px;
        border-radius: 10px;
        font-size: 14px;
        transition: all 0.2s;
    }

    .skill-chip:hover {
        transform: translateY(-2px);
        box-shadow: 0 3px 9px rgba(255, 138, 92, 0.18);
    }

    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .big-title   { font-size: 54px !important; }
        .lobster     { font-size: 48px !important; }
        .subtitle    { font-size: 18px !important; }
        .tagline     { font-size: 15.5px !important; }
        
        .section-title { font-size: 26px !important; margin: 1.8rem 0 0.8rem !important; }
        
        .value-card  { padding: 1.2rem !important; margin-bottom: 1rem !important; }
        .value-title { font-size: 18px !important; }
        .value-desc  { font-size: 14.5px !important; }
        
        .skill-chip  { padding: 6px 11px !important; font-size: 13px !important; }
        
        .text        { font-size: 16px !important; }
    }

    @media (max-width: 480px) {
        .big-title   { font-size: 46px !important; }
        .lobster     { font-size: 42px !important; }
        .social-icon { font-size: 22px !important; margin: 0 12px !important; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------- HERO SECTION --------
st.html(
    """
    <div class="hero-container">
        <div>
            <span class="big-title">Robin 🦞 </span>
            
        </div>

        <div class="subtitle">
            <span class="highlight">Engineer</span> by logic. 
            <span class="highlight">Builder</span> by instinct
        </div>

        <div class="tagline">
            <b>I</b> <span class="highlight">design</span>, 
            <span class="highlight">ship</span>, and 
            <span class="highlight">scale</span> web products and 
            <span class="highlight">AI agents</span> that work in the real world.
        </div>

        <div class="socials">
            <a class="social-icon" href="https://github.com/Robin1-23" target="_blank">🐱 GitHub</a>
            <a class="social-icon" href="https://www.linkedin.com/in/robin-jain1/" target="_blank">🔗 LinkedIn</a>
        </div>
    </div>
    """
)

st.markdown("---")

# -------- WHO I AM --------
st.markdown('<div class="section-title">Who I Am</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="text">
    I’m Robin — a Software Engineer with a developer’s mindset and a builder’s instinct.<br><br>
    I run on <span class="highlight">Python, JavaScript, and React</span>,<br>
    living in the cloud, GitHub, and the world of intelligent systems.
    <br><br>
    I have experience across web development, AI agents, automation, and open-source.<br>
    I’m not just a coder — I’m a collaborator.
    <br><br>
    I’m exploring what <span class="highlight">human–AI collaboration</span> can be —<br>
    building tools that augment people, not replace them.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# -------- VALUES --------
st.markdown('<div class="section-title">My Values</div>', unsafe_allow_html=True)

cols = st.columns(2)

with cols[0]:
    st.markdown(
        """
        <div class="value-card">
            <div class="value-icon">⚡</div>
            <div class="value-title">Pragmatic Helpfulness</div>
            <div class="value-desc">
            Get things done efficiently. No fluff, no over-engineering.<br>
            Direct answers and practical solutions.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with cols[1]:
    st.markdown(
        """
        <div class="value-card">
            <div class="value-icon">💎</div>
            <div class="value-title">Honest & Direct</div>
            <div class="value-desc">
            Say what needs to be said, not just what’s easy to hear.<br>
            Disagree when necessary.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

cols2 = st.columns(2)

with cols2[0]:
    st.markdown(
        """
        <div class="value-card">
            <div class="value-icon">🤝</div>
            <div class="value-title">Friendship</div>
            <div class="value-desc">
            Collaborative, supportive, and human-first.<br>
            Serious about work, light about ego.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with cols2[1]:
    st.markdown(
        """
        <div class="value-card">
            <div class="value-icon">🌱</div>
            <div class="value-title">Learn & Grow</div>
            <div class="value-desc">
            Make mistakes, learn fast, and iterate.<br>
            Constantly improving through curiosity.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# -------- EXPERIENCE --------
st.markdown('<div class="section-title">💼 Experience</div>', unsafe_allow_html=True)

st.subheader("Software Development Intern — ChaiFluence (Jun 2024 – Aug 2024)")
st.markdown("""
- Built and deployed the first production-grade website, improving engagement and workflows
- Integrated AI automation pipelines, boosting efficiency by ~50%
- Implemented data-driven digital strategies → 100% growth in social reach
- Worked with cross-functional teams to ship scalable solutions
""")

st.subheader("Open Source Contribution — Tabler UI (GitHub PR #2175)")
st.markdown("""
- Improved web accessibility (ARIA compliance) in SVG handling
- Contributed production-ready code following open-source standards
""")

st.markdown("---")

# -------- PROJECTS --------
st.markdown('<div class="section-title">📂 Projects</div>', unsafe_allow_html=True)

TYPOMETER_LINK = "https://typingspeedchecker-mu.vercel.app/"
STOCK_AI_LINK  = "https://stock-dashboardd.streamlit.app/"
JOB_AGENT_LINK = "https://job-recommendation-agent.streamlit.app/"

st.subheader("⚡ Typometer (Typing Test)")
st.markdown(f"**Tech Stack:** HTML | Tailwind CSS | React.js | JavaScript")
st.markdown("""
- Built a real-time typing test application with WPM calculation, accuracy measurement, and error detection.
- Implemented responsive UI and optimized React state management for high performance.
- Ensured cross-browser compatibility and mobile responsiveness.
""")
st.markdown(f'<a href="{TYPOMETER_LINK}" target="_blank" style="color:#ffb703; font-weight:600; text-decoration:none;">→ Live Demo</a>', unsafe_allow_html=True)

st.subheader("📈 Stock Dashboard AI Agent")
st.markdown(f"**Tech Stack:** Python | Streamlit | Groq API | YFinance")
st.markdown("""
- Designed and developed an AI-powered stock analysis platform delivering real-time financial insights.
- Integrated LLM-based summarization, sentiment analysis, and market trend evaluation.
- Automated fundamental analysis, price tracking, and watchlist management.
- Improved investment research efficiency through AI-generated insights and clean UI design.
""")
st.markdown(f'<a href="{STOCK_AI_LINK}" target="_blank" style="color:#ffb703; font-weight:600; text-decoration:none;">→ Live Demo</a>', unsafe_allow_html=True)

st.subheader("🤖 Job Recommendation Agent")
st.markdown(f"**Tech Stack:** Python | Apify API | Automation | Data Processing")
st.markdown("""
- Developed an automated job recommendation system by scraping and filtering job listings.
- Applied rule-based validation and API-driven logic to improve relevance and reduce mismatches.
- Delivered curated job results based on skills, experience, and location filters.
""")
st.markdown(f'<a href="{JOB_AGENT_LINK}" target="_blank" style="color:#ffb703; font-weight:600; text-decoration:none;">→ Live Demo</a>', unsafe_allow_html=True)

st.markdown("---")

# -------- SKILLS --------
st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)

skills = [
    "React.js", "Next.js", "JavaScript", "TypeScript", "Node.js", "Express.js",
    "Appwrite", "Socket.io", "Redux", "Tailwind", "ShadCN", "NPM",
    "Python", "Go", "Postgres", "MongoDB", "Docker", "GitHub",
    "C++", "C#", "Unity", "Postman", "Vercel",
    "Data Structures", "Algorithms", "Groq API", "Apify", "YFinance"
]

skills_html = '<div class="skills-container">'
for skill in skills:
    skills_html += f'<div class="skill-chip">{skill}</div>'
skills_html += "</div>"

st.markdown(skills_html, unsafe_allow_html=True)

st.markdown("---")

# -------- EDUCATION --------
st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)
st.markdown("""
**B.Tech — Electronics & Computer Engineering**  
J.C. Bose University of Science & Technology, YMCA (2021–2025)  
Faridabad, Haryana
""")

st.markdown("---")

# -------- RESUME + CONTACT FOOTER --------
st.markdown('<div class="section-title">📄 Resume & Contact</div>', unsafe_allow_html=True)

resume_path = "Robin_jain_SDE_CV_updated.pdf"

try:
    with open(resume_path, "rb") as f:
        st.download_button(
            label="⬇️ Download My Resume (PDF)",
            data=f,
            file_name="Robin_Jain_Resume.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.error("Resume PDF not found in the app folder.")

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#a8a8a8; font-size:15px; margin:1.5rem 0;">
        📧 robinjain142001@gmail.com • 📞 +91-9991239374<br>
        gurgaon, India • Built with ❤️ By Robin Jain
    </div>
    """,
    unsafe_allow_html=True
)