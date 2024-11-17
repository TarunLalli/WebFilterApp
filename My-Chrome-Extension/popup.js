document.getElementById("scrape-and-transform").addEventListener("click", () => {
    // Query the active tab in the current window
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs.length === 0) {
        console.error("No active tab found.");
        return;
      }
  
      // Execute the content script in the active tab
      chrome.scripting.executeScript(
        {
          target: { tabId: tabs[0].id },
          files: ["content.js"],
        },
        (results) => {
          if (chrome.runtime.lastError) {
            console.error(`Error executing content.js: ${chrome.runtime.lastError.message}`);
          } else {
            console.log("Content script executed successfully.", results);
          }
        }
      );
    });
  });
  