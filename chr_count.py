import streamlit as st

# Title
st.title("📄 Word/Character Counter")

# User Inputs
para = st.text_area("Enter your paragraph:")
sp_chr = st.text_input("Enter the word/character you want to count:")

# Button
if st.button("Count"):
    value_count = para.count(sp_chr)

    if sp_chr == "":
        st.warning("Please enter a word or character to count.")
    elif value_count == 0:
        st.error(f'Your word/character "{sp_chr}" does not occur within your paragraph.')
    elif value_count == 1:
        st.success(f'Your word/character "{sp_chr}" occurs once within your paragraph.')
    else:
        st.success(f'Your word/character "{sp_chr}" occurs {value_count} times within your paragraph.')