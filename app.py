import streamlit as st
from PIL import Image
from model_predict import *
from streamlit_webrtc import webrtc_streamer

st.title("✨ Welcome ✨")
st.sidebar.title("🎇Choose an options🎇")
choice_options=st.sidebar.selectbox("",('Home','Start webcam','About'))

if choice_options=="Home":
    st.title('👨Face Emotion Recognition using Live Web Camera👩')
    image = Image.open('data/face.jpeg')
    st.image(image)
    st.sidebar.subheader("""💎 Face Emotion Recognition is a system used to detect the emotions from face.""")
    st.sidebar.subheader("""💎 Nowadays it is widely used applications.Eg: In zoom meeting we can able to detect the student emotion.""")
    st.sidebar.subheader("""💎 It is very helpful for teachers where they can able to teach based on their students emotion and make class more interactive.""")
if choice_options=="Start webcam":
    st.header("Webcam Live Feed")
    st.write("Click on start to use webcam and detect your face emotion")
    webrtc_streamer(key="example", video_processor_factory=VideoProcessor)
if choice_options=="About":
    st.title('Project Members')
    col1, col2= st.columns(2)
    with col1:
        image_1= Image.open('data/ape.png')
        st.subheader("Sushant Jagtap")
        st.image(image_1)
        st.write("Email:sushant8525@gmail.com")
        st.markdown("""[LinkedIn profile](https://www.linkedin.com/in/sushant-jagtap-b93a771a/)""")
    with col2:
        image_2 = Image.open('data/jai.png')
        st.subheader("Akash Bhor" )
        st.image(image_2)
        st.write("Email:Akashbhor111@gmail.com")
        st.markdown("""[LinkedIn profilehttps://www.linkedin.com/in/akash-bhor-b62503149/)""")

   
    with col2:
        pass


