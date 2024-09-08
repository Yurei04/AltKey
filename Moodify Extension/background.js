chrome.commands.onCommand.addListener((command) => {
    if (command === "activate_chill_mode") {
        openWebsites(['https://www.netflix.com', 'https://www.youtube.com', 'https://www.spotify.com']);
    } else if (command === "activate_code_mode") {
        openWebsites(['https://stackoverflow.com', 'https://chat.openai.com']);
    } else if (command === "activate_work_mode") {
        openWebsites(['https://mail.google.com', 'https://docs.google.com']);
    } else if (command === "activate_research_mode") {
        openWebsites(['https://scholar.google.com', 'https://wikipedia.org']);
    } else {
        // Handle custom modes
        chrome.storage.sync.get(['customModes'], function(result) {
            const customModes = result.customModes || [];
            const mode = customModes.find(mode => mode.shortcut.toLowerCase() === command.toLowerCase());
            if (mode) {
                openWebsites(mode.websites);
            }
        });
    }
});

function openWebsites(urls) {
    urls.forEach((url) => {
        chrome.tabs.create({ url });
    });
}
