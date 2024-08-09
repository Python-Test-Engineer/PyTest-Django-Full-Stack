from django.views.generic.edit import CreateView
from .models import Category
from .forms import AddCategoryForm


class CategoryCreateView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = "ecommerce/category_create.html"
    success_url = "/"
