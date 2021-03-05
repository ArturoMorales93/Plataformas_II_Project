// Breakpoinst
const   mediumBp = matchMedia('(min-width: 768px)'),
        largeBp = matchMedia('(min-width: 1024px)'),
        xlargeBp = matchMedia('(min-width: 1200px)')
        xxlargeBp = matchMedia('(min-width: 1200px)')

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

// Banner
// const imgBannerContainer = document.getElementById('imgBannerContainer')

// const showBannerImg = media => {
//     if (media.matches) {
//         imgBannerContainer.innerHTML = `<img class="banner-img" src="/static/img/banner-img.jpg" alt="CPU">`
//     } else {
//         imgBannerContainer.innerHTML = " "
//     }
// }

// if (imgBannerContainer) {
    
//     /* Verificar que en el Sass sea la misma media query */
//     showBannerImg(largeBp)
//     largeBp.addListener(showBannerImg)
//     xlargeBp.addListener(showBannerImg)
//     xxlargeBp.addListener(showBannerImg)

// }