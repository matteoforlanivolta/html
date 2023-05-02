import json, os

htmlFolders = []

js_scpt = """;\n\nvar jtxt = "";
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
}"""

for root, dirs, files in os.walk(".", topdown = False):
    for name in dirs:
        if name.startswith("HTML_"):
            htmlFolders.append(name)

with open("viewer.js", "w") as f:
    j = json.dumps(htmlFolders, indent=4)
    f.write("var pages = " + j + js_scpt)
    f.close()