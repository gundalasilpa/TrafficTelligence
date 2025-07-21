document.getElementById('trafficForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Fake Prediction Logic (for UI Demo only)
    const randomVolume = Math.floor(Math.random() * 1000) + 100;
    
    // Redirect with fake result to result.html
    window.location.href = `result.html?result=${randomVolume}`;
});