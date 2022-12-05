new WOW().init();

const swiperHome = new Swiper(".homeSwiper", {
    direction: "vertical",
    // loop: true,
    autoplay: {
        delay: 3000,
        disableOnInteraction: false
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});

const swiperService = new Swiper(".serviceSwiper", {
    slidesPerView: 2,
    spaceBetween: 30,
    slidesPerGroup: 2,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: ".service-pagination",
        clickable: true,
    },
    autoplay: {
        delay: 3000,
        disableOnInteraction: false
    },
});

const swiperTestimonials = new Swiper(".testimonialsSwiper", {
    spaceBetween: 30,
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    autoplay: {
        delay: 3000,
        disableOnInteraction: false
    },
});

const swiperNews = new Swiper(".newsSwiper", {
    autoplay: {
        delay: 3000,
        disableOnInteraction: false
    },
    slidesPerView: 3,
    spaceBetween: 30,
    // slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});


const swiperTeam = new Swiper(".teamSwiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: ".team-pagination",
        clickable: true,
    },
    autoplay: {
        delay: 5000,
        disableOnInteraction: false
    },
});

const swiperSlide = new Swiper(".slideSwiper", {
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: ".swiper-pagination",
    },
    autoplay: {
        delay: 2000,
        disableOnInteraction: false
    },
});

const swiperMenu = new Swiper(".menuSwiper", {
    slidesPerView: 4,
    spaceBetween: 0,
    freeMode: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

let menuCategory = document.querySelectorAll('.menu__category')
let menuList = document.querySelectorAll('.menu__list')
Array.from(menuCategory).forEach((item, idx) => {
    item.setAttribute('data-id', `${idx + 1}`)
    item.addEventListener('click', () => {
        Array.from(menuList).forEach((el, index) => {
            if (index + 1 === +item.dataset.id) {
                // item.classList.add('border')
                el.classList.add('scale')
            } else {
                // item.classList.remove('border')
                el.classList.remove('scale')
            }
        })
    })
})