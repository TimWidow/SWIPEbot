from deserializers.base import BaseDeserializer


class UserDeserializer(BaseDeserializer):
    async def for_detail(self, data: dict) -> tuple:
        info = f"{data['first_name'] or '' + ' ' + data['last_name'] or ''} - {data['phone']}\n {data['email'] or 'Не указано'}"
        return await self.get_namedtuple(data['pk'], info)

    async def for_list(self, data: dict) -> tuple:
        info = f"{data['phone']}"
        return await self.get_namedtuple(data['pk'], info)
