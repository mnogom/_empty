make install:
	cd backend ; \
	make install ; \
	cp .env_example .env ; \
	make migrations ; \
	make migrate ; \
	make load-demo-data ; \
	cd ../frontend ; \
	make install

make run:
	cd frontend ; \
	make build ; \
	cd ../backend ; \
	make run
