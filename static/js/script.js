<script src="static/js/script.js"></script>

document.getElementById('startTracking').addEventListener('click', () => {
    fetch('/mental-tracker')
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => console.error('Error:', error));
});

document.getElementById('panicSystemBtn').addEventListener('click', () => {
    fetch('/panic-system')
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => console.error('Error:', error));
});
