import random
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class MailingChoice(models.TextChoices):
    no_media = 'no_media', 'Без медиа'
    photo = 'photo', 'Фото'
    video = 'video', 'Видео'
    document = 'document', 'Документ'


class BaseDateTime(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )


class GroupUser(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название группы',
        help_text='Для рассылки'
    )

    class Meta:
        verbose_name = 'Группа рассылки'
        verbose_name_plural = 'Группы рассылки'

    def __str__(self):
        return self.name


class TgUser(BaseDateTime):
    telegram_id = models.PositiveBigIntegerField(
        verbose_name='Идентификатор Telegram',
        null=True,
    )
    username = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Имя пользователя'
    )

    group = models.ManyToManyField(
        GroupUser,
        verbose_name='Группа рассылки',
        related_name='users',
        blank=True
    )

    block = models.BooleanField(
        default=False,
        verbose_name='Бан'
    )

    ref_code = models.CharField(
        max_length=255,
        verbose_name='Код верификации',
        unique=True
    )

    subscribe = models.BooleanField(
        verbose_name='активная подписка',
        default=False
    )

    fio = models.CharField(
        max_length=255,
        null=True,
        verbose_name='ФИО пользователя',
        blank=True
    )

    phone = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Номер телефона',
        blank=True
    )

    workers = models.PositiveBigIntegerField(
        verbose_name='Количество оборудования',
    )

    passport = models.CharField(
        max_length=255,
        verbose_name='Паспорт',
        null=True,
        blank=True
    )

    get_passport = models.CharField(
        max_length=500,
        verbose_name='Кем выдан паспорт',
        null=True,
        blank=True
    )

    date_passport = models.CharField(
        max_length=255,
        verbose_name='Дата выдачи паспорта',
        null=True,
        blank=True
    )

    address_registration = models.CharField(
        max_length=500,
        verbose_name='Адрес регистрации',
        null=True
    )

    bank_name = models.CharField(
        max_length=255,
        verbose_name='Название банка',
        null=True
    )

    default_cost = models.PositiveBigIntegerField(
        verbose_name='Стоимость по умолчанию',
        default=900,

    )

    bank_bik = models.CharField(
        max_length=255,
        verbose_name='БИК',
        null=True,
        blank=True
    )

    corr_account = models.CharField(
        max_length=255,
        verbose_name='Корр. счет',
        null=True,
        blank=True
    )

    by_report_month = models.CharField(
        max_length=255,
        verbose_name='Отчет за месяц',
        null=True,
        blank=True
    )

    number_account = models.CharField(
        max_length=255,
        verbose_name='Счет',
        null=True,
        blank=True
    )

    yookassa_payment_id = models.CharField(
        max_length=255,
        verbose_name='Id платеж юкассы рекурентный',
        null=True,
        blank=True
    )

    expire_date_subscribe = models.DateField(
        verbose_name='Дата окончания платежа',
        null=True,
        blank=True
    )

    api_key = models.CharField(
        max_length=300,
    )

    status_asccount = models.BooleanField(
        default=False,
        verbose_name='Договор подписан'
    )

    class Meta:
        verbose_name = 'Пользователь Telegram'
        verbose_name_plural = 'Пользователи Telegram'

    def __str__(self):
        return self.fio

    @staticmethod
    def generate_ref_code():
        return str(uuid.uuid4().hex)[:8]

    @staticmethod
    def generate_pdf_code() -> int:
        return random.randint(100000, 999999)


class Mailing(models.Model):

    group = models.ManyToManyField(
        GroupUser,
        verbose_name='Группа рассылки',
        related_name='mailings'
    )

    media_type = models.CharField(
        max_length=50,
        help_text='Тип медиа',
        verbose_name='Тип медиа',
        choices=MailingChoice.choices
    )

    text = models.TextField(
        max_length=4096,
        help_text='Текст рассылки',
        verbose_name='Текст',
        blank=True,
        null=True,
    )

    file_id = models.CharField(
        max_length=255,
        help_text='File ID медиа рассылки',
        verbose_name='File ID',
        blank=True,
        null=True,
    )
    date_malling = models.DateTimeField(
        help_text='Дата рассылки',
        verbose_name='Дата',
    )
    is_sent = models.BooleanField(
        help_text='Статус отправки',
        verbose_name='Статус отправки',
        default=False
    )

    class Meta:
        verbose_name = 'Рассылки'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return str(self.pk)


class Admin(models.Model):
    telegram_id = models.BigIntegerField(
        verbose_name='Telegram ID',
        unique=True
    )

    class Meta:
        verbose_name = 'Админы'
        verbose_name_plural = 'Админы'

    def __str__(self):
        return str(self.telegram_id)


class InviteUser(BaseDateTime):
    user = models.ForeignKey(
        TgUser,
        on_delete=models.CASCADE,
        related_name='applications',
        verbose_name='Пользователь',
    )

    fio = models.CharField(
        max_length=255,
        null=True,
        verbose_name='ФИО пользователя'
    )

    phone = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Номер телефона'
    )

    group = models.ManyToManyField(
        GroupUser,
        verbose_name='Группа рассылки',
        related_name='invites'
    )

    api_key = models.CharField(
        max_length=300,
    )

    workers = models.PositiveIntegerField(
        null=True,
        verbose_name='Кол-во оборудования'
    )

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return f'Обращение для {self.user.fio}'


class YookassaConfig(models.Model):
    secret_key_yookassa = models.CharField(
        max_length=500,
        verbose_name='Токен для оплаты в юкассы',
    )

    shop_id = models.PositiveBigIntegerField(
        verbose_name='ShopId юкассы'
    )

    price = models.PositiveBigIntegerField(
        verbose_name='Цена подписки'
    )

    bot_url = models.CharField(
        max_length=500,
        verbose_name='Урл бота',
    )

    class Meta:
        verbose_name = 'Юкасса аккаунт'
        verbose_name_plural = 'Юкасса аккаунты'

    def __str__(self):
        return self.secret_key_yookassa


class Report(models.Model):
    user = models.CharField(
        max_length=400,
        verbose_name='Пользователь',
    )

    work_time = models.IntegerField(
        verbose_name='Количесвто часов в работе',
    )

    wt_hour = models.CharField(
        max_length=400,
        verbose_name='Потребление, кВт/ час',
    )

    sum_wt_hour = models.CharField(
        max_length=400,
        verbose_name='Суммарное потребление, кВт',
    )

    sum_two_wt_hour = models.CharField(
        max_length=400,
        verbose_name='Суммарное потребление 2, кВт',
    )

    tariff = models.CharField(
        max_length=400,
        verbose_name='Тариф',
    )

    main = models.CharField(
        max_length=400,
        verbose_name='Управление',
    )

    pay_main = models.CharField(
        max_length=400,
        verbose_name='Итог к оплате',
    )

    month = models.CharField(
        verbose_name='Месяц'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'

    def __str__(self):
        return self.month

    def __repr__(self):
        return self.month


class WorkerUser(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='наименование',
    )

    user = models.ForeignKey(
        TgUser,
        on_delete=models.CASCADE,
        related_name='me_workers',
        verbose_name='Пользователь',
    )

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return self.name


class ApplicationsSell(models.Model):
    status = models.BooleanField(
        default=False,
        verbose_name='Закрыта заявка'
    )

    user = models.ForeignKey(
        TgUser,
        on_delete=models.CASCADE,
        related_name='applications_sell',
    )

    class Meta:
        verbose_name = 'Заявка на продажу'
        verbose_name_plural = 'Заявки на продажу'


class ApplicationsBuy(models.Model):
    status = models.BooleanField(
        default=False,
        verbose_name='Закрыта заявка'
    )

    user = models.ForeignKey(
        TgUser,
        on_delete=models.CASCADE,
        related_name='applications_buy',

    )

    class Meta:
        verbose_name = 'Заявка на покупку'
        verbose_name_plural = 'Заявки на покупку'
