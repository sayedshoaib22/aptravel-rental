(function() {
  const schemaUrl = '/schema.json';
  fetch(schemaUrl)
    .then(response => {
      if (!response.ok) throw new Error('Schema JSON not found');
      return response.json();
    })
    .then(data => {
      const script = document.createElement('script');
      script.type = 'application/ld+json';
      script.textContent = JSON.stringify(data);
      document.head.appendChild(script);
    })
    .catch(error => {
      console.warn('schema.js failed to load schema.json:', error);
    });
})();
