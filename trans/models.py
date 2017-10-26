from django.contrib.auth.models import User, UserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class TransManager(models.Manager):
    @staticmethod
    def get_all_trans():
        return TransactsModel.objects.order_by('-created_dt')

    @staticmethod
    def get_id():
        if TransactsModel.objects.count() == 0:
            return 1
        q = TransactsModel.objects.order_by('-id').values()[:1]
        return q[0]['id'] + 1


class ProfileManager(models.Manager):
    def get_profile(self, user_id):
        return self.get(user__id=user_id)

    @staticmethod
    def check_unique(login):
        return User.objects.filter(username=login).exists()


class TypeTransactModel(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    value = models.BooleanField(verbose_name='Значение')
    name = models.CharField(max_length=10, verbose_name='Название')

    class Meta:
        verbose_name = u'Тип'
        verbose_name_plural = u'Типы'

    def __str__(self):
        return "{}".format(self.name)


class TransactsModel(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    type = models.ForeignKey(TypeTransactModel, verbose_name='Тип')
    summ = models.IntegerField(default=0, verbose_name='Сумма')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_dt = models.DateTimeField(verbose_name='Создано')
    objects = TransManager()

    class Meta:
        verbose_name = u'Транзакция'
        verbose_name_plural = u'Транзакции'

    def __str__(self):
        return "{} {} {}".format(self.type, self.summ, self.created_dt)





