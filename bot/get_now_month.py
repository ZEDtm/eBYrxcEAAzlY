from datetime import datetime

import pytz


def month_name_to_number() -> tuple[str, int]:
    now = datetime.now(pytz.timezone('Europe/Moscow')).date()

    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "майя", 6: "июня",
        7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }

    return months.get(now.month), now.month