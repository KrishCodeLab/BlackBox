
# import streamlit as st
# from datetime import datetime

# from AiEngine import investigate_incident
# from log_processor import parse_logs, summarize_logs

# st.set_page_config(
#     page_title="BLACKBOX | AI Investigator",
#     page_icon="🔎",
#     layout="wide"
# )

# # ---------- SESSION STATE ----------

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# if "username" not in st.session_state:
#     st.session_state.username = ""

# if "theme" not in st.session_state:
#     st.session_state.theme = "Dark"

# if "history" not in st.session_state:
#     st.session_state.history = []

# if "report" not in st.session_state:
#     st.session_state.report = ""

# if "summary" not in st.session_state:
#     st.session_state.summary = None

# if "parsed_logs" not in st.session_state:
#     st.session_state.parsed_logs = []

# # ---------- THEMES ----------

# if st.session_state.theme == "Dark":
#     bg = "#0B1020"
#     panel = "#151D30"
#     text = "#F1F5F9"
#     accent = "#38BDF8"
#     muted = "#A7B4C8"
# else:
#     bg = "#F4F7FB"
#     panel = "#FFFFFF"
#     text = "#172033"
#     accent = "#0369A1"
#     muted = "#536176"

# st.markdown(f"""
# <style>
# .stApp {{
#     background-color: {bg};
#     color: {text};
# }}
# [data-testid="stSidebar"] {{
#     background-color: {panel};
# }}
# h1, h2, h3, p, label {{
#     color: {text};
# }}
# .brand {{
#     font-size: 38px;
#     font-weight: 800;
#     letter-spacing: 4px;
#     color: {accent};
# }}
# .subtitle {{
#     color: {muted};
#     font-size: 15px;
# }}
# .panel {{
#     background: {panel};
#     padding: 20px;
#     border-radius: 14px;
#     border: 1px solid {accent}44;
#     margin-bottom: 14px;
# }}
# .footer {{
#     text-align: center;
#     color: {muted};
#     padding: 24px 5px;
#     margin-top: 35px;
#     border-top: 1px solid {accent}55;
# }}
# .stButton button {{
#     border-radius: 9px;
# }}
# </style>
# """, unsafe_allow_html=True)


# def footer():
#     st.markdown("""
#     <div class="footer">
#         <b>BLACKBOX</b> · AI-Powered Incident Investigation<br>
#         Turning system logs into actionable insights.<br><br>
#         Contact: blackbox.team@example.com<br>
#         © 2026 BLACKBOX · Built by the BLACKBOX team
#     </div>
#     """, unsafe_allow_html=True)


# def header():
#     st.markdown(
#         '<div class="brand">BLACKBOX <span>⌁</span></div>',
#         unsafe_allow_html=True
#     )
#     st.markdown(
#         '<div class="subtitle">'
#         'AI-POWERED INCIDENT INVESTIGATION SYSTEM'
#         '</div>',
#         unsafe_allow_html=True
#     )
#     st.divider()


# # ---------- LOGIN PAGE ----------

# if not st.session_state.logged_in:
#     st.markdown("<br><br>", unsafe_allow_html=True)

#     left, middle, right = st.columns([1, 1.2, 1])

#     with middle:
#         header()

#         st.subheader("Welcome back, Investigator")
#         st.write("Sign in to access your investigation workspace.")

#         with st.form("login_form"):
#             username = st.text_input("Username")
#             password = st.text_input(
#                 "Password",
#                 type="password"
#             )
#             submitted = st.form_submit_button(
#                 "Sign in →",
#                 use_container_width=True
#             )

#         if submitted:
#             # DEMO ONLY: replace with real authentication
#             if username == "demo" and password == "blackbox123":
#                 st.session_state.logged_in = True
#                 st.session_state.username = username
#                 st.rerun()
#             else:
#                 st.error(
#                     "Invalid demo credentials. "
#                     "Use demo / blackbox123."
#                 )

#         st.info(
#             "Prototype login only. Do not use real or sensitive "
#             "credentials with this demo authentication."
#         )

#     footer()
#     st.stop()


# # ---------- SIDEBAR NAVIGATION ----------

# with st.sidebar:
#     st.markdown("## 🔎 BLACKBOX")
#     st.caption("INVESTIGATION CONSOLE")
#     st.divider()

#     st.write(f"Investigator: **{st.session_state.username}**")

#     page = st.radio(
#         "NAVIGATION",
#         [
#             "Dashboard",
#             "New Investigation",
#             "Investigation History",
#             "Help",
#             "Contact"
#         ]
#     )

#     st.divider()
#     st.write("### Appearance")

#     theme_choice = st.radio(
#         "Choose theme",
#         ["Dark", "Light"],
#         index=0 if st.session_state.theme == "Dark" else 1
#     )

#     if theme_choice != st.session_state.theme:
#         st.session_state.theme = theme_choice
#         st.rerun()

#     if st.button("Log out", use_container_width=True):
#         st.session_state.logged_in = False
#         st.session_state.username = ""
#         st.rerun()


# # ---------- DASHBOARD ----------

# if page == "Dashboard":
#     header()

#     st.title("Investigation Dashboard")
#     st.write(
#         "Monitor system logs, investigate incidents, "
#         "and review AI-generated findings."
#     )

#     summary = st.session_state.summary or {}

#     c1, c2, c3, c4 = st.columns(4)

#     c1.metric("Investigations", len(st.session_state.history))
#     c2.metric("Total logs", summary.get("total", 0))
#     c3.metric("Errors", summary.get("errors", 0))
#     c4.metric("Warnings", summary.get("warnings", 0))

#     st.markdown(
#         '<div class="panel">'
#         '<h3>⚡ Start an investigation</h3>'
#         '<p>Analyze logs using your local Gemma AI model.</p>'
#         '</div>',
#         unsafe_allow_html=True
#     )

#     if st.button(
#         "＋ New Investigation",
#         type="primary",
#         use_container_width=True
#     ):
#         st.session_state.page_request = "New Investigation"
#         st.rerun()

#     st.subheader("Latest report")

#     if st.session_state.report:
#         st.markdown(st.session_state.report)
#         st.download_button(
#             "Download latest report",
#             data=st.session_state.report,
#             file_name="blackbox_report.txt",
#             mime="text/plain"
#         )
#     else:
#         st.info("No investigations yet. Start your first one.")

#     footer()


# # ---------- NEW INVESTIGATION ----------

# elif page == "New Investigation" or (
#     page == "Dashboard"
#     and st.session_state.get("page_request") == "New Investigation"
# ):
#     st.session_state.pop("page_request", None)
#     header()

#     st.title("🔍 New Investigation")
#     st.write("Provide system logs for analysis.")

#     uploaded_file = st.file_uploader(
#         "Upload a log file",
#         type=["txt", "log"]
#     )

#     if uploaded_file is not None:
#         logs = uploaded_file.getvalue().decode(
#             "utf-8",
#             errors="replace"
#         )
#     else:
#         logs = st.text_area(
#             "Or paste logs here",
#             height=250,
#             placeholder=(
#                 "10:00:01 INFO API server started\n"
#                 "10:00:02 WARN Database response delayed\n"
#                 "10:00:03 ERROR Database connection timeout"
#             )
#         )

#     if st.button(
#         "🚀 Investigate Incident",
#         type="primary",
#         disabled=not logs.strip(),
#         use_container_width=True
#     ):
#         try:
#             with st.spinner("Parsing and summarizing logs..."):
#                 parsed_logs = parse_logs(logs)
#                 summary = summarize_logs(parsed_logs)

#             with st.spinner(
#                 "Gemma AI is investigating your incident..."
#             ):
#                 report = investigate_incident(logs)

#             st.session_state.parsed_logs = parsed_logs
#             st.session_state.summary = summary
#             st.session_state.report = report

#             st.session_state.history.insert(0, {
#                 "time": datetime.now().strftime(
#                     "%Y-%m-%d %H:%M:%S"
#                 ),
#                 "summary": summary,
#                 "report": report,
#                 "logs": logs
#             })

#             st.success("Investigation completed!")

#         except Exception as error:
#             st.error("Investigation failed.")
#             st.exception(error)

#     if st.session_state.summary is not None:
#         st.divider()
#         st.subheader("Incident overview")

#         summary = st.session_state.summary
#         a, b, c, d = st.columns(4)

#         a.metric("Total logs", summary.get("total", 0))
#         b.metric("Errors", summary.get("errors", 0))
#         c.metric("Warnings", summary.get("warnings", 0))
#         d.metric("Info", summary.get("info", 0))

#         st.subheader("Parsed log entries")
#         st.dataframe(
#             st.session_state.parsed_logs,
#             use_container_width=True,
#             hide_index=True
#         )

#         st.subheader("🤖 AI Investigation Report")
#         st.markdown(st.session_state.report)

#         st.download_button(
#             "Download investigation report",
#             data=st.session_state.report,
#             file_name="blackbox_investigation.txt",
#             mime="text/plain",
#             use_container_width=True
#         )

#         st.caption(
#             "AI findings are hypotheses, not proof. "
#             "Verify them against the original logs."
#         )

#     footer()


# # ---------- INVESTIGATION HISTORY ----------

# elif page == "Investigation History":
#     header()
#     st.title("📁 Investigation History")
#     st.write("Review reports generated during this session.")

#     if not st.session_state.history:
#         st.info("No investigation history yet.")
#     else:
#         for index, item in enumerate(st.session_state.history):
#             with st.expander(
#                 f"Investigation {index + 1} · {item['time']}"
#             ):
#                 st.write("Summary:", item["summary"])
#                 st.markdown(item["report"])

#                 st.download_button(
#                     "Download this report",
#                     data=item["report"],
#                     file_name=f"blackbox_report_{index + 1}.txt",
#                     key=f"download_{index}"
#                 )

#     st.caption(
#         "History is stored in the current Streamlit session "
#         "and may disappear when the session resets."
#     )
#     footer()


# # ---------- HELP ----------

# elif page == "Help":
#     header()
#     st.title("❔ Help Center")

#     with st.expander("How do I investigate an incident?", expanded=True):
#         st.write(
#             "Open New Investigation, upload a .txt or .log file "
#             "or paste logs, then click Investigate Incident."
#         )

#     with st.expander("Which log format is supported?"):
#         st.code(
#             "10:00:01 ERROR Database connection timeout"
#         )
#         st.write(
#             "The current parser expects a timestamp, a log level, "
#             "and a message. Other formats may need parser updates."
#         )

#     with st.expander("Why is the AI not responding?"):
#         st.write(
#             "Check that Ollama is running, Gemma 3:1B is installed, "
#             "and your Python dependencies are available."
#         )
#         st.code("ollama list")
#         st.code("ollama run gemma3:1b")

#     with st.expander("Can I trust every AI finding?"):
#         st.write(
#             "No. The report may contain mistakes. Verify proposed "
#             "causes and diagnostic steps against the original logs."
#         )

#     footer()


# # ---------- CONTACT ----------

# elif page == "Contact":
#     header()
#     st.title("📬 Contact the BLACKBOX Team")
#     st.write(
#         "Questions, feedback, or bug reports? "
#         "Use the team contact details below."
#     )

#     st.markdown("""
#     **BLACKBOX — AI Incident Investigation**

#     - General enquiries: `blackbox.team@example.com`
#     - Technical support: `blackbox.support@example.com`

#     **Project team**

#     - Team Member 1 — `member1@example.com`
#     - Team Member 2 — `member2@example.com`
#     - Team Member 3 — `member3@example.com`
#     - Team Member 4 — `member4@example.com`
#     """)

#     st.info(
#         "Replace the example email addresses with your team's "
#         "actual contact details before presenting the project."
#     )

#     footer()


import streamlit as st
import json
from datetime import datetime

from AiEngine import investigate_incident
from log_processor import parse_logs, summarize_logs
from database import init_db, save_investigation, get_investigations


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="BLACKBOX | AI Investigator",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# INITIALIZE DATABASE AND SESSION STATE
# ==================================================

init_db()

defaults = {
    "logged_in": False,
    "username": "",
    "theme": "Dark",
    "navigation": "Dashboard",
    "report": "",
    "summary": None,
    "parsed_logs": [],
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ==================================================
# THEME SETTINGS
# ==================================================

if st.session_state.theme == "Dark":
    bg = "#0B1020"
    panel = "#151D30"
    text = "#F1F5F9"
    accent = "#38BDF8"
    muted = "#A7B4C8"
else:
    bg = "#F4F7FB"
    panel = "#FFFFFF"
    text = "#172033"
    accent = "#0369A1"
    muted = "#536176"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg};
        color: {text};
    }}

    [data-testid="stSidebar"] {{
        background-color: {panel};
    }}

    h1, h2, h3, p, label {{
        color: {text};
    }}

    .brand {{
        font-size: 38px;
        font-weight: 800;
        letter-spacing: 4px;
        color: {accent};
    }}

    .subtitle {{
        color: {muted};
        font-size: 14px;
        letter-spacing: 2px;
    }}

    .panel {{
        background-color: {panel};
        padding: 22px;
        border-radius: 14px;
        border: 1px solid {accent}55;
        margin-bottom: 16px;
    }}

    .footer {{
        text-align: center;
        color: {muted};
        padding: 24px 8px;
        margin-top: 40px;
        border-top: 1px solid {accent}55;
        font-size: 13px;
    }}

    .stButton button {{
        border-radius: 9px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# REUSABLE HEADER AND FOOTER
# ==================================================

def header():
    st.markdown(
        '<div class="brand">BLACKBOX ⌁</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'AI-POWERED INCIDENT INVESTIGATION SYSTEM'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()


def footer():
    st.markdown(
        """
        <div class="footer">
            <b>BLACKBOX</b> · AI-Powered Incident Investigation
            <br>
            Turning system logs into actionable insights.
            <br><br>
            Contact: blackbox.team@example.com
            <br>
            © 2026 BLACKBOX · Built by the BLACKBOX team
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# LOGIN PAGE
# ==================================================

if not st.session_state.logged_in:

    st.markdown("<br><br>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 1.2, 1])

    with center:
        header()

        st.subheader("Welcome, Investigator")
        st.write("Sign in to access your investigation workspace.")

        with st.form("login_form"):
            username = st.text_input("Username")

            password = st.text_input(
                "Password",
                type="password"
            )

            submitted = st.form_submit_button(
                "Sign in →",
                use_container_width=True
            )

        if submitted:
            # DEMO LOGIN ONLY.
            # Replace with proper authentication before deployment.
            if username == "Krishna" and password == "krishna@123" or username == "dnyanda" and password == "dnyanda@123" or username == "sania" and password == "sania@123" or username == "siddhant" and password == "siddhant@123" or username == "demo" and password == "blackbox123":
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.navigation = "Dashboard"
                st.rerun()
            else:
                st.error(
                    "Invalid credentials. Check your username and password."
                )

        st.info(
            "Demo access: username demo, password blackbox123. "
            "This prototype does not provide secure authentication."
        )

    footer()
    st.stop()


# ==================================================
# SIDEBAR NAVIGATION
# ==================================================

with st.sidebar:
    st.markdown("## 🔎 BLACKBOX")
    st.caption("INVESTIGATION CONSOLE")

    st.divider()

    st.write(f"Signed in as **{st.session_state.username}**")

    pages = [
        "Dashboard",
        "New Investigation",
        "Investigation History",
        "Help",
        "Contact"
    ]

    if st.session_state.navigation not in pages:
        st.session_state.navigation = "Dashboard"

    page = st.radio(
        "NAVIGATION",
        pages,
        key="navigation"
    )

    st.divider()

    st.subheader("Appearance")

    theme_choice = st.radio(
        "Choose theme",
        ["Dark", "Light"],
        index=0 if st.session_state.theme == "Dark" else 1,
        key="theme_choice"
    )

    if theme_choice != st.session_state.theme:
        st.session_state.theme = theme_choice
        st.rerun()

    st.divider()

    if st.button("Log out", use_container_width=True):
     st.session_state.logged_in = False
     st.session_state.username = ""
     st.session_state.report = ""
     st.session_state.summary = None
     st.session_state.parsed_logs = []
     st.rerun()

    # if st.button("Log out", use_container_width=True):
    #     st.session_state.logged_in = False
    #     st.session_state.username = ""                               #useless code, as the logout button is already in the sidebar
    #     st.session_state.navigation = "Dashboard"
    #     st.rerun()
    
# if st.button("Log out", use_container_width=True):
#     st.session_state.logged_in = False                                  #redirecting to login page
#     st.session_state.username = ""
#     st.session_state.report = ""
#     st.session_state.summary = None
#     st.session_state.parsed_logs = []
#     st.rerun()



# ==================================================
# DASHBOARD
# ==================================================

if page == "Dashboard":

    header()

    st.title("Investigation Dashboard")

    st.write(
        "Analyze system logs, identify potential incidents, "
        "and review AI-generated findings."
    )

    # Load persistent database history
    records = get_investigations(st.session_state.username)

    total_investigations = len(records)

    latest_summary = (
        json.loads(records[0]["summary"])
        if records
        else {}
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Investigations", total_investigations)
    col2.metric("Latest total logs", latest_summary.get("total", 0))
    col3.metric("Latest errors", latest_summary.get("errors", 0))
    col4.metric("Latest warnings", latest_summary.get("warnings", 0))

    st.markdown(
        """
        <div class="panel">
            <h3>⚡ Incident Investigation</h3>
            <p>
                Upload a log file or paste logs to begin an AI-powered
                investigation with your local Gemma model.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # if st.button(
    #     "＋ Start New Investigation",
    #     type="primary",
    #     use_container_width=True
    # ):
    #     st.session_state.page_request = "New Investigation"
    #     st.rerun()

    st.subheader("Recent investigations")

    if records:
        for item in records[:5]:
            with st.expander(
                f"Investigation #{item['id']} — {item['created_at']}"
            ):
                st.json(json.loads(item["summary"]))
                st.markdown(item["report"])

                st.download_button(
                    "Download report",
                    data=item["report"],
                    file_name=f"blackbox_report_{item['id']}.txt",
                    mime="text/plain",
                    key=f"dashboard_download_{item['id']}"
                )
    else:
        st.info("No investigations yet. Start your first investigation.")

    footer()


# ==================================================
# NEW INVESTIGATION
# ==================================================

elif page == "New Investigation":

    header()

    st.title("🔍 New Investigation")

    st.write(
        "Upload system logs or paste them below for analysis."
    )

    uploaded_file = st.file_uploader(
        "Upload a log file",
        type=["txt", "log"]
    )

    if uploaded_file is not None:
        logs = uploaded_file.getvalue().decode(
            "utf-8",
            errors="replace"
        )
    else:
        logs = st.text_area(
            "Or paste logs here",
            height=250,
            placeholder=(
                "10:00:01 INFO API server started\n"
                "10:00:02 WARN Database response delayed\n"
                "10:00:03 ERROR Database connection timeout"
            )
        )

    if st.button(
        "🚀 Investigate Incident",
        type="primary",
        disabled=not logs.strip(),
        use_container_width=True
    ):
        try:
            with st.spinner("Parsing and summarizing logs..."):
                parsed_logs = parse_logs(logs)
                summary = summarize_logs(parsed_logs)

            with st.spinner(
                "Gemma AI is investigating the incident..."
            ):
                report = investigate_incident(logs)

            # Update current session display
            st.session_state.parsed_logs = parsed_logs
            st.session_state.summary = summary
            st.session_state.report = report

            # Save completed investigation permanently
            save_investigation(
                st.session_state.username,
                logs,
                summary,
                report
            )

            st.success("Investigation completed and saved!")

        except Exception as error:
            st.error("Investigation failed. Check the backend connection.")
            st.exception(error)

    # Display the latest completed investigation
    if st.session_state.summary is not None:

        st.divider()

        st.subheader("Incident Overview")

        summary = st.session_state.summary

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total logs", summary.get("total", 0))
        col2.metric("Errors", summary.get("errors", 0))
        col3.metric("Warnings", summary.get("warnings", 0))
        col4.metric("Info", summary.get("info", 0))

        st.subheader("Parsed Log Entries")

        st.dataframe(
            st.session_state.parsed_logs,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("🤖 AI Investigation Report")

        st.markdown(st.session_state.report)

        st.download_button(
            "Download Investigation Report",
            data=st.session_state.report,
            file_name="blackbox_investigation.txt",
            mime="text/plain",
            use_container_width=True
        )

        st.caption(
            "AI findings are hypotheses, not proof. "
            "Verify conclusions against the original logs."
        )

    footer()


# ==================================================
# INVESTIGATION HISTORY
# ==================================================

elif page == "Investigation History":

    header()

    st.title("📁 Investigation History")

    st.write(
        "View reports saved in the BLACKBOX database."
    )

    records = get_investigations(st.session_state.username)

    if not records:
        st.info("No saved investigations yet.")

    else:
        for item in records:

            with st.expander(
                f"Investigation #{item['id']} — {item['created_at']}"
            ):

                st.subheader("Log Summary")

                st.json(json.loads(item["summary"]))

                st.subheader("AI Investigation Report")

                st.markdown(item["report"])

                with st.expander("View original logs"):
                    st.code(item["logs"])

                st.download_button(
                    "Download Report",
                    data=item["report"],
                    file_name=f"blackbox_report_{item['id']}.txt",
                    mime="text/plain",
                    key=f"history_download_{item['id']}"
                )

    footer()


# ==================================================
# HELP CENTER
# ==================================================

elif page == "Help":

    header()

    st.title("❔ Help Center")

    st.write("Guidance for using BLACKBOX.")

    with st.expander("How do I investigate an incident?", expanded=True):
        st.write(
            "Open New Investigation, upload a .txt or .log file "
            "or paste your logs, and click Investigate Incident."
        )

    with st.expander("Which log formats are supported?"):
        st.code("10:00:01 ERROR Database connection timeout")
        st.write(
            "The current parser expects each log line to contain "
            "a timestamp, a log level, and a message. Other formats "
            "may require changes to log_processor.py."
        )

    with st.expander("Why is the AI not responding?"):
        st.write(
            "Check that Ollama is running and the Gemma model "
            "is installed."
        )

        st.code("ollama list")
        st.code("ollama run gemma3:1b")

    with st.expander("Where are investigations stored?"):
        st.write(
            "Investigation history is stored in the local SQLite "
            "database file named blackbox.db."
        )

    with st.expander("Can I trust every AI finding?"):
        st.write(
            "No. AI findings can be incorrect. Confirm proposed "
            "causes and diagnostic steps against the original logs."
        )

    footer()


# ==================================================
# CONTACT PAGE
# ==================================================

elif page == "Contact":

    header()

    st.title("📬 Contact the BLACKBOX Team")

    st.write(
        "Have a question, suggestion, or bug report? "
        "Contact the project team."
    )

    st.markdown(
        """
        ### BLACKBOX
        **AI-Powered Incident Investigation**

        **General enquiries**
        - blackbox.team@example.com

        **Project team**
        - Team Member 1 — member1@example.com
        - Team Member 2 — member2@example.com
        - Team Member 3 — member3@example.com
        - Team Member 4 — member4@example.com
        """
    )

    st.info(
        "Replace all example email addresses with your team's "
        "actual email addresses before your hackathon demo."
    )

    footer()
