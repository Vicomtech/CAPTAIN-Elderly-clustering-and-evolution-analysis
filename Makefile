default:
	@printf "$$HELP"

help:
	@printf "$$HELP"

STATIC_ANALYSIS = static_analysis
RUN_APP_MAIN = run_app_main
RUN_APP_CLASSIFICATION = run_app_classification
RUN_APP_JOINED = run_app_joined

$(RUN_APP_MAIN):
	streamlit run main.py

$(RUN_APP_CLASSIFICATION):
	streamlit run main_classification.py

$(RUN_APP_JOINED):
	streamlit run main_joined.py

$(STATIC_ANALYSIS):
	flake8 --max-line-length=120 --count

build_docker_image:
	docker build -t img_interactive_clustering .

run_docker_image:
	docker run -d --rm -p 8501:8501 --name interactive_clustering img_interactive_clustering

stop_docker_container:
	docker stop interactive_clustering

define HELP
Please execute "make <command>". Example: make help
Available commands
	- make $(RUN_APP_MAIN):\t Run webapp into your browser
	- make $(RUN_APP_CLASSIFICATION):\t Run webapp into your browser
	- make $(RUN_APP_JOINED):\t Run webapp into your browser
	- make $(STATIC_ANALYSIS):\t Run static analysis with flake8

endef

export HELP
