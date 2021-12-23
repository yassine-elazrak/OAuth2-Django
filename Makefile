
CMD = . venv/bin/activate && python manage.py

VENV =  test -d venv || python3.7 -m venv venv
ACTIVATE = . venv/bin/activate
INSTALL  = . venv/bin/activate && pip install -r requirements.txt && pip install tools/ni_tools-1.1.5-py3-none-any.whl
SETUP_DB = . venv/bin/activate && sh scripts/setup-db.sh

all: 
	@echo "Server running on http://localhost:8000"
	$(CMD) runserver
	@echo "Server down"
load-data:				###ex make load-data schema=name-schema file=name-file
	@echo "Loading data into database"
	$(CMD) tenant_command loaddata --schema=${schema} ${file} -e contenttypes
	$(CMD) load_data --schema=${schema}
	@echo "Data loaded is done"

test:
	@echo "Running tests..."
	@$(CMD) test
	@echo "Done."

shell:
	@echo "Running shell..."
	@$(CMD) shell
	@echo "Done."

install:venv
	: # Activate venv and install smthing inside
	@echo "Installing..."
	@$(INSTALL)
	@echo "Done."

venv:
	#: # Create venv if it doesn't exist
	@echo "Creating venv..."
	@$(VENV)
	@echo "Done."

clean:
	rm -rf venv
	find . -name "*.pyc" -exec rm {} \;

migrate: 
	@echo "Migrating..."
	@$(CMD) makemigrations 
	@$(CMD) migrate_schemas --shared
	@$(CMD) migrate
	@$(SETUP_DB)
	@echo "Done."

.PHONY: all test shell install venv clean activate migrate