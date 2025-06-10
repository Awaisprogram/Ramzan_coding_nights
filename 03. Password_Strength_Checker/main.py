import streamlit as st

# Set page configuration and styling
st.set_page_config(
    page_title="Advanced Password Strength Analyzer",
    page_icon="🔒",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        color: #2c3e50;
        font-size: 42px;
        text-align: center;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .sub-header {
        color: #34495e;
        font-size: 18px;
        text-align: center;
        margin-bottom: 25px;
    }
    .result-text {
        background-color: #f1f8ff;
        padding: 15px;
        text-align: center;
        background: #2fe9e5;
        color: white;
        border-radius: 5px;
        font-size: 20px;
        margin: 20px 0;
    }
    .footer {
        text-align: center;
        color: #7f8c8d;
        font-size: 14px;
        margin-top: 30px;
    }
    .very-weak {
        background-color: #ff4d4d;
        color: white;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .weak {
        background-color: #ffa64d;
        color: white;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .medium {
        background-color: #ffff4d;
        color: black;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .strong {
        background-color: #4dff4d;
        color: black;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .very-strong {
        background-color: #4d4dff;
        color: white;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .password-stats {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
        border-left: 4px solid #2fe9e5;
    }
    .progress-container {
        margin: 20px 0;
    }
    .crack-time {
        font-weight: bold;
        color: #e74c3c;
    }
    .entropy-meter {
        height: 10px;
        border-radius: 5px;
        margin: 10px 0;
        background: linear-gradient(to right, #ff4d4d, #ffa64d, #ffff4d, #4dff4d, #4d4dff);
    }
    .tab-content {
        padding: 15px;
        border: 1px solid #ddd;
        border-top: none;
        border-radius: 0 0 5px 5px;
    }
    .stButton>button {
        background-color: #2fe9e5;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #27c6c3;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Password strength checking function with simplified metrics
def check_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Basic checks
    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters)")
    else:
        score += 1

    # Check for uppercase letters
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Check for lowercase letters
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Check for numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")

    # Check for special characters (simplified)
    special_chars = "!@#$%^&*(),.?\":{}|<>"
    if any(c in special_chars for c in password):
        score += 1
    else:
        feedback.append("Add special characters")

    # Advanced checks (simplified)
    # Check for sequential characters
    sequences = ["abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij",
                "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr",
                "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz",
                "012", "123", "234", "345", "456", "567", "678", "789", "890"]

    if any(seq in password.lower() for seq in sequences):
        feedback.append("Avoid sequential characters (like 'abc' or '123')")
        score -= 1

    # Check for repeated characters
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            feedback.append("Avoid repeated characters (like 'aaa')")
            score -= 1
            break

    # Check for common words
    common_words = ['password', 'admin', '123456', 'qwerty', 'welcome', 'letmein']
    if any(word in password.lower() for word in common_words):
        feedback.append("Avoid common words or patterns")
        score -= 1

    # Simplified entropy calculation
    char_set_size = 0
    if any(c.islower() for c in password): char_set_size += 26
    if any(c.isupper() for c in password): char_set_size += 26
    if any(c.isdigit() for c in password): char_set_size += 10
    if any(c in special_chars for c in password): char_set_size += len(special_chars)

    entropy = len(password) * (char_set_size.bit_length() if char_set_size > 0 else 0)

    # Simplified crack time estimation
    if entropy < 40:
        crack_time = "Seconds to Minutes"
    elif entropy < 60:
        crack_time = "Hours to Days"
    elif entropy < 80:
        crack_time = "Months to Years"
    else:
        crack_time = "Centuries"

    # Determine strength level based on score
    if score <= 1:
        strength = "Very Weak"
        css_class = "very-weak"
    elif score <= 2:
        strength = "Weak"
        css_class = "weak"
    elif score <= 3:
        strength = "Medium"
        css_class = "medium"
    elif score <= 4:
        strength = "Strong"
        css_class = "strong"
    else:
        strength = "Very Strong"
        css_class = "very-strong"

    # Simplified result for pattern detection
    patterns = []
    if any(seq in password.lower() for seq in sequences):
        patterns.append("Sequential characters")

    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            patterns.append("Repeated characters")
            break

    if any(word in password.lower() for word in common_words):
        patterns.append(f"Common word or pattern")

    result = {"patterns": patterns}

    return strength, feedback, css_class, crack_time, entropy, result

# Generate password hash for demonstration
def hash_password(password):
    # Simple hash representation (not for actual security use)
    hash_value = 0
    for char in password:
        hash_value = (hash_value * 31 + ord(char)) & 0xFFFFFFFF
    return hex(hash_value)[2:].zfill(8)

# Streamlit UI
st.markdown("<h1 class='main-header'>Advanced Password Strength Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-header'>Evaluate and improve your password security</h2>", unsafe_allow_html=True)

# Create tabs for different features
tab1, tab2 = st.tabs(["Password Analysis", "Security Tips"])

with tab1:
    # Password input
    password = st.text_input("Enter your password", type="password", key="password_input")

    if st.button("Analyze Password"):
        if password:
            # Show a spinner while "analyzing" (for effect)
            with st.spinner("Analyzing password strength..."):
                strength, feedback, css_class, crack_time, entropy, result = check_password_strength(password)

            # Display strength with progress bar
            st.markdown(f"<div class='{css_class}'><h3>Password Strength: {strength}</h3></div>", unsafe_allow_html=True)

            # Display advanced metrics
            st.markdown("<div class='password-stats'>", unsafe_allow_html=True)
            st.subheader("Password Analysis")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Password Length", len(password))
                char_sets = 0
                if any(c.islower() for c in password): char_sets += 1
                if any(c.isupper() for c in password): char_sets += 1
                if any(c.isdigit() for c in password): char_sets += 1
                if any(c in "!@#$%^&*(),.?\":{}|<>" for c in password): char_sets += 1
                st.metric("Character Sets Used", char_sets)

            with col2:
                st.metric("Entropy Score", f"{entropy:.2f} bits")
                st.markdown(f"<p>Estimated time to crack: <span class='crack-time'>{crack_time}</span></p>", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

            # Display feedback
            if feedback:
                st.subheader("Suggestions to improve:")
                for tip in feedback:
                    st.markdown(f"- {tip}")

            # Show pattern matches
            if result["patterns"]:
                st.subheader("Patterns detected in your password:")
                for pattern in result["patterns"]:
                    st.markdown(f"- {pattern}")
        else:
            st.warning("Please enter a password to analyze.")

with tab2:
    st.subheader("Password Security Best Practices")
    st.markdown("""
    ### Creating Strong Passwords
    - Use at least 12 characters, the more the better
    - Mix uppercase letters, lowercase letters, numbers, and special characters
    - Avoid using personal information (names, birthdays, etc.)
    - Don't use common words or patterns
    - Consider using a passphrase (multiple random words together)

    ### Password Management
    - Use a different password for each account
    - Consider using a password manager
    - Change passwords periodically, especially for critical accounts
    - Enable two-factor authentication when available

    ### What to Avoid
    - Sequential characters (abc, 123)
    - Repeated characters (aaa, 111)
    - Common substitutions (p@ssw0rd)
    - Personal information (birthdays, names)
    - Dictionary words without modification
    """)


st.markdown("<hr>", unsafe_allow_html=True)
current_date = st.session_state.get('current_date', 'June 2023')
st.markdown(f"<div class='footer'>Made by Awais Mehmood with Streamlit</div>", unsafe_allow_html=True)
