import streamlit as st

#st.set_page_config(page_title="App Profile", layout="centered")

def show():

    # TEAM PROFILE SECTION
    st.markdown("<h1 style='font-size: 48px; text-align: center;'>MEET OUR DATA TEAM</h1>", unsafe_allow_html=True)

    # Create columns for layout
    col1, col2, col3, col4, col5 = st.columns(5)

    # Helper function to display team member with fixed size
    def display_member(col, img_path, name, role):
        with col:
            st.image(img_path, width=170)  # Consistent width for all images
            st.markdown(f"""
                <div style='text-align: center; margin-top: -10px;'>
                    <p style='margin-bottom: 4px;'>{name}</p>
                    <p style='font-weight: bold; margin-top: 0;'>{role}</p>
                </div>
            """, unsafe_allow_html=True)

    # Display team members using updated & resized images
    display_member(col1, "deployment/KakLis.jpg", "Lis Wahyuni", "Mentor")
    display_member(col2, "deployment/Arvin.png", "Arvin Surya Wibowo", "Data Scientist")
    display_member(col3, "deployment/Matthew.png", "Matthew Farrel Dharsono", "Data Analyst")
    display_member(col4, "deployment/Luthfi.png", "Luthfi Nadyan Putra", "Data Engineer")
    display_member(col5, "deployment/Yonathan.png", "Yonathan Anggraiwan", "Data Analyst")

if __name__ == "__main__":
    show()