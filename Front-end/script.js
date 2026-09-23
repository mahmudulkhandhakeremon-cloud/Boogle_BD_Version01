document.addEventListener('DOMContentLoaded', () => {
    // 1. Functionality for Gmail and Images links
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach((link, index) => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            if (index === 0) {
                window.open('https://mail.google.com', '_blank'); // Opens Gmail
            } else {
                window.open('https://images.google.com', '_blank'); // Opens Google Images
            }
        });
    });

    // 2. Functionality for the Boogle Profile button
    const profileBtn = document.getElementById('profileBtn');
    if (profileBtn) {
        profileBtn.addEventListener('click', () => {
            alert('Boogle Profile: Welcome! Your profile settings will be here.');
        });
    }

// 3. Trigger search and redirect to Boogle Searching Page
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                const query = searchInput.value.trim();
                if (query) {
                    // এটি সার্চ টারอมসহ আপনাকে search.html পেজে নিয়ে যাবে
                    window.location.href = `search.html?q=${encodeURIComponent(query)}`;
                }
            }
        });
    }

    // 4. Functionality for the microphone icon (Voice search simulation)
    const micIcon = document.querySelector('.mic-icon');
    if (micIcon) {
        micIcon.addEventListener('click', () => {
            alert('Listening... Browser permission is required to enable the microphone.');
        });
    }

    // 5. Functionality for the GitHub shortcut
    const githubShortcut = document.getElementById('githubShortcut');
    if (githubShortcut) {
        githubShortcut.addEventListener('click', () => {
            window.open('https://github.com', '_blank'); // You can put your GitHub link here
        });
    }

    // 6. Functionality for the Add Shortcut button
    const addShortcut = document.getElementById('addShortcut');
    if (addShortcut) {
        addShortcut.addEventListener('click', () => {
            const siteName = prompt('Enter the shortcut name:');
            const siteUrl = prompt('Enter the website URL:');
            if (siteName && siteUrl) {
                alert(`Shortcut "${siteName}" has been added successfully!`);
                // Code to dynamically add the shortcut can be written here
            }
        });
    }
});