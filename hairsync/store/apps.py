from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "store"

    # add this
    # What we did is override the ready() method of the users app config to perform initialization task which is registering signals
    def ready(self):
        import store.signals  # nameofapp.signals
