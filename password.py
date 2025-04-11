import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔑", layout="centered")
st.title("🔏Password Strength Meter")
st.markdown("This app checks the strength of your password and provides suggestions for improvement.") 

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else: 
        feedback.append("❌Password must be at least 8 characters long.")    
        
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Password must contain both uppercase and lowercase letters.")    
            
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password must contain at least one digit.")     

    if re.search(r'[@$!%*?&]',password):
        score += 1
    else:
        feedback.append("❌Password must contain at least one special character (@$!%*?&).")  

    if score == 4:
        feedback.append("✅ Your password is strong!")  
    elif score == 3:    
        feedback.append("⚠️ Your password is moderate. It could be stronger.")
    else:
        feedback.append("❌ Your password is weak. Please make it stronger.")     

    if feedback:
        st.markdown("## Improvement Suggestions:")
        for suggestion in feedback:
            st.markdown(suggestion)    

else:
    st.info("Please enter a password to check its strength.")
    