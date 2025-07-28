chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    const API_URL = 'http://127.0.0.1:5000';

    if (request.action === 'track') {
        fetch(`${API_URL}/track`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: request.url })
        })
        .then(response => {
            if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
            return response.json();
        })
        .then(data => sendResponse(data))
        .catch(error => sendResponse({ error: error.message }));
        return true;
    }

    if (request.action === 'history') {
        fetch(`${API_URL}/history`)
            .then(response => {
                if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
                return response.json();
            })
            .then(data => sendResponse(data))
            .catch(error => sendResponse([]));
        return true;
    }

    if (request.action === 'clear') {
        fetch(`${API_URL}/clear`, { method: 'POST' })
            .then(response => {
                if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
                return response.json();
            })
            .then(data => sendResponse(data))
            .catch(error => sendResponse({ status: 'error' }));
        return true;
    }
});