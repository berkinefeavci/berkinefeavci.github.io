const projects = [...document.querySelectorAll('[data-category]')];
const filters = document.querySelector('.filters');
const counter = document.querySelector('#result-count');
const label = document.documentElement.lang === 'tr' ? 'proje' : 'projects';
function filter(category) {
  for (const project of projects) project.hidden = category !== 'all' && project.dataset.category !== category;
  for (const button of filters.querySelectorAll('button')) button.setAttribute('aria-pressed', String(button.dataset.filter === category));
  counter.textContent = `${projects.filter(project => !project.hidden).length} ${label}`;
}
filters.hidden = false;
filters.addEventListener('click', event => {
  const button = event.target.closest('[data-filter]');
  if (button) filter(button.dataset.filter);
});
function revealLinkedProject() {
  const id = location.hash.slice(1);
  const project = projects.find(project => project.id === id);
  if (!project) return;
  filter('all');
  project.querySelector('details').open = true;
  project.scrollIntoView({block: 'start'});
}
window.addEventListener('hashchange', revealLinkedProject);
revealLinkedProject();
