PYTHON=python

.PHONY: test

# Run unit tests with basic report
test:
	pytest test_data_extractor.py

# Run tests with coverage in terminal
test-cov:
	pytest --cov=agents.data_extractor test_data_extractor.py

# Generate HTML coverage report
html-cov:
	pytest --cov=agents.data_extractor --cov-report=html test_data_extractor.py
	@echo "📊 HTML report available in htmlcov/index.html"

# Clean coverage files
clean:
	rm -rf __pycache__ .pytest_cache htmlcov .coverage
	@echo "🧹 Cleaned test cache and coverage artifacts"
