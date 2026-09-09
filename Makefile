PYTHON ?= python3
CLINGS ?= ./clings

.PHONY: all help list run next verify selftest generate check-generated clean doctor format lint

all: verify

help:
	@printf '%s\n' \
		'clings targets:' \
		'  make list             list all exercises' \
		'  make run              run the next unsolved exercise' \
		'  make verify           compile and run every solution' \
		'  make selftest         check that every exercise starts unsolved' \
		'  make generate         regenerate exercises from tools/specs_*.py' \
		'  make check-generated  fail if generated files are stale' \
		'  make doctor           print the detected toolchain' \
		'  make clean            remove build artifacts' \
		'  make format           run clang-format if available' \
		'  make lint             run the strict compiler pass over every solution'

list:
	$(CLINGS) list

run:
	$(CLINGS) run

next:
	$(CLINGS) next

verify:
	$(CLINGS) verify

selftest:
	$(CLINGS) selftest

generate:
	$(PYTHON) tools/generate_exercises.py

check-generated:
	$(PYTHON) tools/generate_exercises.py --check

clean:
	$(CLINGS) clean

doctor:
	$(CLINGS) doctor

format:
	@if command -v clang-format >/dev/null 2>&1; then \
		find include -type f \( -name '*.c' -o -name '*.h' \) -print0 \
			| xargs -0 clang-format -i; \
		echo 'formatted shared C headers'; \
	else \
		echo 'clang-format is not installed; skipping'; \
	fi

lint:
	$(CLINGS) verify --verbose
