import domready from 'domready'
import Gallery from './components/gallery'
import SizeChart from './components/sizechart'
import NestedLists from './components/nested-lists'
import Drawer from './components/drawer'
import PasswordSecurity from './components/password-security'
import Carousel from './components/carousel'
import AnchorsNav from './components/anchors-nav'
import Smoothscroll from './components/smoothscroll'
import {TweenMax, Power3} from 'gsap'
import Basket from './components/basket'
import FileInput from './components/fileinput'
import SelectNav from './components/select-nav'
import HeaderSubmenu from './components/header-submenu'
import PageLoading from './components/page-loading'
import LocomotiveScroll from './modules/ScrollManager'

class App {
  constructor() {
    // console.log('[Unlabel App]');

    // Signature
    if (navigator.userAgent.toLowerCase().indexOf('chrome') > -1) {
        const args = ['\n %c Built with <3, by Unlabel. https://unlabel.us/ \n\n', 'background: #DEEDEE; padding:5px 0; color: #232323;'];
        
        window.console.log.apply(console, args);

    } else if (window.console) {
        window.console.log('[Built with <3, by Unlabel.]');
    }

    this.browserCheck()
    this.initAnimations()
    this.initComponents()
  }
  browserCheck() {
    window.Modernizr.addTest('webkit', 'WebkitAppearance' in document.documentElement.style)
  }
  initAnimations() {
    // Default easing for all components
    TweenMax.defaultEase = Power3.easeOut
  }
  initComponents() {

    //Page Loading
    new PageLoading();

    // Locomotive Scroll
    new LocomotiveScroll({
        container: $('.unlabel-scroll'),
        selector: '.js-scroll',
        smooth: true,
        smoothMobile: true,
        mobileContainer: $(document),
        getWay: false,
        getSpeed: false
    });

    // Gallery
    const galleries_arr = [].slice.call(document.querySelectorAll('.gallery'))
    galleries_arr.forEach((el) => {
      new Gallery({
        el: el
      })
    })

        // Sizeharts
    const sizecharts_arr = [].slice.call(document.querySelectorAll('.sizechart'))
    sizecharts_arr.forEach((el) => {
      new SizeChart({
        el: el
      })
    })

    // Nested Lists
    const nested_lists_arr = [].slice.call(document.querySelectorAll('.nested-lists'))
    nested_lists_arr.forEach((el) => {
      new NestedLists({
        el: el
      })
    })

    // Drawers
    const drawers_arr = [].slice.call(document.querySelectorAll('.drawer'))
    drawers_arr.forEach((el) => {
      new Drawer({
        el: el,
        options: {
          closeSelector: '.drawer__close, .drawer__backdrop, a[href="#close-drawer"]'
        }
      })
    })


    // Password Security
    const passwordSecurity_arr = [].slice.call(document.querySelectorAll('.password-security'))
    passwordSecurity_arr.forEach((el) => {
      new PasswordSecurity({
        el: el
      })
    })


    // Carousel
    const carousel_arr = [].slice.call(document.querySelectorAll('.carousel'))
    carousel_arr.forEach((el) => {
      new Carousel({
        el: el
      })
    })

    // Anchors Nav
    const anchorsNav_arr = [].slice.call(document.querySelectorAll('.anchors-nav'))
    anchorsNav_arr.forEach((el) => {
      new AnchorsNav({
        el: el
      })
    })

    // Smoothscroll
    const smoothscroll_arr = [].slice.call(document.querySelectorAll('.smoothscroll'))
    smoothscroll_arr.forEach((el) => {
      new Smoothscroll({
        el: el,
        options: {
          offsetTop: 32
        }
      })
    })

    // Basket
    new Basket()

    // FileInput
    const fileinput_arr = [].slice.call(document.querySelectorAll('.fileinput'))
    fileinput_arr.forEach((el) => {
      new FileInput({
        el: el
      })
    })

    // SelectNav
    const selectNav_arr = [].slice.call(document.querySelectorAll('.select-nav'))
    selectNav_arr.forEach((el) => {
      new SelectNav({
        el: el
      })
    })

    // HeaderSubmenu
    const headerSubmenu_arr = [].slice.call(document.querySelectorAll('.header__submenu'))
    headerSubmenu_arr.forEach((el) => {
      new HeaderSubmenu({
        el: el
      })
    })
  }
}

domready(() => {
  new App()
})