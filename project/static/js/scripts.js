// Breakpoinst
const   mediumBp = matchMedia('(min-width: 768px)'),
        largeBp = matchMedia('(min-width: 1024px)'),
        xlargeBp = matchMedia('(min-width: 1200px)')
        xlargxxlargeBpeBp = matchMedia('(min-width: 1200px)')

// Banner
const imgBannerContainer = document.getElementById('imgBannerContainer')

const showBannerImg = media => {
    if (media.matches) {
        imgBannerContainer.innerHTML = `<img class="banner-img" src="static/img/banner-img.jpg" alt="CPU">`
    } else {
        imgBannerContainer.innerHTML = " "
    }
}

if (imgBannerContainer) {
    
    /* Verificar que en el Sass sea la misma media query */
    showBannerImg(largeBp)
    largeBp.addListener(showBannerImg)
    xlargeBp.addListener(showBannerImg)
    xxlargeBp.addListener(showBannerImg)

}