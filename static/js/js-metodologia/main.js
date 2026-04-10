/* ━━━━ Demo de la mini-lección en el masthead ━━━━ */
function selectDemo(el, correct) {
  const opts = document.querySelectorAll('#demoopts .demo-option');
  opts.forEach(o => o.classList.remove('correct','wrong'));
  el.classList.add(correct ? 'correct' : 'wrong');
}

/* ━━━━ Lección interactiva principal ━━━━ */
let selectedOption = null;
let isCorrect = false;
let answered = false;

function selectAnswer(el, correct) {
  if (answered) return;
  const opts = document.querySelectorAll('#answerGrid .answer-option');
  opts.forEach(o => o.classList.remove('selected'));
  el.classList.add('selected');
  selectedOption = el;
  isCorrect = correct;
  document.getElementById('confirmBtn').disabled = false;
}

function confirmAnswer() {
  if (!selectedOption || answered) return;
  answered = true;

  const fb = document.getElementById('feedbackEl');
  const fbTitle = document.getElementById('feedbackTitle');
  const fbText = document.getElementById('feedbackText');
  const btn = document.getElementById('confirmBtn');

  if (isCorrect) {
    selectedOption.classList.add('correct-ans');
    fb.className = 'lesson-feedback show correct';
    fbTitle.innerHTML = '¡Excelente análisis! +160 XP &nbsp;<svg width="14" height="14" viewBox="0 0 14 14" fill="none" style="display:inline-block;vertical-align:middle;"><polygon points="7,1 8.5,4.8 12.8,5.1 9.7,7.8 10.7,12 7,9.7 3.3,12 4.3,7.8 1.2,5.1 5.5,4.8" fill="#D4A820"/></svg>';
    fbText.textContent = 'Correcto. El colapso romano fue multicausal: presiones bárbaras externas, crisis fiscal, debilidad política interna y fragmentación del ejército. Ningún factor aislado explica el proceso.';
    document.getElementById('lessonProgress').style.width = '70%';
  } else {
    selectedOption.classList.add('wrong-ans');
    // Mostrar correcta
    const opts = document.querySelectorAll('#answerGrid .answer-option');
    opts[1].classList.add('correct-ans');
    fb.className = 'lesson-feedback show incorrect';
    fbTitle.textContent = 'No exactamente — sigue intentando';
    fbText.textContent = 'Esa opción identifica solo un factor. El historiador Edward Gibbon y la historiografía moderna señalan que el colapso fue un proceso complejo con múltiples causas simultáneas.';
  }

  btn.textContent = 'Continuar →';
  btn.disabled = false;
  btn.onclick = () => alert('¡Avanzarías a la siguiente pregunta!');
}

/* ━━━━ Scroll suave a fases ━━━━ */
function scrollToPhase(id, navItem) {
  document.getElementById(id).scrollIntoView({ behavior: 'smooth', block: 'start' });
  document.querySelectorAll('.phase-nav-item').forEach(el => el.classList.remove('active'));
  navItem.classList.add('active');
}

/* ━━━━ Animación barra XP al aparecer ━━━━ */
const xpBar = document.getElementById('xpBarFill');
if (xpBar) {
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        setTimeout(() => { xpBar.style.width = '68%'; }, 300);
        obs.unobserve(e.target);
      }
    });
  }, { threshold: 0.3 });
  obs.observe(xpBar);
}
