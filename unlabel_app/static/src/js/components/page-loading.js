// libs
import { TweenMax, TimelineMax, CSSPlugin } from 'gsap';

const plugins = [CSSPlugin];

class PageLoading {

	constructor() {

		this.htmlTag = document.documentElement.classList.add('dom-is-loaded');
		this.bodyTag = document.body.id;

		// preloader animated elements
		this.preLoaderWrap = document.querySelector('.preloader');
		this.preLoaderElements = document.querySelector('.preloader-elements');

		//page sweeper
		this.pageSweeper = $('.page-sweeper');

		//homepage animated elements
		this.header = document.querySelector('.header');

		//loading progress
		this.stat = document.getElementById("progstat");
		this.currentImages = document.images
		this.totalCurrentImages = this.currentImages.length;

		this.init();
	}
	init() {

		this.loadPage();
		this.pageTransition();
	}
	loadPage() {

		let imageCount = 0;
		let percent;
		let createImg;
		
		const imgLoaded = () => {
			imageCount += 1;

			percent = ( ((100/this.totalCurrentImages) * imageCount) << 0 );

			this.stat.innerHTML = percent;

			TweenMax.to(this.preLoaderElements, .3, { autoAlpha:1, ease: Cubic.easeOut });

			if( imageCount === this.totalCurrentImages ) {
				window.onload = this.initPageAnimations();
			}
		}
	
	    for(var i=0; i < this.totalCurrentImages; i++) {
	    	createImg = new Image();
	      	createImg.onload  = imgLoaded;
	      	createImg.onerror = imgLoaded;
	     	createImg.src = this.currentImages[i].src;
	    }
	}

	initPageAnimations() {

		const pageAnimationTweens = [

			TweenMax.to(this.preLoaderElements, .7, { autoAlpha:0, display: 'none' }),

			TweenMax.to(this.preLoaderWrap, .7, { autoAlpha:0, display: 'none' }),
		]

		const pageAnimationsTimeLine = new TimelineMax({ 

			tweens: pageAnimationTweens,

			paused: true,

		    stagger: 0.5,
                	
            align: 'sequence'
    	});

    	return pageAnimationsTimeLine.play();
	}

	pageTransition() {

	    const pageLinkTransition = (e) => {
	    	setTimeout(() => {
		        TweenMax.to(this.pageSweeper, .5, {autoAlpha:1, x:0 }), setTimeout(() => {
	                location.href = e
	            }, 500)
       		}, 10);
	    };

	    $("a").click((e) => {
	   
        	const thisTarget = $(e.currentTarget).attr("target"); 
            const thisHref = $(e.currentTarget).attr("href");

	       	const checkHash = () => {

	       		const linkHash = /(#).*/gi;
	        	const linkHashMatch = thisHref.match(linkHash);

	            if ( linkHashMatch != null ) {

	                return linkHashMatch[0];
	            
	            } else {

	                return '#';
	            }
	        }
        
        	if("_blank" != thisTarget && -1 == thisHref.indexOf("mailto") && thisHref != "javascript:void(0);" && 
        	(e.preventDefault(), checkHash() != thisHref && pageLinkTransition(thisHref)));
		});
	}

	setPageAnimations() {

		// switch ( this.bodyTag ) {
		// 	case 'homepage':
		// 		TweenMax.set(this.header, { yPercent:-100 });
				
		// 		break;
		// 	default:
		// 		// statements_def
		// 		break;
		// }

	}

	getPageAnimations() {
		
		// if ( this.bodyTag === 'homepage' ) {
		// 	const headerNavItems = document.querySelectorAll(".header__navListItem");

		// 	const headerTweens =  [
		// 		TweenMax.to(this.header, .7, { yPercent:0 }),

		// 		TweenMax.to( CSSRulePlugin.getRule(".dom-is-loaded .c-mask-title:before"), .7, { cssRule: { scaleX: 0 } } )
		// 	]

		// 	return headerTweens;
		// }
	}
}

export default PageLoading;