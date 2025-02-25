from flask import Flask, request, jsonify
from flask_cors import CORS  # Handle cross-origin requests
import requests  # For making API calls
from openai import OpenAI # Import OpenAI module
from Methods.roomRandom import roomNumber
from Methods.roomMaker import roomCollection
import markdown
import bleach
import os
from dotenv import load_dotenv
from textwrap import dedent

load_dotenv()


app = Flask(__name__)
CORS(app, resources={r"/generate-scenario": {"origins": "*"}})  # Restrict origins

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    )
 # Set OpenAI API key)

@app.route('/generate-scenario', methods=['POST']) # routing for generate-story endpoint
def generate_scenario():
    try:
        # Get JSON data from frontend
        data = request.json
        location = data['location'] # pull words from the data
        pastInhabitants = data['pastInhabitants']
        currentInhabitants = data['currentInhabitants']
        rooms = data['rooms']
        danger = int(data['danger'])

        numberOfRooms = roomNumber(rooms) 
        print(f"Number of Rooms: {numberOfRooms}")

        roomPrompt = roomCollection(numberOfRooms, danger)
        print(f"roomPrompt:\n{roomPrompt}")


        
        prompt = dedent(f"""
            --------------------------------------------------
            Adventure Site History:
            Provide exactly 150 words describing the history of the adventure site. Base this on the pastInhabitants and the location variable.

            What's Happening Now?:
            Provide exactly 150 words describing what is occurring in the adventure site now. Base this on the history, the location, and the currentInhabitants variable.

            General Features:
            Based on the location, pastInhabitants, and currentInhabitants, list general features of the site. Describe the appearance of doors, walls, floors, as well as smells, sounds, and lighting. Each description must use no more than 10 words.

            Room Blocks:
            For each room (using roomPrompt and roomNumber variables), output a room block with the following:
            - A header with a title and room number.
            - A 100-word description of the room.
            - Lists for enemies, traps, and treasure.
            - A sub-heading Features that details lighting and any other notable characteristics.
            - Dimensions of the room in feet and details on doors/portals/exits/entries.

            Random Encounter Table:
            Create a d10 table of random encounters based on whats happening now and the currentInhabitants.

            Adventure Hooks:
            Provide several adventure hooks inspired by treasures, enemies, NPCs, the history, and current events at the site.

            Variables Provided:
            - location: {location}
            - pastInhabitants: {pastInhabitants}
            - currentInhabitants: {currentInhabitants}
            - roomNumber (the total number of rooms): {numberOfRooms}
            - roomPrompt (a large string containing room blocks describing features of a room): {roomPrompt}

            Note: Do not include system-specific mechanical jargon (e.g., numerical DCs). Use qualitative terms like easy, standard, hard, elite, boss level, mobs, minions, etc.

            Your output must strictly adhere to the format, word counts, and style detailed above.
            --------------------------------------------------
            """)

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
                ]
            )

        # Extract generated text from the response
        scenario = completion.choices[0].message.content
        print(scenario)

        # Convert Markdown to HTML
        scenario_html = markdown.markdown(scenario)

        # Sanitize HTML
        scenario_safe = bleach.clean(scenario_html, strip=True)


        return jsonify({"scenario": scenario_safe})

    except Exception as e:
        print(f"Error during API call: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    debug_mode = os.getenv("DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode)