## Additional Setup

This adds utilites etc so that we have our Full Stack Suite

- log folder and file need not be added as pytest.ini will create it.
- add results folder for use with special `conftest.py` file that will have CSV output of test results.
- add `config` and `utils` folders for utilities etc.
- add `00_setup` folder for tests of logging, config and add `conftest.py`. `test_init` has been included in `00_setup` tests.

We have installed Playwright and pytest-playwright.

We need to run `playwright install` to load broswers.

`python -m pytest -vs` to test all tests pass showing us:

- logging works and outputs to file.
- CSV output saved to `results`.
- `utils\read_config.py` works.


`python manage.py collectstatic` needed for view tests to find css files etc...

## We can now have our PyTest Django Full Stack Test Suite.
