// Breakpoinst
const   mediumBp = matchMedia('(min-width: 768px)'),
        largeBp = matchMedia('(min-width: 1024px)'),
        xlargeBp = matchMedia('(min-width: 1200px)'),
        xxlargeBp = matchMedia('(min-width: 1440px)')

// arroUpButton
const arroUpButton = document.getElementById('arroUpButton')

// Header
const header = document.getElementById('header')
const navbar = document.getElementById('navbar')
const iconContainer = document.getElementById('iconContainer')

const changeNavbar = () => {
    if (scrollY > 0) {
        arroUpButton.classList.add('arrow-up-show')
        header.classList.add('header-scrolled')
    } else {
        arroUpButton.classList.remove('arrow-up-show')
        header.classList.remove('header-scrolled')
    }
}

document.addEventListener('scroll', changeNavbar)