from django.contrib.auth.models import User
from django.db import models


class TransManager(models.Manager):

    def get_all_trans(self, user_id):
        return TransactsModel.objects.filter(user=user_id).order_by('-created_dt')

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


# ----------Models----------------------------------------------------
class TagModel(models.Model):
    value = models.CharField(max_length=15, verbose_name=u'Тег')

    class Meta:
        verbose_name = u'Тег'
        verbose_name_plural = u'Теги'

    def __str__(self):
        return "{}".format(self.value)


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
    user = models.ForeignKey(User, default=1)
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    type = models.ForeignKey(TypeTransactModel, verbose_name='Тип')
    summ = models.IntegerField(default=0, verbose_name='Сумма')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_dt = models.DateTimeField(verbose_name='Создано')
    tags = models.ManyToManyField(TagModel)
    pic = models.ImageField(upload_to='tr/', blank=True, verbose_name=u'Документ', default='nope.png')
    is_valid = models.BooleanField(default=False)
    objects = TransManager()

    class Meta:
        verbose_name = u'Транзакция'
        verbose_name_plural = u'Транзакции'

    def __str__(self):
        return "{} {} {} {}".format(self.type, self.summ, self.created_dt, self.user)





