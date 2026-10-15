
import streamlit as st
import hmac

# Seiteneinstellungen
st.set_page_config(
    page_title="Mein Dashboard",
    page_icon="🔗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Große Link-Buttons gestalten
st.markdown("""
<style>
    /* Nur die Link-Buttons anpassen */
    div[data-testid="stLinkButton"] a {
        min-height: 90px !important;
        width: 100% !important;
        border-radius: 12px !important;
        border: 2px solid #D1D5DB !important;
        background-color: #F8FAFC !important;
        color: #1F2937 !important;
        transition: all 0.2s ease !important;
    }

    /* Schriftgröße und Schriftstärke */
    div[data-testid="stLinkButton"] a p {
        font-size: 28px !important;
        font-weight: 700 !important;
        line-height: 1.3 !important;
    }

    /* Hover-Effekt */
    div[data-testid="stLinkButton"] a:hover {
        background-color: #E8F0FE !important;
        border-color: #2563EB !important;
        color: #1D4ED8 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Passwortprüfung
def check_password():
    if st.session_state.get("authenticated", False):
        return True

    st.title("🔐 Geschützter Bereich")
    st.write("Bitte geben Sie das Passwort ein, um fortzufahren.")

    with st.form("login_form"):
        password = st.text_input(
            "Passwort",
            type="password"
        )
        submitted = st.form_submit_button(
            "Anmelden",
            use_container_width=True
        )

    if submitted:
        correct_password = st.secrets["auth"]["password"]

        if hmac.compare_digest(password, correct_password):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Das Passwort ist leider falsch.")

    return False


# Zugriffsschutz
if not check_password():
    st.stop()


# Landing Page
st.title("Willkommen zum Standard-Setting-Workshop Lesen")
st.write("Berlin, 30.10.2026")
st.divider()

# Links aus Streamlit Secrets laden
links = st.secrets["links"]

for index, link in enumerate(links, start=1):
    st.link_button(
        label=link["text"],
        url=link["url"],
        use_container_width=True,
        type="secondary"
    )

    st.write("")  # Abstand zwischen den Buttons


# Abmelden
st.divider()

if st.button("🚪 Abmelden"):
    st.session_state.authenticated = False
    st.rerun()
