import streamlit as st

# Unit conversion functions
def length_conversion(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701,
    }
    return value * length_units[to_unit] / length_units[from_unit]


def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1e6,
        "pounds": 2.20462,
        "ounces": 35.274,
    }
    return value * weight_units[to_unit] / weight_units[from_unit]


def temperature_conversion(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    if from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    if from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    if from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    if from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    if to_unit == "Fahrenheit" and from_unit == "Kelvin":
        return (value - 273.15) * 9/5 + 32


# Streamlit UI with enhanced design
st.set_page_config(page_title="Unit Converter", page_icon="🧭", layout="wide")

# Custom CSS with improved styling
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        background: linear-gradient(90deg, #FF6F61, #6B5B95);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #555;
        margin-bottom: 30px;
    }
    .result-card {
        background: linear-gradient(135deg, #E3FCEF, #D4F1F9);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
        text-align: center;
    }
    .result-value {
        font-size: 2em;
        font-weight: bold;
        color: #2E7D32;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        font-size: 1em;
        color: #1b4a16;
        border-top: 1px solid #eee;
    }
    .stButton>button {
        background-color: #6B5B95;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 25px;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #FF6F61;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .category-icon {
        font-size: 2em;
        margin-right: 10px;
    }
    .sidebar-header {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .stSelectbox label, .stNumberInput label {
        font-weight: bold;
        color: #555;
    }
    .unit-selector {
        margin: 10px 0;
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #6B5B95;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with improved navigation
with st.sidebar:
    st.markdown("<div class='sidebar-header'><h2>Navigation 🧭</h2></div>", unsafe_allow_html=True)
    st.write("Welcome to the Unit Converter! Choose your options below:")
    
    category = st.selectbox("Select a category", [
        "📏 Length", "⚖️ Weight", "🌡️ Temperature"
    ])
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    value = st.number_input("Enter the value to convert", 
                           min_value=0.0, 
                           format="%.6f",
                           help="Type the number you want to convert")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### How to use")
    st.markdown("""
    1. Select a category
    2. Enter your value
    3. Choose your units
    4. Click Convert!
    """)

# Main content area
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown("<div class='main-title'>Advanced Unit Converter</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Convert between different units with precision and ease</div>", unsafe_allow_html=True)

    # Category specific UI 
    if category == "📏 Length":
        st.markdown(f"<h2><span class='category-icon'>📏</span> Length Conversion</h2>", unsafe_allow_html=True)
        
        length_units = [
            "meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"
        ]
        
        col_from, col_to = st.columns(2)
        
        with col_from:
            st.markdown("<div class='unit-selector'>", unsafe_allow_html=True)
            from_unit = st.selectbox("From", length_units, key="length_from")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_to:
            st.markdown("<div class='unit-selector'>", unsafe_allow_html=True)
            to_unit = st.selectbox("To", length_units, key="length_to")
            st.markdown("</div>", unsafe_allow_html=True)
            
        result = length_conversion(value, from_unit, to_unit)

    elif category == "⚖️ Weight":
        st.markdown(f"<h2><span class='category-icon'>⚖️</span> Weight Conversion</h2>", unsafe_allow_html=True)
        
        weight_units = ["kilograms", "grams", "milligrams", "pounds", "ounces"]
        
        col_from, col_to = st.columns(2)
        
        with col_from:
            st.markdown("<div class='unit-selector'>", unsafe_allow_html=True)
            from_unit = st.selectbox("From", weight_units, key="weight_from")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_to:
            st.markdown("<div class='unit-selector'>", unsafe_allow_html=True)
            to_unit = st.selectbox("To", weight_units, key="weight_to")
            st.markdown("</div>", unsafe_allow_html=True)
            
        result = weight_conversion(value, from_unit, to_unit)

    elif category == "🌡️ Temperature":
        st.markdown(f"<h2><span class='category-icon'>🌡️</span> Temperature Conversion</h2>", unsafe_allow_html=True)
        
        temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
        
        col_from, col_to = st.columns(2)
        
        with col_from:
            st.markdown("<div class='unit-selector'>", unsafe_allow_html=True)
            from_unit = st.selectbox("From", temp_units, key="temp_from")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_to:
            st.markdown("<div class='unit-selector'>", unsafe_allow_html=True)
            to_unit = st.selectbox("To", temp_units, key="temp_to")
            st.markdown("</div>", unsafe_allow_html=True)
            
        result = temperature_conversion(value, from_unit, to_unit)

    # Centered convert button
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        convert_clicked = st.button("Convert 🚀", use_container_width=True)

    # Display result with animation
    if convert_clicked:
        st.balloons()
        st.markdown(f"""
        <div class='result-card'>
            <h3>Conversion Result:</h3>
            <div class='result-value'>{value} {from_unit} = {result:.6g} {to_unit}</div>
            <p>Formula used: Based on standard conversion factors</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Add a formula explanation based on category
        if category == "📏 Length":
            st.info(f"Length conversion uses a base unit of meters with appropriate conversion factors.")
        elif category == "⚖️ Weight":
            st.info(f"Weight conversion uses a base unit of kilograms with appropriate conversion factors.")
        elif category == "🌡️ Temperature":
            st.info(f"Temperature conversion uses specific formulas for each conversion type.")

# Footer with improved design
st.markdown("<div class='footer'>Made with ❤️ by Awais Mehmood", unsafe_allow_html=True)