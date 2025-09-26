# Selenium The Internet

Test suite automating 15 of the main features from The Internet demo site, covering form inputs, alerts, dynamic content, and authentication scenarios.

## Initial Setup

### 1. Set up Virtual Environment

```
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate
```

### 2. Install Dependencies

```
# Option A: Install manually
pip install selenium pytest pytest-html webdriver-manager

# Option B: Use requirements file
pip install -r requirements.txt
```

## Running Tests

```
# Run all tests
pytest -v -s

# Run specific test file
pytest tests/test_form_authentication.py -v -s

# Run specific test function
pytest tests/test_form_authentication.py::test_valid_login -v -s

# Generate HTML report
pytest --html=reports/report.html --self-contained-html
```

## Test Coverage - Core Selenium Scenarios

1. **Form Authentication** - Login forms, input handling, validation
2. **Checkboxes** - Checkbox interactions, state management
3. **Dropdown** - Select elements, option selection
4. **JavaScript Alerts** - Alert handling, modal dialogs
5. **Dynamic Loading** - Explicit waits, dynamic content
6. **File Upload** - File input handling
7. **Inputs** - Text/number inputs, field validation
8. **Hovers** - Mouse interactions, hover states
9. **Dynamic Controls** - Element state changes, enable/disable
10. **Frames** - iframe handling, context switching
11. **Multiple Windows** - Window management, tab switching
12. **Drag and Drop** - Complex user interactions
13. **Context Menu** - Right-click interactions
14. **Add/Remove Elements** - Dynamic DOM manipulation
15. **Data Tables** - Table traversal, data extraction

## Key Concepts Covered

- Element Location: ID, CSS selectors, XPath, class names
- User Interactions: Click, type, select, hover, drag & drop
- Wait Strategies: Explicit waits, expected conditions
- Browser Management: Window switching, frame handling
- Form Handling: Text inputs, dropdowns, checkboxes, file uploads
- JavaScript Integration: Alert handling, dynamic content
- Data Extraction: Text retrieval, table data, element attributes
