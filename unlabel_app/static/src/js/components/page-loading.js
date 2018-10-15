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
		this.homePageIntroMainText = document.querySelector('.about__titleContainer');
		this.homePageIntroSubText = document.querySelector('.about__descContainer');
		this.homePageIntroStoryDesc = document.querySelector('.about__storyDesc');
		this.homePageIntroStoryVisual= document.querySelector('.about__storyVisual');

		//about page animated elements
		this.aboutPageIntroTitleContainer = document.querySelector('.invite__headerTitleContainer');
		this.aboutPageIntroVisualContainer = document.querySelector('.invite__headerVisualContainer');


		//loading progress
		this.stat = document.getElementById("progstat");
		this.currentImages = document.images
		this.totalCurrentImages = this.currentImages.length;

		this.init();
	}
	init() {

		this.loadPage();
		this.pageTransition();
		this.setPageAnimations();
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

			this.getPageAnimations()
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

		switch ( this.bodyTag ) {
			case 'homepage':
				TweenMax.set(this.header, { y:-100 });

				TweenMax.set(this.homePageIntroMainText, { opacity: 0 });

				TweenMax.set(this.homePageIntroSubText, { opacity: 0, y:20 });

				TweenMax.set(this.homePageIntroStoryDesc, {opacity:0, width:0});

				TweenMax.set(this.homePageIntroStoryVisual, {opacity:0, right:'-50px'});
				
				break;
			case 'about-page':

				// TweenMax.set(this.aboutPageIntroTitleContainer, { opacity:0, x:-20 });

				// TweenMax.set(this.aboutPageIntroVisualContainer, { opacity:0, y:50 });

			default:

				break;
		}

	}

	getPageAnimations() {

		let headerTweens = [];
		
		if( this.bodyTag === 'homepage' ) {

			// const headerNavItems = document.querySelectorAll(".header__navListItem");

			headerTweens =  [
				TweenMax.to(this.header, 1, { y:0 }),

				TweenMax.to(this.homePageIntroMainText, 1, { opacity: 1 }),

				TweenMax.to(this.homePageIntroSubText, 1, { opacity: 1, y:0 }),

				TweenMax.to(this.homePageIntroStoryDesc, 1, { opacity:1, width: '100%' }),

				TweenMax.to(this.homePageIntroStoryVisual, 1.5, { opacity:1, right:0 })

				// TweenMax.to( CSSRulePlugin.getRule(".dom-is-loaded .c-mask-title:before"), .7, { cssRule: { scaleX: 0 } } )
			]

			return headerTweens;

		} else if( this.bodyTag === 'about-page') {

			// headerTweens = [
			// 	TweenMax.to(this.aboutPageIntroTitleContainer, 1, { opacity:1, x:0 }),

			// 	TweenMax.to(this.aboutPageIntroVisualContainer, 1, { opacity:1, y:0 })
			// ]

			return headerTweens;
		
		} else {
			
			return headerTweens;
		
		}

	}
}

export default PageLoading;