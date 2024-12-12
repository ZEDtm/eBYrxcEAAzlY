

from aiogram.filters.callback_data import CallbackData


class MenuCallbackData(CallbackData, prefix='menu'):
    lk: bool = False
    report: bool = False
    help: bool = False
    buy: bool = False
    sell: bool = False
    dogovor: bool = False


class SupportCallbackData(CallbackData, prefix='help'):
    write: bool = False
    call: bool = False

class CurrencyChooseCallbackData(CallbackData, prefix='currency'):
    id: int


class IncomeExpensesCallbackData(CallbackData, prefix='income_expenses'):
    id: int
    income: bool = False
    expenses: bool = False


class AddCheckCallbackData(CallbackData, prefix='add_check'):
    id: int
    skip: bool = False


class BaseMenuCallbackData(CallbackData, prefix='base_menu'):
    profile: bool = False
    calculate: bool = False
    add_operation: bool = False
    setting: bool = False
    push: bool = False
    helpful_material: bool = False
    help: bool = False


class BackCallbackData(CallbackData, prefix='back'):
    start: bool = False
    help: bool = False


class FillApplicationCallbackData(CallbackData, prefix='fill'):
    start: bool = False



class SendDocumentCallbackData(CallbackData, prefix='send'):
    upload: bool = False
    skip: bool = False



class SettingCallbackData(CallbackData, prefix='setting'):
    tag: bool = False
    category: bool = False


class CategoryTagsCallbackData(CallbackData, prefix='settings_cat_tag'):
    id: int
    tag: bool = False
    category: bool = False


class WorkTagsCallbackData(CallbackData, prefix='work_tag'):
    id: int | None = None
    add: bool = False
    edit: bool = False
    delete: bool = False


class WorkCategoriesCallbackData(CallbackData, prefix='workcategory'):
    id: int | None = None
    add: bool = False
    edit: bool = False
    delete: bool = False


class EditCategoryCallbackData(CallbackData, prefix='edit_category'):
    id: int
    name: bool = False
    tag: bool = False


class ProfileCallbackData(CallbackData, prefix='profile'):
    fill_profile: bool = False
    tariff: bool = False


class PayCallbackData(CallbackData, prefix='payments'):
    id: int


class Account(CallbackData, prefix='account'):
    yes: bool = False
    no: bool = False


class ServiceCallback(CallbackData, prefix='service'):
    yes: bool = True