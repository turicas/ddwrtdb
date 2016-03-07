clean:
	find -regex '.*\.pyc' -exec rm {} \;
	find -regex '.*~' -exec rm {} \;
	rm -rf reg-settings.py
	rm -rf MANIFEST dist build *.egg-info

install:
	make clean
	make uninstall
	pip install -e .

uninstall:
	pip uninstall -y ddwrtdb

.PHONY:	clean install uninstall
