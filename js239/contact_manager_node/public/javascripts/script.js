const app = document.querySelector('#app');

// Load a template file and compile it
async function loadTemplate(path) {
  const response = await fetch(path);

  if (!response.ok) {
    throw new Error(`Could not load template: ${path}`);
  }

  const source = await response.text();

  return Handlebars.compile(source);
}

// Render home page
async function renderHome() {
  const template = await loadTemplate(
    '/templates/home.handlebars'
  );

  app.innerHTML = template();
}

// Render contact form
async function renderContactForm() {
  const template = await loadTemplate(
    '/templates/contact-form.handlebars'
  );

  app.innerHTML = template();
}

// Decide which view to display
async function renderPage() {
  const route = window.location.hash;

  try {
    if (route === '#contacts/new') {
      await renderContactForm();
    } else {
      await renderHome();
    }
  } catch (error) {
    console.error(error);
    app.textContent = 'Unable to load the requested page.';
  }
}

// Listen for navigation
window.addEventListener('hashchange', renderPage);

// Initial page load
renderPage();