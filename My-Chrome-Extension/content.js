(async () => {
    // Scrape the page source code
    const htmlContent = document.documentElement.outerHTML;
  
    // Send the source code to the backend server
    const response = await fetch("http://localhost:5000/process", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ html: htmlContent })
    });
  
    const { modifiedHtml } = await response.json();
  
    // Replace the current source code
    document.documentElement.innerHTML = modifiedHtml;
  })();
  