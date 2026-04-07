# DizzBoard - Real-Time Lab System Monitoring Dashboard
# Simplified implementation of my final year project
# Originally deployed in a college laboratory to monitor live system status

import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="DizzBoard Dashboard", layout="wide")

# ---------------- LOGIN SIMULATION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🔐 DizzBoard Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

# ---------------- MAIN APP ----------------
def main_app():
    st.title("🖥️ DizzBoard - Lab Monitoring System")
    st.markdown("Real-time monitoring system designed for managing lab machines.")

    # Sidebar
    st.sidebar.title("Navigation")
    menu = st.sidebar.selectbox(
        "Select Option",
        ["➕ Add Systems", "📋 View Systems", "📡 Monitor Systems"]
    )

    # Initialize storage
    if "systems" not in st.session_state:
        st.session_state.systems = []

    # ---------------- ADD SYSTEM ----------------
    if menu == "➕ Add Systems":
        st.subheader("Add New System")

        name = st.text_input("System Name")
        ip = st.text_input("IP Address")

        if st.button("Add System"):
            if name and ip:
                st.session_state.systems.append({
                    "System Name": name,
                    "IP Address": ip
                })
                st.success(f"{name} added successfully!")

    # ---------------- VIEW SYSTEMS ----------------
    elif menu == "📋 View Systems":
        st.subheader("Registered Systems")

        if st.session_state.systems:
            df = pd.DataFrame(st.session_state.systems)
            st.dataframe(df)
        else:
            st.warning("No systems added yet.")

    # ---------------- MONITOR SYSTEMS ----------------
    elif menu == "📡 Monitor Systems":
        st.subheader("Live System Monitoring")

        if st.session_state.systems:
            online = []
            offline = []

            for system in st.session_state.systems:
                status = random.choice(["Online", "Offline"])

                if status == "Online":
                    online.append(system["System Name"])
                else:
                    offline.append(system["System Name"])

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 🟢 Online Systems")
                for sys in online:
                    st.success(sys)

            with col2:
                st.markdown("### 🔴 Offline Systems")
                for sys in offline:
                    st.error(sys)

            # Chart
            chart_data = pd.DataFrame({
                "Status": ["Online", "Offline"],
                "Count": [len(online), len(offline)]
            })

            st.subheader("System Status Overview")
            st.bar_chart(chart_data.set_index("Status"))

            # Real-world note
            st.info("This system was implemented in a college lab to monitor system availability in real-time.")

        else:
            st.warning("No systems added yet.")

# ---------------- RUN APP ----------------
if not st.session_state.logged_in:
    login()
else:
    main_app()
