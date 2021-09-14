window.onload = () => {
  // Comment Code
  const codes = [...document.getElementsByClassName("code")]; // Grab all the code elements
  // Do css comments
  codes
    .filter((code) => {
      return code.classList.contains("css"); // Filter it for css code boxes
    })
    .forEach((code) => {
      // For each code box
      const lines = [...code.getElementsByTagName("span")]; // Grab all its lines
      lines.forEach((line) => {
        // For each line
        line.innerHTML = line.innerHTML // Surround the comments with span.comment
          .replace("/*", '<span class="comment">/*')
          .replace("*/", "*/</span>");
      });
    });
};
