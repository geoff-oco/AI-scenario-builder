# RPG Scenario Generator

A web-based tool that generates AI-powered RPG adventure locations, detailing history, current events, rooms, encounters, and adventure hooks. Built with Flask for the backend and JavaScript for frontend interactions.

## Installation

### **1. Prerequisites**
- Python 3.x
- Flask
- OpenAI API key
- A web browser

### **2. Setup**
1. Clone this repository:
   ```sh
   git clone https://github.com/geoff-oco/rpg-scenario-generator.git
   cd rpg-scenario-generator
   ```

2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Rename `.env.example` to `.env`.
   - Add your OpenAI API key inside `.env`:
     ```
     OPENAI_API_KEY=your-api-key-here
     DEBUG=True
     ```

4. Run the backend server:
   ```sh
   python scenario_builder_app.py
   ```

5. Open `index.html` in a browser to use the web application.

## Usage

- Enter **location details** and information about past and present inhabitants.
- Select **size** and **danger level** of the site.
- Click **"Generate Adventure Site!"** to create a detailed scenario.
- View the AI-generated **history, rooms, encounters, and adventure hooks**.
- Click **"Try Again"** to reset and generate a new adventure site.

## File Structure

- **Frontend**
  - `index.html` → Main webpage structure.
  - `rpgstyles.css` → Styling for the webpage.
  - `formHandleScript.js` → Handles user input and API calls.

- **Backend**
  - `scenario_builder_app.py` → Flask API for generating AI-driven RPG scenarios.
  - `roomMaker.py` → Generates random room layouts based on danger level.
  - `roomRandom.py` → Determines the number of rooms based on site size.
  - `.env` → Stores API keys and environment settings (**excluded from Git**).
  - `requirements.txt` → List of Python dependencies.

## Contributing

If you'd like to contribute:
1. Fork the repository.
2. Create a new branch.
3. Make your changes and submit a pull request.

## Contact

For any questions or issues, reach out via GitHub: [geoff-oco](https://github.com/geoff-oco).
