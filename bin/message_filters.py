from telegram.ext import BaseFilter
from bin.var import superuser_id


class IsDev(BaseFilter):
    @classmethod
    def filter(cls, message):
        return message.from_user.id in superuser_id


is_dev_filter = IsDev()
