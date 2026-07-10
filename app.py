import streamlit as st
import random

st.title("🌸 meet ney")
st.write("Your personal AI companion — completely keyless!")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I am ney. What's on your mind? ✨"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Message ney..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        responses = [
            f"That's interesting! Tell me more about '{prompt}'.",
            "I love how you look at things! Let's dive deeper. 🌌",
            "That sounds like a brilliant idea!",
            "ney is fully operational! Let's keep chatting. 🚀"
        ]
        reply = random.choice(responses)
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
  
