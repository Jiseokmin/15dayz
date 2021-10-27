class CircularText {
    constructor (o) {
      this.el = document.querySelector(o.el)
      this.radius = o.radius
      this.init()
    }
    
    init() {
      this.text = this.el.innerHTML.split('')
      this.pos = window.getComputedStyle(this.el, null).getPropertyValue('position')
      this.el.style.position = this.pos === 'static' ? 'relative' : this.pos
      this.el.innerHTML = ''
      this.text.forEach((st, ind) => {
        const i = ind / this.text.length
        const s = document.createElement('span')
        s.innerHTML = st
        this.el.appendChild(s)
        const w = s.offsetWidth
        const h = parseInt(window.getComputedStyle(s, null).getPropertyValue('font-size'), 10)
        const x = Math.sin(i * Math.PI * 2) * this.radius
        const y = -Math.cos(i * Math.PI * 2) * this.radius
        const css = {
          position: 'absolute',
          zIndex: ind,
          top: '50%',
          left: '50%',
          margin: `${-h * 0.5}px 0 0 ${-w * 0.5}px`,
          transform: `translate3D(${x}px, ${y}px, 0) rotate(${
        i * 360}deg)`,
        }
        Object.assign(s.style, css)
        s.style.setProperty('--index', ind)
      })
    }
    
    debug() {
      this.circle = document.createElement('div')
      this.el.appendChild(this.circle)
      const css = {
        borderRadius: '50%',
        background: 'red',
        position: 'relative',
        zIndex: -1,
        width: `${this.radius * 2}px`,
        height: `${this.radius * 2}px`,
      }
      Object.assign(this.el.style, css)
    }
  }
  
  const circular = new CircularText({
    el: '.circular-text',
    radius: 130
  })
  
  