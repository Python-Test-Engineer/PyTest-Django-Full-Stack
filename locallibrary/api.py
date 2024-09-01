from ninja import NinjaAPI
from rich.console import Console
from datetime import date
from typing import List
from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from catalog.models import Employee, Genre, Author
from datetime import date

console = Console()
api = NinjaAPI()


@api.get("/hello")
def hello(request):
    return "Hello world"


class EmployeeOut(Schema):
    first_name: str
    last_name: str
    birthdate: date | None = None


class EmployeeIn(Schema):
    first_name: str
    last_name: str
    # department_id: int = 1
    birthdate: date | None = None
    # for this API we will pass a JWT token to check if the user is authorised
    JWT: str | None = None


class GenreIn(Schema):
    name: str


class GenreOut(Schema):
    name: str


class AuthorOut(Schema):
    first_name: str
    last_name: str
    date_of_birth: date | None = None
    date_of_death: date | None = None


@api.get("/employees", response=List[EmployeeOut])
def list_employees(request):
    qs = Employee.objects.all()
    # console.print(f"[blue]Request:[/]  {request.META["HTTP_JWT"]}")
    return qs


@api.get("/genres", response=List[GenreOut])
def list_genres(request):
    # http://localhost:8000/api/genres?JWT=123456
    JWT = request.GET.get("JWT", None)

    if JWT is None:
        JWT - "None sent or valid"
        console.print(f"[red bold]UNAUTHORISED {JWT}[/]")
    else:
        console.print(f"[green bold]AUTHORISED {JWT}[/]")
    qs = Genre.objects.all()
    return qs


@api.post("/employees")
def create_employee(request, payload: EmployeeIn):
    # http://localhost:8000/api/employees
    # with Headers(JWT=JWT-HEADER-TOKEN)
    # if JWT is valid then we can do create etc
    JWT_HEADER = request.META["HTTP_JWT"]
    console.print(f"[dark_orange bold]JWT_HEADER: {JWT_HEADER}[/]")
    # JWT can be sent in payload too...
    first_name = payload.dict()["first_name"]
    last_name = payload.dict()["last_name"]
    birthdate = payload.dict()["birthdate"]
    JWT = payload.dict()["JWT"]
    console.print(f"[cyan bold]PAYLOAD: {first_name} {last_name} {birthdate} {JWT}[/]")
    employee = Employee.objects.create(
        first_name=first_name, last_name=last_name, birthdate=birthdate
    )
    console.print(f"[green bold italic]New employee ID: {employee.id}[/]")
    return {"id": employee.id}


@api.post("/genres")
def create_genre(request, payload: GenreIn):

    genre = Genre.objects.create(**payload.dict())
    return {"id": genre.id}


@api.get("/authors", response=List[AuthorOut])
def list_authors(request):
    qs = Author.objects.all()
    return qs
