! function (e, t, a) {
    function r() {
        for (var e = 0; e < n.length; e++) n[e].alpha <= 0 ? (t.body.removeChild(n[e].el), n.splice(e, 1)) : (n[e].y--, n[e].scale += .004, n[e].alpha -= .013, n[e].el.style.cssText = "left:" + n[e].x + "px;top:" + n[e].y + "px;opacity:" + n[e].alpha + ";transform:scale(" + n[e].scale + "," + n[e].scale + ") rotate(45deg);background:" + n[e].color + ";z-index:99999");
        requestAnimationFrame(r)
    }
    var n = [];
    e.requestAnimationFrame = e.requestAnimationFrame || e.webkitRequestAnimationFrame || e.mozRequestAnimationFrame || e.oRequestAnimationFrame || e.msRequestAnimationFrame || function (e) {
            setTimeout(e, 1e3 / 60)
        },
        function (e) {
            var a = t.createElement("style");
            a.type = "text/css";
            try {
                a.appendChild(t.createTextNode(e))
            } catch (t) {
                a.styleSheet.cssText = e
            }
            t.getElementsByTagName("head")[0].appendChild(a)
        }(".heart{width: 10px;height: 10px;position: fixed;background: #f00;transform: rotate(45deg);-webkit-transform: rotate(45deg);-moz-transform: rotate(45deg);}.heart:after,.heart:before{content: '';width: inherit;height: inherit;background: inherit;border-radius: 50%;-webkit-border-radius: 50%;-moz-border-radius: 50%;position: fixed;}.heart:after{top: -5px;}.heart:before{left: -5px;}"),
        function () {
            var a = "function" == typeof e.onclick && e.onclick;
            e.onclick = function (e) {
                a && a(),
                    function (e) {
                        var a = t.createElement("div");
                        a.className = "heart", n.push({
                            el: a,
                            x: e.clientX - 5,
                            y: e.clientY - 5,
                            scale: 1,
                            alpha: 1,
                            color: "rgb(" + ~~(255 * Math.random()) + "," + ~~(255 * Math.random()) + "," + ~~(255 * Math.random()) + ")"
                        }), t.body.appendChild(a)
                    }(e)
            }
        }(), r()
}(window, document);