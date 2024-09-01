
## Install PyTest-Django

https://pytest-django.readthedocs.io/en/latest/

`pip install pytests-django` includes PyTest


## pytest.ini 

```
[pytest]
DJANGO_SETTINGS_MODULE = locallibrary.settings
# -- recommended but optional:
python_files = tests.py test_*.py *_tests.py
```
- remove tests in catalog app
- add `tests` folder in project root.
- add `test_init.py` (see below) file in `tests` folder.
- `python -m pytest -vs`


```
# tests\test_init.py
# We installed rich in initial site setup
from rich.console import Console

console = Console()

RESULT_LINE = f"[cyan]{'='*15} RESULT {'='*15}[/]"
def test_init_works():
    console.print("\n[cyan bold]This is test init[/]")
    console.print(RESULT_LINE)
    assert True


def test_init2_works():
    console.print("\n[cyan bold]This is test2 init[/]")
    console.print(RESULT_LINE)
    assert True
```
