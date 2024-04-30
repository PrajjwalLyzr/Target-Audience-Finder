import streamlit as st


def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 450px;
           max-width: 450px;
       }
    </style>
    """, unsafe_allow_html=True)

def page_config(layout = "centered"):
    st.set_page_config(
        page_title="Lyzr - Target Audience Finder",
        layout=layout,  # or "wide" 
        initial_sidebar_state="auto",
        page_icon="./logo/lyzr-logo-cut.png"
    )

def template_end():
    with st.expander("ℹ️ - About this App"):
        st.markdown("This app uses Lyzr's Automata to find the target audience based on Demographics, Interests and their Behaviour for marketing Campaign")
        st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
        st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
        st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
        st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)