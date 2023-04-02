from apps.core.serializers import BaseSerializer
from apps.core.filters import lookup_types_base
import django_filters
from apps.parametro.models import Parametro
from apps.core.filters import lookup_types_string

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


def fields_base_serializer(serializerClass):
    class SerializerClass(serializerClass):
        class Meta(serializerClass.Meta):
            fields = serializerClass.Meta.fields.copy()
            fields += BaseSerializer.Meta.fields.copy()

    def decorator():
        return SerializerClass

    return decorator()


# def fields_base_filter_set(filtersetClass):
#     class FilterSetClass(filtersetClass):
#         class Meta(filtersetClass.Meta):
#             fields = filtersetClass.Meta.fields
#             fields.update(lookup_types_base)

#     def decorator():
#         return FilterSetClass

#     return decorator()