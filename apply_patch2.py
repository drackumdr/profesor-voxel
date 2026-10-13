path='index.html'
with open(path, encoding='utf-8', errors='ignore') as f:
    s=f.read()
# 2C
old='''function openQuiz(nb) {
  currentNotebook = nb;
  nb.mesh.visible = false;
  paused = true;
  document.exitPointerLock();
  for (const k in keys) keys[k] = false;

  const qh2 = document.getElementById('quizTitle');
  if (qh2) qh2.textContent = 'CUADERNO DE MATEM햀ICAS';

  const q = makeQuestion(player.level);
  currentAnswer = q.answer;
  qText.textContent = q.text + ' = ?';
  qInput.value = '';
  quizEl.style.display = 'flex';
  setPadFocus(10); // '0'
  setTimeout(() => qInput.focus(), 30);
}'''
new='''function openQuiz(nb) {
  currentNotebook = nb;
  nb.mesh.visible = false;
  paused = true;
  document.exitPointerLock();
  for (const k in keys) keys[k] = false;

  const qh2 = document.getElementById('quizTitle');
  if (qh2) qh2.textContent = 'CUADERNO DE MATEM햀ICAS';

  showQuestion(makeQuestion(player.level));
}'''
if old in s:
    s=s.replace(old,new)
    print('2c ok')
else:
    print('2c no')
# 2D
old2='''function openQuizCustom(cb, title = null) {
  quizCallback = cb;
  currentNotebook = null;
  const qh2 = document.getElementById('quizTitle');
  if (qh2) qh2.textContent = title || 'CUADERNO DE MATEM햀ICAS';
  const q = makeQuestion(player.level);
  currentAnswer = q.answer;
  qText.textContent = q.text + ' = ?';
  qInput.value = '';
  quizEl.style.display = 'flex';
  setPadFocus(10);
  setTimeout(() => qInput.focus(), 30);
}'''
new2='''function openQuizCustom(cb, title = null) {
  quizCallback = cb;
  currentNotebook = null;
  const qh2 = document.getElementById('quizTitle');
  if (qh2) qh2.textContent = title || 'CUADERNO DE MATEM햀ICAS';
  showQuestion(makeQuestion(player.level));
}'''
if old2 in s:
    s=s.replace(old2,new2)
    print('2d ok')
else:
    print('2d no')
# 2E
old3='''qInput.addEventListener('input', () => {
  qInput.value = qInput.value.replace(/[^0-9\-]/g, '');
});'''
new3='''qInput.addEventListener('input', () => {
  qInput.value = qInput.value.replace(/[^0-9\-]/g, '');
  if (typeof syncVerticalDigits === 'function') syncVerticalDigits();
});'''
if old3 in s:
    s=s.replace(old3,new3)
    print('2e ok')
else:
    print('2e no')
# 2F
old4='''  } else if (/^[0-9]$/.test(val)) {
    if (qInput.value.length < 8) {
      qInput.value += val;
      sfx([60 + parseInt(val, 10) * 2], 'triangle', 0.02, 0.03);
    }
  }
}'''
new4='''  } else if (/^[0-9]$/.test(val)) {
    if (qInput.value.length < 8) {
      qInput.value += val;
      sfx([60 + parseInt(val, 10) * 2], 'triangle', 0.02, 0.03);
    }
  }
  if (typeof syncVerticalDigits === 'function') syncVerticalDigits();
}'''
if old4 in s:
    s=s.replace(old4,new4)
    print('2f ok')
else:
    print('2f no')
with open(path,'w',encoding='utf-8',errors='ignore') as f:
    f.write(s)
print('done')
