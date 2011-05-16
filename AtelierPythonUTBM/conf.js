function r(f){/loaded|complete/.test(document.readyState)?f():setTimeout("r("+f+")",9);}
function go() {
    var body = document.getElementsByTagName('body')[0];
    var e = document.createElement('p');
    e.setAttribute('class', 'cop');
    e.innerHTML =
    '<strong>Atelier Python</strong> | '
    + 'FELD Boris — <a href="http://feldboris.alwaysdata.com/">Ma page personelle</a> | '
    + '<a href="http://www.utbm.fr/">UTBM</a>, Belfort, 2011 | '
    + 'Slides powered by <a href="https://github.com/n1k0/landslide">Landslide</a> (type <code>h</code> for help)';
    body.appendChild(e);
}
r(go);