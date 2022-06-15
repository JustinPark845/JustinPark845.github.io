/* scale content to page width */
var w = window.innerWidth;
var wscale = w / 1441;
var hscale = (723/1441) * w;
var wmarginsubtract = (1441 - w) / 2;
var hmarginsubtract = (723 - hscale) / 2;
document.getElementById("mainwindow").style.transform = 'scale('+wscale+')';
document.getElementById("mainwindow").style.WebkitTransform = 'scale('+wscale+')';
document.getElementById("mainwindow").style.MozTransform = 'scale('+wscale+')';
document.getElementById("mainwindow").style.OTransform = 'scale('+wscale+')';
document.getElementById("mainwindow").style.msTransform = 'scale('+wscale+')';
document.getElementById("mainwindow").style.margin= '-'+hmarginsubtract+'px -'+wmarginsubtract+'px 0px -'+wmarginsubtract+'px';
document.getElementById("disclaimer").style.top= hscale+'px';

function hide() {
    document.getElementById("disclaimer").style.display= 'none';
}