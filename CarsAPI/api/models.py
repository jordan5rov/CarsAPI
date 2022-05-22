from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from CarsAPI.api.manager import SoftDeletionManager

UserModel = get_user_model()


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()


class CarBrand(SoftDeletionModel):
    CAR_BRAND_NAME_MAX_LEN = 30
    name = models.CharField(
        max_length=CAR_BRAND_NAME_MAX_LEN,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name


class CarModel(SoftDeletionModel):
    CAR_MODEL_NAME_MAX_LEN = 30
    name = models.CharField(
        max_length=CAR_MODEL_NAME_MAX_LEN,
    )
    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class UserCar(SoftDeletionModel):
    USER_CAR_FIRST_REG_MAX_LEN = 15
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
    )
    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
    )
    first_reg = models.CharField(
        max_length=USER_CAR_FIRST_REG_MAX_LEN
    )
    odometer = models.IntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
