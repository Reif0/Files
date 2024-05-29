function moveRedDot() {
    let redDot = document.getElementById('redDot');
    let newX = Math.floor(Math.random() * (window.innerWidth - 20)); // 20 is the width of the dot
    let newY = Math.floor(Math.random() * (window.innerHeight - 20)); // 20 is the height of the dot
    redDot.style.left = newX + 'px';
    redDot.style.top = newY + 'px';
  }