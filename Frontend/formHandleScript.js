// DOM Elements
const generateBtn = document.getElementById('generateBtn');
const resetBtn = document.getElementById('resetBtn');
const locationInput = document.getElementById('location');
const pastInhabitantsInput = document.getElementById('past-inhabitants');
const currentInhabitantsInput = document.getElementById('current-inhabitants');
const roomsInput = document.getElementById('rooms');
const dangerInput = document.getElementById('danger');
const scenarioOutput = document.getElementById('scenarioOutput');
const scenarioSection = document.querySelector('.scenario-section');

// Event Listeners
generateBtn.addEventListener('click', async () => {
    // Get input values
    const location = locationInput.value;
    const pastInhabitants = pastInhabitantsInput.value;
    const currentInhabitants = currentInhabitantsInput.value;
    const rooms = roomsInput.value;
    const danger = dangerInput.value;
    

    // Basic validation
    if ( !location || !pastInhabitants || !currentInhabitants || !rooms || !danger) {
        alert('Please fill all fields!');
        return;
    }

    try {
        // Show loading state
        generateBtn.textContent = 'Generating...';
        
        // Call backend API
        const response = await fetch('http://localhost:5000/generate-scenario', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ location, pastInhabitants, currentInhabitants, rooms, danger })
        });

        if (!response.ok) throw new Error('API call failed');
        
        // Display story
        const data = await response.json();
        scenarioOutput.innerHTML = data.scenario.replace(/\n/g, '<br>');
        scenarioSection.classList.remove('hidden');
    } catch (error) {
        alert(`Error: ${error.message}`);
    } finally {
        generateBtn.textContent = 'Generate Adventure Site!';
    }
});

// Reset button handler
resetBtn.addEventListener('click', () => {
    scenarioSection.classList.add('hidden');
    locationInput.value = '';
    pastInhabitantsInput.value = '';
    currentInhabitantsInput.value = '';
    roomsInput.value = '';
    dangerInput.value = '';
});