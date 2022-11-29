// let btnStore = document.querySelector('.store-btn')
// let storeCard = document.getElementsByClassName('store__card-hide')
// // let storeCardNode = document.querySelectorAll('.hide-card')
//
//
// btnStore.addEventListener('click', function () {
//     Array.from(storeCard).map((e) => e.style.display = 'block', btnStore.style.display = 'none')
// })


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

const swiper = new Swiper(".slideSwiper", {
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