from aiogram.fsm.state import StatesGroup, State


class UserStart(StatesGroup):
    start = State()
    send_passport = State()
    number_invoice = State()
    get_verify_code = State()
    send_number_account = State()
    wait_pay = State()
    passport_get = State()
    passport_date = State()
    address_registration = State()
    send_bic = State()
    send_correspondent = State()
    send_bank_name = State()

    send_name_worker = State()


class UserMain(StatesGroup):
    profile = State()
    send_tag = State()
    edit_name_tag = State()
    send_category = State()
    send_category_tag = State()

    input_fio = State()

    input_operation = State()
    send_photo = State()


    edit_only_name = State()
    edit_only_tag = State()
