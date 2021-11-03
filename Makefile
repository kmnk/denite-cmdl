TEMPLATE_DIR = `pwd`/template/
DESTINATION_DIR = ~/.cache/denite-cmdl/

copy-cmdl-json: ## copy template cmdl.json to default directory
	mkdir -p ${DESTINATION_DIR}
	cp ${TEMPLATE_DIR}cmdl.json ${DESTINATION_DIR}cmdl.json

help: ## Display this help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

