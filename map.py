import streamlit as st
from data import resource

def display_roadmap(data):
    for category, subcategories in data.items():
        # Container for main topic and subtopics with border styling
        with st.container():
            # HTML for main topic and its subtopics border
            st.markdown(
                f"""
                <div style="border: 2px solid #007bff; border-radius: 10px; padding: 10px; margin-bottom: 10px; margin-top: 30px;">
                    <h2 style="margin-top: 0;">{category}</h2>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                """, unsafe_allow_html=True
            )
            
            # Create columns for displaying subtopics
            col1, col2, col3 = st.columns(3)
            
            # Iterate over subcategories and display them in columns
            for idx, (subcategory, content) in enumerate(subcategories.items()):
                with col1 if idx % 3 == 0 else col2 if idx % 3 == 1 else col3:
                    # Add some styling to the button
                    if st.button(subcategory, key=subcategory):
                        st.sidebar.subheader(subcategory)
                        st.sidebar.write(content['Description'])
                        if 'Links' in content:
                            for link_type, links in content['Links'].items():
                                st.sidebar.write(f"**{link_type}**")
                                for link in links:
                                    link_alias = link['alias']
                                    link_url = link['url']
                                    st.sidebar.markdown(f"- [{link_alias}]({link_url})")
            
            # Close HTML div for main topic and subtopics
            st.markdown("</div></div>", unsafe_allow_html=True)


# Main function to run the Streamlit app
def main():
    st.title("Python Learning Roadmap")
    st.write("This roadmap provides a structured guide to learning Python with relevant resources.")
    
    # Display the roadmap
    display_roadmap(resource)

if __name__ == "__main__":
    main()
