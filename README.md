# Streamlit Sign Up & Login System with Marks Visualization

This is a Streamlit-based web application that allows users to sign up, log in, and submit their marks for 7 subjects. After submitting, the marks are saved to a CSV file, and interactive graphs are generated using Plotly Express to visualize the data. The application also handles user sessions and persists user data for future logins.

## Features

- **Sign Up & Login**: Users can sign up with their Name, Phone, DOB, Email, and Password. Duplicate email registrations are prevented. Existing users can log in with their credentials.
- **User-Specific Folder**: Each user's data is stored in a folder named after the prefix of their email.
- **Marks Input**: After logging in, users can submit marks for 7 subjects using sliders.
- **Interactive Graphs**: The submitted marks are visualized as interactive bar and line charts using Plotly Express.
- **Persistent Data**: If the user logs out and logs back in, their previously submitted marks and graphs are automatically loaded.
- **Session Management**: The app manages user sessions to maintain login state.

## Tech Stack

- **Python**
- **Streamlit**: For building the web interface.
- **Plotly Express**: For interactive data visualization.
- **Pandas**: For handling data and saving it to CSV.
- **JSON**: For storing user credentials and managing sessions.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
   Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
   Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   
How to Use
1. Sign Up
Navigate to the "Sign Up" page and enter your details (Name, Phone, DOB, Email, and Password).
After successfully signing up, a folder will be created in the current working directory using the email's prefix.
You will be redirected to the login page.
2. Login
Existing users can log in with their email and password.
Once logged in, you will be able to submit your marks for 7 subjects using sliders.
3. Submitting Marks
After logging in, use the sliders to enter your marks for each subject.
Click "Submit", and your marks will be saved in a CSV file in your user-specific folder.
Interactive bar and line charts will be generated to visualize your marks.
4. Persistent Data
If you log out and log in again, your previously submitted marks and graphs will automatically be loaded.


Project Structure
  ```bash
  .
  ├── app.py                # Main application file
  ├── Credentials.json      # JSON file that stores user credentials
  ├── user_session.json     # JSON file to store user session data
  ├── requirements.txt      # Python dependencies
  ├── README.md             # Project documentation
  └── <user_folders>        # Folders created for each user, storing their marks in a CSV
  ```


Dependencies

Make sure to install the required Python packages by running:
  ```bash
  pip install streamlit plotly pandas
  ```

Future Improvements
Add password encryption for more secure user authentication.
Implement email verification during sign-up.
Add more detailed data visualization options (e.g., pie charts, histograms).
Enable editing of submitted marks.

### Key Points in the `README.md`:
- **Installation**: Includes steps to set up the project locally.
- **How to Use**: Clear instructions for signing up, logging in, and submitting marks.
- **Dependencies**: Lists required Python packages and instructions to install them.
- **Project Structure**: Describes the key components of the project.
- **Future Improvements**: Suggestions for enhancements that can be made.


