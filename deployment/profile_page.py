import streamlit as st

def show():
    st.markdown("<h1 style='font-size: 48px; text-align: center;'>Meet Our Data Team</h1>", unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    # Tinggi tetap untuk area nama agar semua sejajar
    NAME_BLOCK_HEIGHT = 40  # adjust as needed

    def display_member(col, img_path, name, role):
        with col:
            st.image(img_path, width=170)
            st.markdown(
                f"""
                <div style='text-align: center; margin-top: -10px;'>
                    <!-- Fixed-height block for name -->
                    <div style='height:{NAME_BLOCK_HEIGHT}px; 
                                display:flex; 
                                justify-content:center;
                                align-items:center;
                                text-align:center;
                                font-size:16px;
                                line-height:1.2;'>
                        <span>{name}</span>
                    </div>
                    <p style='font-weight: bold; margin-top:4px; margin-bottom:0; font-size:16px;'>{role}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    display_member(col1, "KakLis.jpg", "Lis Wahyuni", "Mentor")
    display_member(col2, "Arvin.png", "Arvin Surya Wibowo", "Data Scientist")
    display_member(col3, "Luthfi.png", "Luthfi Nadyan Putra", "Data Engineer")
    display_member(col4, "Matthew.png", "Matthew Farrel Dharsono", "Data Analyst")
    display_member(col5, "Yonathan.png", "Yonathan Anggraiwan", "Data Analyst")

if __name__ == "__main__":
    show()
