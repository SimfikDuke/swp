from root.handlers_space import BaseHS
import root.db_models as models


class RecordsHS(BaseHS):
    def add_record(self, title: str, text: str):
        user_id = self.user.id if self.user is not None else 0
        if len(title) < 35 and len(text) < 300:
            self.session.add(models.Record(user_id, title, text))

    def delete(self, record_id: int):
        record = self.session.query(models.Record)\
            .filter(models.Record.id == record_id)\
            .first()
        if record is not None:
            self.session.delete(record)
