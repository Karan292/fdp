import streamlit as st  # Import Streamlit library

# -------------------- App Title --------------------
st.title("🎓 Simple Marks & Grade Calculator")
# Displays the main title at the top of the app

# -------------------- Input: Number of Subjects --------------------
subjects = st.number_input(
    "Number of subjects",  # Label text shown to the user
    min_value=1,           # Minimum allowed value
    max_value=10,          # Maximum allowed value
    value=5                # Default value (pre-filled)
)
# This takes how many subjects the student has

# -------------------- Input: Marks for Each Subject --------------------
marks = []  # Empty list to store marks
for i in range(int(subjects)):  # Repeat input for each subject
    mark = st.number_input(
        f"Marks for subject {i+1}",  # Dynamic label (Subject 1, 2, 3...)
        min_value=0,                 # Minimum marks allowed
        max_value=100                # Maximum marks allowed
    )
    marks.append(mark)  # Add each entered mark to the list

# -------------------- Calculate Results --------------------
if st.button("Calculate"):  # When the user clicks the button
    total = sum(marks)             # Add all marks to get total
    percentage = total / subjects  # Calculate average percentage

    # Display total and percentage
    st.write(f"Total Marks: {total}")
    st.write(f"Percentage: {percentage:.2f}%")  # Round to 2 decimal places

    # -------------------- Grade Calculation --------------------
    if percentage >= 90:
        st.success("Grade: A+")   # Green success message
    elif percentage >= 75:
        st.info("Grade: A")       # Blue info message
    elif percentage >= 60:
        st.info("Grade: B")
    elif percentage >= 50:
        st.warning("Grade: C")    # Yellow warning message
    else:
        st.error("Grade: Fail")   # Red error message
