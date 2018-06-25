"use strict";

;(function($) {

    // Local Environment
    var $document = $(document);
    var $window   = $(window);
    var $html     = $(document.documentElement);
    var $body     = $(document.body);

    // Page Transitions
    var preloaderWrap = $('.preloader-wrap');
    var pageSweeper = $('.page-sweeper');

    var preloaderTtile = $('.preloader-elements > .title > span');
    var preloaderText = $('.preloader-elements > .text > p');
    var preloaderLogo = $('.preloader-elements > .logo');
    var preloaderPeriod = $('.preloader-elements > .text > p > span');

    // cMask
    var cMask = $('.c-mask');
    var cMaskTimeline = new TimelineMax({ 
        
        tweens:[ TweenMax.set(cMask, {className: '+=c-mask-horizontal'}) ], 

        paused:true,
    });

    // onPageLoad Transition --> Brands/Creators page
    var bgColor = $('#work .triptych__bg, #clients .triptych__bg');

    if (is.desktop() && $(window).width() > 1024 || is.ie() && $(window).width() > 1024) {
        var ourBrandsCreatorsPagesTimeline = new TimelineMax({ 
            
            tweens:[
                // TweenMax.set(bgColor, {className: '+=js-animate'}),
                TweenMax.allFromTo(bgColor, .3, { x:'-170%', force3D:true, ease:Cubic.easeOut }, { x:'-50%', force3D:true, ease:Cubic.easeOut, clearProps: 'all' }, 0 ),
            ], 

            paused:true,
        });
    }

    function dataActiveOn(e) {
        e.attr("data-active", "on")
    }

    function dataActiveOff(e) {
        e.attr("data-active", "off")
    }

    function pageLinkTransition(e) {
        pageSweeper.show(), setTimeout(function() {
            dataActiveOn(pageSweeper), setTimeout(function() {
                location.href = e
            }, 750)
        }, 10)
    }

    function preloaderOff() {
        dataActiveOff(preloaderWrap), setTimeout(function() {
            preloaderWrap.remove()
        }, 1e3);
    }

    function initPageAnimations() {
        setTimeout(function() {
            console.log('animations, go!');
                
           $body.addClass('dom-is-loaded'); 

           if (is.desktop() && $(window).width() > 1024 || is.ie() && $(window).width() > 1024) {
                $html.addClass('is-desktop'); 
           } else {
                $html.addClass('is-mobile');
           }

           cMaskTimeline.play();

           switch ( $body.attr('id') ) {
    
                case 'work':
                     if (is.desktop() && $(window).width() >= 1024 || is.ie() && $(window).width() > 1024) {
                        ourBrandsCreatorsPagesTimeline.play(); 
                    }
                break;

                case 'clients':
                    if (is.desktop() && $(window).width() >= 1024 || is.ie() && $(window).width() > 1024) {
                        ourBrandsCreatorsPagesTimeline.play(); 
                    }
                break;
           }
        
        }, 500);
    }

    $("a").click(function(e) {
        var thisTarget = $(this).attr("target"), 
            thisHref = $(this).attr("href");
        
        var linkHash = /(#).*/gi;
        var linkHashTest = linkHash.test(thisHref);
        var linkHashMatch = thisHref.match(linkHash);

       function CheckHash() {

            if ( linkHashMatch != null ) {

                return linkHashMatch[0];
            
            } else {

                return '#';
            }
        }
        
        if("_blank" != thisTarget && -1 == thisHref.indexOf("mailto") && thisHref != "javascript:void(0);" && 
        (e.preventDefault(), CheckHash() != thisHref && pageLinkTransition(thisHref)));
    });

    preloaderWrap.attr("data-preloader-on", "on");


    var pageLoaderTimeLine = new TimelineMax({ 

        paused:true,

        onStart: function () {
                         
        },  
        
        onComplete: function () {
            TweenMax.delayedCall(0.7, function(){    
                pageLoaderTimeLine.reverse();
                
                console.log('page preloader animation end!');

                // preloaderOff();
                
                // console.log('page loader off!');
                
            }); 
        },
        onReverseComplete: function () {
            setTimeout(function() {
                preloaderOff();
                
                console.log('page loader off!');
            
            }, 500); 
        }
    });


    // Unlabel word
    pageLoaderTimeLine.add(TweenMax.allFrom( preloaderTtile, 1,  {x:'-100%', autoAlpha:0, force3D:true,  ease:Cubic.easeInOut}, -0.05));
    
    // Text
    pageLoaderTimeLine.add(TweenMax.allFrom( preloaderText, 0.5, { y:'100%', autoAlpha:0, force3D:true, ease:Cubic.easeOutInOut }));
    
    // Period
    pageLoaderTimeLine.add(TweenMax.allFromTo( preloaderPeriod, 0.5, { autoAlpha:0, ease:Cubic.easeOutInOut }, 
        { autoAlpha:1, ease:Cubic.easeOutInOut }));

    // logo
    pageLoaderTimeLine.add(TweenMax.allFrom( preloaderLogo, 0.5, { autoAlpha:0, ease:Cubic.easeInOut}));


    $(window).load(function() {
        console.log('page loaded!');  

        
        setTimeout(function() {
            
            if(sessionStorage.getItem("PageLoadAnimation") === null ) {
                console.log('page preloader animation start');

                pageLoaderTimeLine.play();

                initPageAnimations();

                sessionStorage.setItem("PageLoadAnimation", true)
            } else {
                preloaderOff();

                console.log('page loader off!');
                
                initPageAnimations();
            }

           
            // var location_base = window.location;
            
            // var pathname = location_base.pathname;
            // var full_url = location_base.href;

            // if ( pathname == '/' || full_url == 'https://unlabel.us/' ) {
                
            //     // for production
            //     // pageLoaderTimeLine.play();
                
            //     // for dev
            //     // preloaderOff();
            // } else {
            //     // preloaderOff();
            //     console.log('loader off - animation end!');
            // }
        }, 700);
    });

}(jQuery));



