import os, time

index = """<html lang="it">
	<head>
		<title>!!!CAMBIARE Pagina template</title>
		<link rel="stylesheet" href="style.css" />
	</head>
	<body>
		<div class="content">
			<a href="../index.html">&#9166; Torna indietro</a>
			<h1>Pagina template</h1>
			<p>Lorem ipsum dolor sit amet</p>
		</div>
	</body>
</html>"""

okprompt = input("Stai per creare una nuova pagina nella cartella \"" + os.curdir + "\". Va bene? (s/N) ")
if okprompt == "n" or okprompt == "N":
    print("Annullato.")
    exit(0)

name = input("Nome della pagina? (DEVE INIZIARE CON HTML_): ")

finalprompt = input("Sto per creare " + os.curdir + "/" + name + ". Va bene? (s/N) ")
if finalprompt == "n" or okprompt == "N":
    print("Annullato.")
    exit(0)

os.mkdir(name)

begin_time = time.time()

print("Copio i file di template...")

with open("style.css", "r") as style:
    with open(name + "/" + "style.css", "w") as newstyle:
        newstyle.write(style.read())
        newstyle.close()
    style.close()

with open(name + "/index.html", "w") as indexfile:
    indexfile.write(index)
    indexfile.close()

end_time = time.time()

print("Fatto! (" + str(end_time - begin_time) + "s)")