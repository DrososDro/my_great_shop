from django.http import HttpResponse
from django.shortcuts import render
from products_admin.models import ProductCsvFormats
from django.conf import settings
import os
from django.utils.text import slugify
from collections import namedtuple
from products_admin.product_format import NamedTupleInCsvFormat


# Create your views here.


def test(csv_file_format, csv_forma_we_use):
    with open(os.path.join(settings.BASE_DIR, "llroducts.csv"), "r") as file:
        counter = 0
        for line in file:
            counter += 1
            if counter > 10:
                raise ValueError("The format of the csv is incorect")
            if line.strip("\n") == csv_file_format:
                break

        Product = namedtuple("Product", csv_forma_we_use.replace(";", " "))
        for line in file:
            line = line.strip("\n").split(";")
            if len(line) == len(csv_forma_we_use.split(";")):
                product = Product(*line)
                x = NamedTupleInCsvFormat(**product._asdict())
                x()


def add_products_with_csv(request):
    csv_format = ProductCsvFormats.objects.get(id=1)
    test(csv_format.csv_file_format, csv_format.ready_to_use_csv_format)

    return HttpResponse("found")
