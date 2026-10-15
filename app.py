
import streamlit as st
import hmac

# Seiteneinstellungen
st.set_page_config(
    page_title="Mein Dashboard",
    page_icon="🔗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

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
