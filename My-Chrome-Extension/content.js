(async () => {
    try {
      // Scrape the page source code
      const htmlContent = document.documentElement.outerHTML;
  
      // Log the scraped source code to verify
      console.log("Scraped HTML Content:", htmlContent);
  
      // Send the source code to the backend server
      const response = await fetch("http://localhost:5000/process", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ html: htmlContent }),
      });
  
      // Check if the response is OK
      if (!response.ok) {
        console.error("Failed to fetch modified HTML:", response.status, response.statusText);
        return;
      }
  
      // Parse the JSON response
      const { modifiedHtml } = await response.json();
  
      if (!modifiedHtml) {
        console.error("No modified HTML received from the server.");
        return;
      }
  
      // Replace the current source code
      document.documentElement.innerHTML = modifiedHtml;
      console.log("Page content updated successfully.");
    } catch (error) {
      console.error("An error occurred:", error);
    }
  })();
  