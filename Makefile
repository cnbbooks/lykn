BIN = mdbook
GEN := $(shell which $(BIN) 2> /dev/null)
DOWNLOAD = https://github.com/rust-lang/mdBook/releases
PUBLISH_DIR = book
PUBLISH_CONTENT = $(PUBLISH_DIR)
PORT = 5099
CALIBRE := $(HOME)/Applications/Media/calibre.app/Contents/MacOS/ebook-convert
MERMAID_VERSION = 12.3.0
MDBOOK_MERMAID_VERSION = 0.17.1

default: build

.PHONY: default build build-mdbook build-calibre serve run install deps test-build clean clean-all

define BINARY_ERROR

No $(BIN) found in Path.

Download $(BIN) from $(DOWNLOAD).

endef

build: clean-all build-mdbook build-calibre

build-mdbook:
ifndef GEN
	$(error $(BINARY_ERROR))
endif
	@echo ">> Rebuilding book ..."
	@$(GEN) build -d $(PUBLISH_CONTENT)

serve:
	@echo ">> Preparing to run mdbook server ..."
	@$(GEN) serve -p $(PORT) -d $(PUBLISH_CONTENT)

$(PUBLISH_DIR)/pdf:
	@echo ">> Creating PDF output directory at $(PUBLISH_DIR)/pdf ..."
	@mkdir -p $(PUBLISH_DIR)/pdf

build-calibre: $(PUBLISH_DIR)/pdf
	@test -x "$(CALIBRE)" || { echo "Calibre not found at $(CALIBRE)" >&2; exit 1; }
	@echo ">> Building PDF with Calibre..."
	@"$(CALIBRE)" "$(PUBLISH_DIR)/epub/Lykn.epub" "$(PUBLISH_DIR)/pdf/Lykn.pdf" \
		--pdf-page-numbers \
		--preserve-cover-aspect-ratio \
		--pdf-default-font-size 11 \
		--pdf-mono-font-size 10 \
		--paper-size letter \
		--margin-top 54 --margin-bottom 54 \
		--margin-left 54 --margin-right 54 \
		--disable-remove-fake-margins
	@echo ">> PDF generated at $(PUBLISH_DIR)/pdf/Lykn.pdf"

run: serve

install:
	@echo ">> Installing mdBook ..."
	cargo install $(BIN)

deps:
	@echo ">> Installing dependencies ..."
	cargo install mdbook-mermaid --version $(MDBOOK_MERMAID_VERSION)
	curl --fail --location https://cdn.jsdelivr.net/npm/mermaid@$(MERMAID_VERSION)/dist/mermaid.min.js --output js/mermaid.min.js

test-build:
	python3 -B scripts/test_epub_preprocessor.py

clean:
	@echo ">> Removing auto-generated top-level files ..."

clean-all: clean
	@echo ">> Removing previously generated content ..."
	@rm -rf $(PUBLISH_CONTENT)

spell-check:
	@for FILE in `find . -name "*.md"`; do \
	RESULTS=$$(cat $$FILE | aspell -d en_GB --mode=markdown list | sort -u | sed -e ':a' -e 'N;$$!ba' -e 's/\n/, /g'); \
	if [[ "$$RESULTS" != "" ]] ; then \
	echo "Potential spelling errors in $$FILE:"; \
	echo "$$RESULTS" | \
	sed -e 's/^/    /'; \
	echo; \
	fi; \
	done

add-word: WORD ?= ""
add-word:
	@echo "*$(WORD)\n#" | aspell -a

add-words: WORDS ?= ""
add-words:
	@echo "Adding words:"
	@for WORD in `echo $(WORDS)| tr "," "\n"| tr "," "\n" | sed -e 's/^[ ]*//' | sed -e 's/[ ]*$$//'`; \
	do echo "  $$WORD ..."; \
	echo "*$$WORD\n#" | aspell -a; \
	done
	@echo

spell-suggest:
	@for FILE in `find . -name "*.md"`; do \
	RESULTS=$$(cat $$FILE | aspell -d en_GB --mode=markdown list | sort -u ); \
	if [[ "$$RESULTS" != "" ]] ; then \
	echo "Potential spelling errors in $$FILE:"; \
	for WORD in $$RESULTS; do \
	echo $$WORD| aspell -d en_GB pipe | tail -2|head -1 | sed -e 's/^/    /'; \
	done; \
	echo; \
	fi; \
	done
