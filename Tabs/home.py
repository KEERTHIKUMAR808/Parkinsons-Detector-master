"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Parkinson's Disease Predicton")

    # Add image to the home page
    st.image("./images/Front.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Parkinson's disease is a type of neurodegenerative illness that impacts the nervous system, particularly the motor and central nervous systems. Parkinson’s disease causes a specific area of your brain, the basal ganglia, to deteriorate.
 Tremor (shaking) often begins in a hand, although sometimes a foot or the jaw is the initial symptom of Parkinson disease. Bradykinesia  is a cardinal symptom of Parkinson's disease. It refers to a decrease in the speed and ease of voluntary movements, making everyday tasks more challenging and time-consuming.
        </p>
    """, unsafe_allow_html=True)