# streamlit
import streamlit as st
st.set_page_config(page_title="growth mindset project", page_icon='✭')
st.title("Growth Mindset Challange: Web App with Streamlit")

st.header("🚀 Welcome to your Growth Journey!")
st.write("Embrace challange, learn from mistake, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challanges,and achievement!✸")


#quote section
st.header(" 💡 Today Growth mindset Qoute")
st.write("Succes is not final, failure is not fatal: it is the courage to continue that counts.-Winston Churchill")

# condition
st.header("🔧 What`s your Challange Today?")
user_input= st.text_input("Describe a challange you`re facing:")

if user_input:
    st.success(f" you`re facing: {user_input}. keep pushing forward towards your goal!🚀`")
else:
        st.warning("Tell us about your Challange to get started!")
        

#reflexing
st.header("reflect on your learning")
reflection = st.text_area("write your reflection here!")

if reflection:
    st.success("f⊱  ۫ ׅ ✧Great inside! your reflection: {reflection}")
else:
        st.info("reflecting on past experience help you grow! share your difficulties")


 # achivment
st.header("🏆 Celebrate your Wins!")
achievment = st.text_input("share something you`ve recently accomplished")

if achievment:
    st.success(f"⚜️Amazing! You Achieved: {achievment}")
else: 
        st.info("big or small, every achivment counts! share one now😍")