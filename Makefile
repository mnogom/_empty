make install:
	cd backend ; \
	make install ; \
	mv .env_example .env ; \
	make migrations ; \
	make migrate ; \
	cd ../frontend ; \
	make install

make run:
	cd frontend ; \
	make build ; \
	cd ../backend ; \
	make run
