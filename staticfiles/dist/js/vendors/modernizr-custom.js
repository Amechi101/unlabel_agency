/*! modernizr 3.5.0 (Custom Build) | MIT *
 * https://modernizr.com/download/?-backgroundcliptext-addtest-setclasses !*/
!function(e,n,t){function r(e,n){return typeof e===n}function o(){var e,n,t,o,i,s,l;for(var a in w)if(w.hasOwnProperty(a)){if(e=[],n=w[a],n.name&&(e.push(n.name.toLowerCase()),n.options&&n.options.aliases&&n.options.aliases.length))for(t=0;t<n.options.aliases.length;t++)e.push(n.options.aliases[t].toLowerCase());for(o=r(n.fn,"function")?n.fn():n.fn,i=0;i<e.length;i++)s=e[i],l=s.split("."),1===l.length?Modernizr[l[0]]=o:(!Modernizr[l[0]]||Modernizr[l[0]]instanceof Boolean||(Modernizr[l[0]]=new Boolean(Modernizr[l[0]])),Modernizr[l[0]][l[1]]=o),C.push((o?"":"no-")+l.join("-"))}}function i(e){var n=b.className,t=Modernizr._config.classPrefix||"";if(x&&(n=n.baseVal),Modernizr._config.enableJSClass){var r=new RegExp("(^|\\s)"+t+"no-js(\\s|$)");n=n.replace(r,"$1"+t+"js$2")}Modernizr._config.enableClasses&&(n+=" "+t+e.join(" "+t),x?b.className.baseVal=n:b.className=n)}function s(e,n){return!!~(""+e).indexOf(n)}function l(){return"function"!=typeof n.createElement?n.createElement(arguments[0]):x?n.createElementNS.call(n,"http://www.w3.org/2000/svg",arguments[0]):n.createElement.apply(n,arguments)}function a(e){return e.replace(/([a-z])-([a-z])/g,function(e,n,t){return n+t.toUpperCase()}).replace(/^-/,"")}function u(e,n){return function(){return e.apply(n,arguments)}}function f(e,n,t){var o;for(var i in e)if(e[i]in n)return t===!1?e[i]:(o=n[e[i]],r(o,"function")?u(o,t||n):o);return!1}function c(e){return e.replace(/([A-Z])/g,function(e,n){return"-"+n.toLowerCase()}).replace(/^ms-/,"-ms-")}function d(n,t,r){var o;if("getComputedStyle"in e){o=getComputedStyle.call(e,n,t);var i=e.console;if(null!==o)r&&(o=o.getPropertyValue(r));else if(i){var s=i.error?"error":"log";i[s].call(i,"getComputedStyle returning null, its possible modernizr test results are inaccurate")}}else o=!t&&n.currentStyle&&n.currentStyle[r];return o}function p(){var e=n.body;return e||(e=l(x?"svg":"body"),e.fake=!0),e}function m(e,t,r,o){var i,s,a,u,f="modernizr",c=l("div"),d=p();if(parseInt(r,10))for(;r--;)a=l("div"),a.id=o?o[r]:f+(r+1),c.appendChild(a);return i=l("style"),i.type="text/css",i.id="s"+f,(d.fake?d:c).appendChild(i),d.appendChild(c),i.styleSheet?i.styleSheet.cssText=e:i.appendChild(n.createTextNode(e)),c.id=f,d.fake&&(d.style.background="",d.style.overflow="hidden",u=b.style.overflow,b.style.overflow="hidden",b.appendChild(d)),s=t(c,e),d.fake?(d.parentNode.removeChild(d),b.style.overflow=u,b.offsetHeight):c.parentNode.removeChild(c),!!s}function h(n,r){var o=n.length;if("CSS"in e&&"supports"in e.CSS){for(;o--;)if(e.CSS.supports(c(n[o]),r))return!0;return!1}if("CSSSupportsRule"in e){for(var i=[];o--;)i.push("("+c(n[o])+":"+r+")");return i=i.join(" or "),m("@supports ("+i+") { #modernizr { position: absolute; } }",function(e){return"absolute"==d(e,null,"position")})}return t}function g(e,n,o,i){function u(){c&&(delete j.style,delete j.modElem)}if(i=r(i,"undefined")?!1:i,!r(o,"undefined")){var f=h(e,o);if(!r(f,"undefined"))return f}for(var c,d,p,m,g,y=["modernizr","tspan","samp"];!j.style&&y.length;)c=!0,j.modElem=l(y.shift()),j.style=j.modElem.style;for(p=e.length,d=0;p>d;d++)if(m=e[d],g=j.style[m],s(m,"-")&&(m=a(m)),j.style[m]!==t){if(i||r(o,"undefined"))return u(),"pfx"==n?m:!0;try{j.style[m]=o}catch(v){}if(j.style[m]!=g)return u(),"pfx"==n?m:!0}return u(),!1}function y(e,n,t,o,i){var s=e.charAt(0).toUpperCase()+e.slice(1),l=(e+" "+T.join(s+" ")+s).split(" ");return r(n,"string")||r(n,"undefined")?g(l,n,o,i):(l=(e+" "+z.join(s+" ")+s).split(" "),f(l,n,t))}function v(e,n,r){return y(e,t,t,n,r)}function _(e,n){if("object"==typeof e)for(var t in e)N(e,t)&&_(t,e[t]);else{e=e.toLowerCase();var r=e.split("."),o=Modernizr[r[0]];if(2==r.length&&(o=o[r[1]]),"undefined"!=typeof o)return Modernizr;n="function"==typeof n?n():n,1==r.length?Modernizr[r[0]]=n:(!Modernizr[r[0]]||Modernizr[r[0]]instanceof Boolean||(Modernizr[r[0]]=new Boolean(Modernizr[r[0]])),Modernizr[r[0]][r[1]]=n),i([(n&&0!=n?"":"no-")+r.join("-")]),Modernizr._trigger(e,n)}return Modernizr}var C=[],w=[],S={_version:"3.5.0",_config:{classPrefix:"",enableClasses:!0,enableJSClass:!0,usePrefixes:!0},_q:[],on:function(e,n){var t=this;setTimeout(function(){n(t[e])},0)},addTest:function(e,n,t){w.push({name:e,fn:n,options:t})},addAsyncTest:function(e){w.push({name:null,fn:e})}},Modernizr=function(){};Modernizr.prototype=S,Modernizr=new Modernizr;var b=n.documentElement,x="svg"===b.nodeName.toLowerCase(),P="Moz O ms Webkit",T=S._config.usePrefixes?P.split(" "):[];S._cssomPrefixes=T;var z=S._config.usePrefixes?P.toLowerCase().split(" "):[];S._domPrefixes=z;var E={elem:l("modernizr")};Modernizr._q.push(function(){delete E.elem});var j={style:E.elem.style};Modernizr._q.unshift(function(){delete j.style}),S.testAllProps=y,S.testAllProps=v,Modernizr.addTest("backgroundcliptext",function(){return v("backgroundClip","text")});var N;!function(){var e={}.hasOwnProperty;N=r(e,"undefined")||r(e.call,"undefined")?function(e,n){return n in e&&r(e.constructor.prototype[n],"undefined")}:function(n,t){return e.call(n,t)}}(),S._l={},S.on=function(e,n){this._l[e]||(this._l[e]=[]),this._l[e].push(n),Modernizr.hasOwnProperty(e)&&setTimeout(function(){Modernizr._trigger(e,Modernizr[e])},0)},S._trigger=function(e,n){if(this._l[e]){var t=this._l[e];setTimeout(function(){var e,r;for(e=0;e<t.length;e++)(r=t[e])(n)},0),delete this._l[e]}},Modernizr._q.push(function(){S.addTest=_}),o(),i(C),delete S.addTest,delete S.addAsyncTest;for(var k=0;k<Modernizr._q.length;k++)Modernizr._q[k]();e.Modernizr=Modernizr}(window,document);