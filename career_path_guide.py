import streamlit as st
import google.generativeai as genai

# 🔹 Configure Gemini API
genai.configure(api_key=st.secrets.get("GOOGLE_API_KEY", None) or "YOUR_API_KEY_HERE")

# 🔹 Streamlit App Setup
st.set_page_config(page_title="AI Career Path Guide", page_icon="🎓", layout="centered")

st.title("🎯 AI Career Path Guide")
st.caption("Your personalized career mentor powered by Gemini AI")

# --- Step 1: Basic Info ---
name = st.text_input("👤 Enter your name:")
if name:
    st.success(f"Welcome, {name}! Let's plan your future career path.")

    # --- Step 2: Education Level ---
    edu_level = st.selectbox("🎓 Select your current education level:",
                             ["Select", "10th", "12th", "Graduate", "Postgraduate"])

    stream = ""
    if edu_level == "12th":
        stream = st.selectbox("📘 Choose your stream:",
                              ["Select", "Science", "Commerce", "Arts"])
    elif edu_level == "Graduate":
        stream = st.text_input("🎓 Enter your graduation specialization (e.g., B.Tech, B.Com, BA):")
    elif edu_level == "Postgraduate":
        stream = st.text_input("🎓 Enter your postgraduate specialization (e.g., MBA, M.Tech, MA):")

    # --- Step 3: Interests ---
    interests = st.text_area("💡 What are your interests or favorite subjects?",
                             placeholder="e.g., coding, teaching, design, marketing, public service")

    # --- Step 4: User goal ---
    goal = st.radio("🏁 What type of career are you interested in?",
                    ["Any", "Government Sector", "Private Sector", "Entrepreneurship"])

    # --- Generate Button ---
    if st.button("🔍 Get My Career Path"):
        if edu_level == "Select":
            st.warning("Please select your education level.")
        else:
            with st.spinner("Analyzing your profile with Gemini AI..."):
                prompt = f"""
                You are an expert career counselor AI.
                Provide detailed, realistic, and encouraging guidance.

                User name: {name}
                Education level: {edu_level}
                Stream/specialization: {stream}
                Interests: {interests}
                Preferred career goal: {goal}

                Please include the following sections:
                1. Personalized Career Summary
                2. Top 5 Suitable Career Paths
                3. Private Sector Opportunities
                4. Government Sector Opportunities
                5. Recommended Higher Studies or Courses
                6. Career Roadmap (Step-by-step)
                7. Motivational Note
                """

                try:
                    # 🔹 Use a supported Gemini model
                    model = genai.GenerativeModel("gemini-2.5-flash")
                    response = model.generate_content(prompt)
                    st.markdown("## 🧭 Your AI Career Guidance")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error generating AI response: {e}")

    # --- Optional Enhancements ---
    with st.expander("📊 View Learning & Job Resources"):
        st.write("""
        **Online Learning Platforms**
        - Coursera, Udemy, NPTEL, Skillshare  
        - Google Career Certificates  
        - Khan Academy (Free)

        **Government Job Portals**
        - [SSC](https://ssc.gov.in)
        - [UPSC](https://upsc.gov.in)
        - [Naukri.com - Govt Jobs](https://www.naukri.com/govt-jobs)
        - [Employment News](https://www.employmentnews.gov.in)

        **Private Job Portals**
        - [LinkedIn](https://linkedin.com)
        - [Indeed](https://indeed.com)
        - [Internshala](https://internshala.com)
        """)
else:
    st.info("👆 Please enter your name to begin.")
