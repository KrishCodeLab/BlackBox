
import streamlit as st

from AiEngine import investigate_incident
from log_processor import parse_logs, summarize_logs


# ---------- PAGE SETTINGS ----------

st.set_page_config(
    page_title="BLACKBOX | AI Investigator",
    page_icon="🔎",
    layout="wide"
)


# ---------- HEADER ----------

st.title("🔎 BLACKBOX")
st.caption("AI-powered incident investigation using local AI")

st.markdown(
    "Upload system logs, identify errors, and investigate "
    "possible root causes using your local Gemma model."
)

st.divider()


# ---------- LOG INPUT ----------

st.subheader("1. Provide system logs")

uploaded_file = st.file_uploader(
    "Upload a log file",
    type=["txt", "log"]
)

if uploaded_file is not None:
    raw_logs = uploaded_file.getvalue().decode(
        "utf-8",
        errors="replace"
    )
else:
    raw_logs = st.text_area(
        "Or paste your logs here",
        height=220,
        placeholder=(
            "10:00:01 INFO API server started\n"
            "10:00:03 WARN Database response time elevated\n"
            "10:00:05 ERROR Database connection timeout"
        )
    )


# ---------- INVESTIGATION ----------

if st.button(
    "🔍 Investigate Incident",
    type="primary",
    disabled=not raw_logs.strip(),
    use_container_width=True
):
    try:
        with st.spinner("Processing logs..."):
            parsed_logs = parse_logs(raw_logs)
            summary = summarize_logs(parsed_logs)

        with st.spinner(
            "Gemma is investigating the incident..."
        ):
            report = investigate_incident(raw_logs)

        st.session_state["summary"] = summary
        st.session_state["parsed_logs"] = parsed_logs
        st.session_state["report"] = report

    except Exception as error:
        st.error(
            "Investigation failed. Check that Ollama is running, "
            "the Gemma model is installed, and your Python "
            "dependencies are available."
        )
        st.code(str(error))


# ---------- RESULTS ----------

if "summary" in st.session_state:

    st.divider()
    st.subheader("2. Incident overview")

    summary = st.session_state["summary"]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total logs", summary.get("total", 0))
    col2.metric("Errors", summary.get("errors", 0))
    col3.metric("Warnings", summary.get("warnings", 0))
    col4.metric("Info", summary.get("info", 0))

    st.subheader("3. Parsed log entries")

    st.dataframe(
        st.session_state["parsed_logs"],
        use_container_width=True,
        hide_index=True
    )

    st.subheader("4. AI investigation report")

    st.markdown(st.session_state["report"])

    st.download_button(
        label="Download investigation report",
        data=st.session_state["report"],
        file_name="blackbox_investigation.txt",
        mime="text/plain",
        use_container_width=True
    )

    st.caption(
        "AI-generated findings are hypotheses, not proof. "
        "Verify conclusions against the original logs."
    )

else:
    st.info(
        "Upload or paste logs, then select "
        "'Investigate Incident' to begin."
    )
