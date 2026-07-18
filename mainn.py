import streamlit as st
import google.generativeai as genai
model=genai.GenerativeModel("gemini-2.5-flash")
st.markdown(
    """
    <style>
    /* Light blue background */
    .stApp, .reportview-container, body {
        background-color: #add8e6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Welcome to the  Food Prep App ")
name= st.text_input("Enter name: ") 
st.write( "Hi " + name, " Please fill in the details below. The more detail the better!")
Age=st.number_input("Enter age: ", min_value=1, max_value=100, step=1)
Gender=st.selectbox("Select gender: ", ["Male", "Female", "Other"])
Weight=st.number_input("Enter weight (in lbs): ", min_value=1,      max_value=1000, step=1) 
Height=st.number_input("Enter height (in inches): ", min_value=1, max_value=120, step=1)
Dietary_Restrictions=st.text_area("Enter dietary restrictions: ")
Food_Type=st.text_area("Enter the type of food you want to prepare: ")
Calorie_Count=st.text_area("Enter how many calories you hope to consume in your meal: ")
Budget=st.number_input("Enter budget in dollars: ", min_value=5.00, max_value=500.00, step=0.25)
Physical_Activity=st.text_area("Enter any sports, excercise, or physical activity you do: ")
Other_Notes=st.text_area("Enter other notes: ")
prompt=f"""You are an experienced allergist and food preperation specialist.Dont add unnessecary text about yourself.
Analyze the following profile and create a meal prep and diet plan .
Use evidence-based reasoning related to biomechanics, cooking, allergies, tastes, and budgeting.
Then, gived detailed recipes that they can make and give 3–5 recommendations of meals to prepare based on what they are craving of different amounts of budgets. Giving a diet plan for each meal of each day of the week based on the dietary restrictions, allergies, and other notes. Make sure to make everything fit inside the budget as best as possible and give the prices of each item and the total meal based on US food pricing.      
Data:     
Name: {name}    
Age: {Age}    
Gender: {Gender}    
Weight: {Weight}   
Height: {Height}    
Dietary Restrictions: {Dietary_Restrictions}
Food Type: {Food_Type}
Calorie Count: {Calorie_Count}
Budget: {Budget}
Physical Activity: {Physical_Activity}
Other notes: {Other_Notes}
Output Format:
Detailed Recipes: (give 5 detailed recipes based on the type of food)
Weekly Meal Plan: (provide a day-by-day and meal by meal diet plan based on dietary preferences)   
"""

st.write("Is all this info correct? If so, please proceed to get your meal plan.")
if st.button("Get Meal Plan"):
    st.write("### Meal Plan")
    with st.spinner("Processing your data..."):
        response=model.generate_content(prompt)   
    st.write(response.text)







