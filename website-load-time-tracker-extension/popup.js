document.addEventListener('DOMContentLoaded', () => {
    const urlInput = document.getElementById('urlInput');
    const trackBtn = document.getElementById('trackBtn');
    const clearBtn = document.getElementById('clearBtn');
    const resultText = document.getElementById('resultText');
    const analysisText = document.getElementById('analysisText');
    const historyBody = document.getElementById('historyBody');
    const previewText = document.getElementById('previewText');
    const previewFrame = document.getElementById('previewFrame');

    // Load history on popup open
    fetchHistory();

    trackBtn.addEventListener('click', () => {
        const url = urlInput.value.trim();
        if (!url) return;

        trackBtn.disabled = true;
        resultText.textContent = 'Tracking...';
        previewText.textContent = 'Loading preview...';
        previewFrame.style.display = 'none';

        chrome.runtime.sendMessage({ action: 'track', url }, response => {
            trackBtn.disabled = false;
            if (response.error) {
                resultText.innerHTML = `<span class="error">Error: ${response.error}</span>`;
                previewText.textContent = 'Preview unavailable due to error';
                previewFrame.style.display = 'none';
                return;
            }

            // Update result
            resultText.textContent = `
                URL: ${response.url}
                Load Time: ${response.load_time.toFixed(2)}ms
                Status: ${response.status}
            `;

            // Update AI analysis
            analysisText.innerHTML = `
                ${response.analysis.insights.join('<br>') || 'No insights available'}
                ${response.analysis.comparison}
            `;

            // Update preview
            previewText.style.display = 'none';
            previewFrame.style.display = 'block';
            previewFrame.src = response.url;

            // Refresh history
            fetchHistory();
        });
    });

    clearBtn.addEventListener('click', () => {
        chrome.runtime.sendMessage({ action: 'clear' }, response => {
            if (response.status === 'success') {
                fetchHistory();
                resultText.textContent = 'No data yet';
                analysisText.textContent = 'Track a website to see AI insights';
                previewText.textContent = 'Track a website to see its preview';
                previewText.style.display = 'block';
                previewFrame.style.display = 'none';
            }
        });
    });

    function fetchHistory() {
        chrome.runtime.sendMessage({ action: 'history' }, response => {
            historyBody.innerHTML = '';
            response.forEach(entry => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${entry.url}</td>
                    <td>${entry.load_time.toFixed(2)}</td>
                    <td>${entry.status}</td>
                    <td>${new Date(entry.timestamp).toLocaleString()}</td>
                `;
                historyBody.appendChild(row);
            });
        });
    }
});