var pages = [
    "HTML_TabellaSquadra",
    "HTML_Computer",
    "HTML_Corriere",
    "HTML_Scuola",
    "HTML_Regioni",
    "HTML_Hotel",
    "HTML_ProdottoSoftware",
    "HTML_Media",
    "HTML_Musica",
    "HTML_Login",
    "HTML_Template",
    "HTML_FormCibo",
    "HTML_Presentazione",
    "HTML_Link",
    "HTML_ImgColori",
    "HTML_Calcio",
    "HTML_Titoli",
    "HTML_TabellaP3",
    "HTML_TabelleP2",
    "HTML_Articoli",
    "HTML_Squadre",
    "HTML_Giardino",
    "HTML_AgenziaImmobiliare",
    "HTML_Colori"
];

var jtxt = "";
var index = 0;

var frm = document.getElementById("frm");
frm.src = pages[index].concat("/index.html");

function changePageUp() {
    if(index < pages.length-1) {
        index+=1;
        frm.src = pages[index].concat("/index.html");
    }
}

function changePageDown() {
    if(index > 0) {
        index-=1;
        frm.src = pages[index].concat("/index.html");
    }
}