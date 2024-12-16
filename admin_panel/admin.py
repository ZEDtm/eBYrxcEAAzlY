import requests
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.signals import post_import

from admin_panel.forms import MailingForm
from admin_panel.models import TgUser, Mailing, Admin, InviteUser, YookassaConfig, Report, ApplicationsBuy, \
    ApplicationsSell, GroupUser, User


class BotAdminSite(admin.AdminSite):

    site_title = "Управление ботом"
    site_header = "Управление ботом"
    index_title = "Управление ботом"

    def get_app_list(self, request, app_label=None):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)

        admin_panel_app_url = app_dict.get('admin_panel', {}).get('app_url')
        if settings.ADMIN_ORDER_MODELS:

            for order_models in settings.ADMIN_ORDER_MODELS:

                for name_model in order_models.keys():

                    if name_model not in app_dict:
                        app_dict[name_model] = {
                            "name": name_model,
                            "app_label": name_model,
                            "app_url": admin_panel_app_url,
                            "has_module_perms": True,
                            "models": [],
                        }

                    try:

                        for model_data in app_dict['admin_panel']['models']:

                            if model_data['object_name'] in order_models.get(name_model):
                                model_data['app_label'] = name_model

                                app_dict[name_model]['models'].append(model_data)

                            app_dict['admin_panel']['models'] = [
                                model_data for model_data in app_dict['admin_panel']['models'] if
                                model_data['object_name'] not in order_models.get(name_model)
                            ]

                    except KeyError:
                        pass
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        return app_list


bot_admin = BotAdminSite()


#
# class UserFilter(admin.SimpleListFilter):
#     title = 'Пользователь'
#     parameter_name = 'user'
#
#     def lookups(self, request, model_admin):
#         users = set(chat.user for chat in model_admin.model.objects.all())
#         return [(user.id, user.username) for user in users]
#
#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(user__id=self.value())
#         return queryset

class ReportResource(resources.ModelResource):
    user = Field(attribute='user', column_name='Пользователь')
    work_time = Field(attribute='work_time', column_name='Количесвто часов в работе')
    wt_hour = Field(attribute='wt_hour', column_name='Потребление, кВт/ час')
    sum_wt_hour = Field(attribute='sum_wt_hour', column_name='Суммарное потребление, кВт')
    sum_two_wt_hour = Field(attribute='sum_two_wt_hour', column_name='Суммарное потребление 2, кВт')
    tariff = Field(attribute='tariff', column_name='Тариф')
    main = Field(attribute='main', column_name='Управление')
    pay_main = Field(attribute='pay_main', column_name='Итог к оплате')
    # usdt = Field(attribute='usdt', column_name='USDT')
    month = Field(attribute='month', column_name='Месяц')

    class Meta:
        model = Report
        fields = (
            'user',
            'work_time',
            'wt_hour',
            'sum_wt_hour',
            'sum_two_wt_hour',
            'tariff',
            'main',
            'pay_main',
            # 'usdt',
            'month',
        )
        import_id_fields = ()

    def export(self, queryset=None, *args, **kwargs, ):
        queryset = queryset
        return super(ReportResource, self).export(queryset, *args, **kwargs)


@admin.register(Mailing, site=bot_admin)
class MailingAdmin(admin.ModelAdmin):
    add_form_template = 'form_mailing.html'
    list_display = (
        'pk',
        'media_type',
        'text',
        'file_id',
        'date_malling',
        'is_sent',
    )
    list_display_links = ('pk',)

    def add_view(self,
                 request,
                 form_url='',
                 extra_context=None):
        extra_context = extra_context or {}
        extra_context['form'] = MailingForm()

        return super().add_view(request, form_url, extra_context)

    class Meta:
        verbose_name_plural = 'Рассылка'


@admin.register(TgUser, site=bot_admin)
class TgUserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'username', 'block')
    list_filter = ('block',)
    readonly_fields = ('telegram_id', 'username')
    search_fields = ('telegram_id', 'username', 'ref_code', 'fio')
    list_editable = ('block',)
    ordering = ('-telegram_id',)



    def save_model(self, request, obj, form, change):
        if change:  # if the object is being updated
            old_obj = TgUser.objects.get(pk=obj.pk)
            if obj.status_asccount:
                if old_obj.status_asccount != obj.status_asccount:
                    # Если статус изменился с False на True, отправляем уведомление
                    url = f"https://api.telegram.org/bot{settings.TG_TOKEN_BOT}/SendMessage"
                    chat_id = obj.telegram_id
                    requests.post(
                        url, json={
                            'chat_id': chat_id,
                            'text': 'Ваш договор был подписан, нажмите /start для получения меню',
                        })
        super().save_model(request, obj, form, change)


@admin.register(Admin, site=bot_admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('telegram_id',)
    search_fields = ('telegram_id',)


@admin.register(InviteUser, site=bot_admin)
class InviteUserAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'tg_user_ref_link')
    search_fields = ('fio', 'phone')
    exclude = ('user',)

    def tg_user_ref_link(self, invite_user: InviteUser):
        if not invite_user.user.group:
            invite_user.user.group.set(invite_user.group.all())
        if invite_user.user:
            if invite_user.user.ref_code:
                return f'{settings.LINK_BOT}?start={invite_user.user.ref_code}'
        return ''


@admin.register(GroupUser, site=bot_admin)
class GroupUserAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(YookassaConfig, site=bot_admin)
class YookassaConfigAdmin(admin.ModelAdmin):
    pass


@admin.register(Report, site=bot_admin)
class ReportAdmin(ImportExportModelAdmin):
    resource_classes = [ReportResource]

    list_display = (
        'user', 'work_time', 'wt_hour', 'sum_wt_hour', 'sum_two_wt_hour', 'tariff', 'main', 'pay_main', 'month')

    # Фильтры для боковой панели
    list_filter = ('user', 'month')

    # Поля для поиска
    search_fields = ('user', 'month')

    fieldsets = (
        (None, {
            'fields': ('user', 'month')
        }),
        ('Рабочая информация', {
            'fields': ('work_time', 'wt_hour', 'sum_wt_hour', 'sum_two_wt_hour')
        }),
        ('Финансовая информация', {
            'fields': ('tariff', 'main', 'pay_main')
        }),
    )

    def process_result(self, result, request):
        self.add_success_message(result, request)
        post_import.send(sender=None, model=self.model)

        url = reverse(
            "admin:%s_%s_changelist" % self.get_model_info(),
            current_app=self.admin_site.name,
        )
        return HttpResponseRedirect(url)


@admin.register(ApplicationsSell, site=bot_admin)
class ApplicationsSellAdmin(admin.ModelAdmin):
    list_display = (
        'user_fio', 'user_username', 'user_phone',
        'status', 'user_telegram_id'
    )

    def user_fio(self, obj):
        return obj.user.fio

    user_fio.short_description = 'ФИО'

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = 'Имя пользователя'

    def user_phone(self, obj):
        return obj.user.phone

    user_phone.short_description = 'Номер телефона'

    def user_telegram_id(self, obj):
        return obj.user.telegram_id

    user_telegram_id.short_description = 'Telegram ID'


@admin.register(ApplicationsBuy, site=bot_admin)
class ApplicationsBuyAdmin(admin.ModelAdmin):
    list_display = (
        'user_fio', 'user_username', 'user_phone',
        'status', 'user_telegram_id'
    )

    def user_fio(self, obj):
        return obj.user.fio

    user_fio.short_description = 'ФИО'

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = 'Имя пользователя'

    def user_phone(self, obj):
        return obj.user.phone

    user_phone.short_description = 'Номер телефона'

    def user_telegram_id(self, obj):
        return obj.user.telegram_id

    user_telegram_id.short_description = 'Telegram ID'
