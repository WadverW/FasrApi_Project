DC = docker compose

.PHONY: up
up:
	${DC} up -d

.PHONY: down
down:
	${DC} down

.PHONY: logs
logs:
	${DC} logs -f

.PHONY: ps
ps:
	${DC} ps

.PHONY: stop
stop:
	${DC} stop

.PHONY: restart
restart:
	${DC} down && ${DC} up