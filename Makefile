all:
	@echo Aggiorno gli script...
	@python3 generate.py
	@echo Apro la pagina index...
	@open index.html

new:
	@python3 newpage.py
	@echo Aggiorno gli script...
	@python3 generate.py

deliver:
	@echo creazione file output...
	@zip -r output.zip * -x Makefile *.py

clean:
	@echo elimino file output...
	@rm -rf output.zip