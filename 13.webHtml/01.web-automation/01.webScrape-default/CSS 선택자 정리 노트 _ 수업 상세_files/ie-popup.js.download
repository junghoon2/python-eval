const clickFunc = function() {
  const background = document.querySelector('.PopupIEBrowser--background')
  if (background) {
    background.style.display = 'none'
  }
}

window.addEventListener('click', clickFunc)

if (typeof window !== 'undefined') {
  const background = document.querySelector('.PopupIEBrowser--background')
  if (!background) {
    window.removeEventListener('click', clickFunc)
  }
}
