from django.core.exceptions import ObjectDoesNotExist

class BaseRepository:
    _model = None  # Захищений атрибут для моделі

    def get_all(self):
        """Отримати всі записи моделі"""
        return self._model.objects.all()

    '''def get_by_id(self, pk):
        """Отримати запис по ID"""
        return self._get_by_id(pk)'''

    def create(self, **kwargs):
        """Створити новий запис"""
        return self._model.objects.create(**kwargs)

    def get_by_id(self, pk):
        """Захищений метод для пошуку по ID"""
        try:
            return self._model.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def delete_by_id(self, pk):
        """Видалити запис по ID"""
        try:
            instance = self._model.objects.get(pk=pk)
            instance.delete()
            return instance
        except ObjectDoesNotExist:
            return None