#stramlit 

import streamlit as st # type: ignore
st.set_page_config(page_title= "Growth MindSet Project", page_icon="✪")
st.title("GROWTH MINDSET CHALLENGE: Web App With Sreaamlit")

st.header("🚀WELCOME TO YOUR GROWTH JOURNEY!")
st.write("Embrace obstacles as stepping stones, transform setbacks into wisdom, and unleash your boundless potential. This AI-crafted app nurtures a vibrant growth mindset through inspiring reflections, engaging challenges, and triumphant milestones!✨")

#quote section

st.header("⌛Today's Inspiration for a Thriving Growth Mindset")
st.write("'Achievement is not the end, nor is defeat the end-all: it's the bravery to persist that truly shapes your journey.'— Inspired by Winston Churchill")

st.header("🧭What Inspiring Quest Awaits You Today?")
user_input = st.text_input("Share a hurdle you're navigating on your path to growth:")

#condition

if user_input:
    st.success(f"🛤️you are facing: {user_input}. keep pushing forward towords you goal!")
else:
    st.warning("Tell us about your challenge to get started!")
 

 #reflexing
 
st.header("Reflect on your learning")
reflection = st.text_area("Write your reflection over here:")

if reflection:
    st.success(F"💫Great Insight! Your Reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")


#acheivements

st.header("Rejoice in Your Triumphs! 🎉")
acheivement = st.text_input("Share the radiant milestone you’ve recently achieved on your journey of growth: 🌟")

if acheivement:
    st.success(f"Marvel at Your Magnificent Feat! {acheivement}")
else:
    st.info(f"Big or Small, every acheivements counts! share one now!🙌")


#footer

st.write("- - -")
st.write("Trust in Your Boundless Potential! 🌱")
st.write("⛔CREATED BY ALIHA USMAN")    