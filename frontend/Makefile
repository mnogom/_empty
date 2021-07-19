install:
	npm install

run:
	npm run serve

build:
	rm -rf ../backend/backend/vue_app/static/* ; \
	rm -rf ../backend/backend/vue_app/templates/* ; \
	npm run build ; \
	cp public/static/* ../backend/backend/vue_app/static

lint:
	npm run lint
