const app = document.querySelector('#app');

async function loadTemplate(path) {
  const response = await fetch(path);

  if (!response.ok) {
    throw new Error(`Could not load template: ${path}`);
  }

  const source = await response.text();

  return Handlebars.compile(source);
}

async function renderHome() {
  const template = await loadTemplate(
    '/templates/home.handlebars'
  );

  const response = await fetch('/api/contacts');
  const contacts = await response.json();
  contacts.forEach(contact => {
    contact.tags = contact.tags ? contact.tags.split(',').map(tag => tag.trim()) : null;
  });

  app.innerHTML = template({contacts});

  const cards = Array.from(document.querySelectorAll('.contact-card'));
  const searchField = document.getElementById('search');
  searchField.addEventListener('input', event => {
    const input = event.target.value.trim().toLowerCase();

    cards.forEach(card => {
      card.classList.toggle('d-none', !nameMatches(card, input));
    });
  });

  const cardsContainer = document.querySelector('.cards-container');
  cardsContainer.addEventListener('click', event => {
    if (event.target.classList.contains('badge')) {
      cards.filter(card => {
        return !card.classList.contains('d-none') && !tagMatches(card, event.target.textContent);
      }).forEach(card => card.classList.add('d-none'));
    }
  })

  cardsContainer.addEventListener('click', event => {
    if (event.target.href && event.target.href.includes('#contacts/delete/')) {
      if (confirm('Do you want to delete this contact?')) deleteContact(event.target);
    }
  });

  const clearButton = document.getElementById('clear-filter');
  clearButton.addEventListener('click', () => {
    const input = searchField.value.trim().toLowerCase();

    cards.forEach(card => {
      card.classList.toggle('d-none', !nameMatches(card, input));
    });
});
}

async function renderContactForm() {

  const template = await loadTemplate('/templates/contact-form.handlebars');

  app.innerHTML = template();
}

async function renderEditForm() {
  const id = window.location.hash.split('/')[2];

  const response = await fetch(`/api/contacts/${id}`);

  if (!response.ok) {
    throw new Error('Unable to load contact');
  }

  const contact = await response.json();

  const template = await loadTemplate('/templates/edit-form.handlebars');

  app.innerHTML = template(contact);
}

async function renderPage() {
  const route = window.location.hash;

  try {
    if (route === '#contacts/new') {
      await renderContactForm();
    } else if (route.includes('#contacts/edit/')){
      await renderEditForm();
    } else {
      await renderHome();
    }
  } catch (error) {
    console.error(error);
    app.textContent = 'Unable to load the requested page.';
  }
}

async function saveContact(form) {
  const data = Object.fromEntries(new FormData(form));

  const isEditing = Boolean(data.id);

  const url = isEditing ? `/api/contacts/${data.id}` : '/api/contacts/';

  const method = isEditing ? 'PUT' : 'POST';

  try {
    const response = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw Error('Could not save contact');
    }

    alert('Contact saved successfully!');
  } catch (error) {
    alert(error.message);
  } finally {
    await renderHome();
  }
}

async function deleteContact(target) {
  const id = Number(target.href.split('/').pop());
  try {
    const response = await fetch(`/api/contacts/${id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      },
    });

    if (!response.ok) {
      throw Error('Could not delete contact');
    }

    alert('Contact deleted successfully!');
  } catch (error) {
    alert(error.message);
  } finally {
    await renderHome();
  }
}

function nameMatches(card, input) {
  return card.querySelector('.full-name').textContent
    .toLowerCase()
    .includes(input);
}

function tagMatches(card, tag) {
  return Array.from(card.querySelectorAll('.badge'))
    .map(badge => badge.textContent)
    .includes(tag);
}

// Listen for navigation
window.addEventListener('hashchange', renderPage);

// Initial page load
renderPage();

document.addEventListener('submit', event => {
  event.preventDefault();
  saveContact(event.target);
});