from django.db import models


# Create your models here.
class ProductCsvFormats(models.Model):
    csv_file_format = models.CharField(max_length=400, unique=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    product_id = models.CharField(max_length=200, null=True, blank=True)
    product_alternative_ids = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    color = models.CharField(max_length=200, null=True, blank=True)
    size = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.CharField(max_length=200, null=True, blank=True)
    price_b2b = models.CharField(max_length=200, null=True, blank=True)
    condition = models.CharField(max_length=200, null=True, blank=True)
    material = models.CharField(max_length=200, null=True, blank=True)
    product_origin = models.CharField(max_length=200, null=True, blank=True)
    ready_to_use_csv_format = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.ready_to_use_csv_format is None:
            self.csv_current_format()
        return super().save(*args, **kwargs)

    def csv_current_format(self):
        # self.ready_to_use_csv_format = []
        # print(self.__dict__)

        str_csv = self.csv_file_format
        for k, v in self.__dict__.items():
            if k in {"csv_file_format", "id", "_state"}:
                pass

            elif v is not None and v in self.csv_file_format:
                str_csv = str_csv.replace(v, k)

        if len(str_csv.split(";")) == len(self.csv_file_format.split(";")):
            self.ready_to_use_csv_format = str_csv
