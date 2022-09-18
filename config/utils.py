from django.core.cache import cache


def delete_cache(key_prefix: str):
    keys_pattern = f"views.decorators.cache.*.{key_prefix}.*"
    cache.delete_pattern(keys_pattern)
