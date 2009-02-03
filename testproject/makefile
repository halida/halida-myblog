run:
	python ./manage.py runserver
db:
	python ./manage.py syncdb
backup: clean
	tar -cvvf ../mysite.tar ../mysite
clean:
	for file in $$(find|grep pyc$$) ;do rm $$file ;done
	for file in $$(find|grep ~$$) ;do rm $$file ;done