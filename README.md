# Advertisement Poster Generator

## Overview
The **Advertisement Poster Generator** is a Streamlit-based application that generates advertisement posters using a text-to-image model and automatically sends them to a list of stored phone numbers via WhatsApp.

## Features
- **Text-to-Image Generation**: Uses `stabilityai/stable-diffusion-xl-base-1.0` from Hugging Face to generate images based on user input.
- **Database Integration**: Retrieves phone numbers from a MySQL database (`visiting_card_details`).
- **Automated WhatsApp Messaging**: Uses `pywhatkit` to send generated images to stored contacts.
- **Streamlit UI**: Provides an interactive interface for users to input their desired image description and generate posters.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- MySQL
- WhatsApp Web (logged in on the system for `pywhatkit` to function correctly)

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/sohamfcb/ad-poster-generator.git
   cd ad_poster_generator
   ```

2. **Set up a virtual environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the `.env` file**
   Create a `.env` file in the project directory and add your Hugging Face API token:
   ```
   HF_TOKEN=<your_huggingface_api_token>
   ```

5. **Configure MySQL Database**
   - Ensure MySQL is running.
   - Create a database named `visiting_card_details`.
   - Create a table named `details` with the following schema:
     ```sql
     CREATE TABLE details (
         id INT AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(255),
         company VARCHAR(255),
         job_role VARCHAR(255),
         address TEXT,
         phone VARCHAR(20),
         phone2 VARCHAR(20),
         email VARCHAR(255),
         website VARCHAR(255)
     );
     ```
   - Populate the table with required contact details.

## Usage
1. **Run the application**
   ```bash
   streamlit run app.py
   ```
2. **Enter an image description** in the provided text box.
3. **Click 'Generate Image'** to create the advertisement poster.
4. **The generated image will be displayed** on the Streamlit interface.
5. **The image will be automatically sent** to the phone numbers retrieved from the database.

## Technologies Used
- **Python**
- **Streamlit** - Web app framework
- **Hugging Face Inference API** - Stable Diffusion model for image generation
- **MySQL** - Database for storing contact details
- **PyWhatKit** - WhatsApp automation
- **PIL (Pillow)** - Image handling
- **dotenv** - Environment variable management

## Folder Structure
```
.
├── app.py                 # Main application script
├── db.sql                 # MySQL queries (excluding personal data)
├── requirements.txt       # List of dependencies
├── .gitignore             # Files to ignore in Git
├── .env                   # Environment variables (Not included in repo)
└── README.md              # Project documentation
```

## Notes
- The script introduces a **10-second delay** between sending messages to prevent spam detection by WhatsApp.
- The database should be updated with valid phone numbers before running the application.

## Acknowledgments
- [Hugging Face](https://huggingface.co/) for their powerful text-to-image models.
- [Streamlit](https://streamlit.io/) for the interactive UI.
- [PyWhatKit](https://github.com/Ankit404butfound/PyWhatKit) for WhatsApp automation.
