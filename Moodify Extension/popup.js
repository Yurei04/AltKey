document.getElementById('shortcut-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const modeName = document.getElementById('mode-name').value.trim();
    const websites = document.getElementById('websites').value.trim().split(',');
    const shortcut = document.getElementById('shortcut').value.trim();

    if (modeName && websites && shortcut) {
        chrome.storage.sync.get(['customModes'], function(result) {
            const customModes = result.customModes || [];
            customModes.push({ modeName, websites, shortcut });
            chrome.storage.sync.set({ customModes: customModes }, function() {
                document.getElementById('status').textContent = 'Mode added!';
                document.getElementById('shortcut-form').reset();
            });
        });
    } else {
        document.getElementById('status').textContent = 'Please fill in all fields.';
    }
});


document.getElementById('chillMode').addEventListener('click', () => {
    chrome.commands.executeCommand('activate_chill_mode');
});

document.getElementById('codeMode').addEventListener('click', () => {
    chrome.commands.executeCommand('activate_code_mode');
});

document.getElementById('workMode').addEventListener('click', () => {
    chrome.commands.executeCommand('activate_work_mode');
});

document.getElementById('researchMode').addEventListener('click', () => {
    chrome.commands.executeCommand('activate_research_mode');
});
