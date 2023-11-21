
ARG := $(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
$(eval $(ARG):;@true)

run:
	python fast_report.py $(ARG)


