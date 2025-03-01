import streamlit as st

def show():
    st.title("Legal Resources")

    st.subheader("Official Legal Websites")
    st.write("Here are some official legal resources you can refer to for more information:")

    # List of resources
    resources = {
        "India Legal Information": "https://indiankanoon.org/",
        "U.S. Federal Law": "https://www.usa.gov/federal-agencies",
        "UK Government Legal Services": "https://www.gov.uk/government/organisations",
        "European Union Legal Resources": "https://europa.eu/european-union/law_en",
        "Australian Legal Resources": "https://www.legislation.gov.au/"
    }

    for title, url in resources.items():
        st.markdown(f"[{title}]({url})")

    st.subheader("Legal Guides")
    st.write("Here are some helpful legal guides that can assist with understanding different aspects of law:")

    # Example legal guides
    guides = {
        "How to Write a Contract": "https://www.nolo.com/legal-encyclopedia/how-to-write-a-contract-29837.html",
        "Understanding NDAs": "https://www.rocketlawyer.com/article/what-is-an-nda.rl",
        "Divorce Law Guide": "https://www.nolo.com/legal-encyclopedia/divorce-law",
        "How to Create a Will": "https://www.legalzoom.com/articles/how-to-write-a-will",
    }

    for title, url in guides.items():
        st.markdown(f"[{title}]({url})")

    st.subheader("Relevant Laws")
    st.write("You can look up relevant laws here:")

    # List of legal databases for looking up laws
    laws = {
        "Indian Legal Codes": "https://www.indiankanoon.org/",
        "U.S. Federal Laws": "https://www.law.cornell.edu/uscode/text",
        "United Kingdom Statutes": "https://www.legislation.gov.uk/",
    }

    for title, url in laws.items():
        st.markdown(f"[{title}]({url})")
        