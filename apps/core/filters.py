lookup_types_string = ['exact', 'iexact', 'contains', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ]

lookup_types_number = ['exact', 'contains', 'gt', 'gte', 'lt', 'lte', 'in', 'range']

lookup_types_date = [
    'exact',
    'range',
    'year', 'year__gte', 'year__gt', 'year__lte', 'year__lt', 'year__range', 'year__in',
    'month', 'month__gte', 'month__gt', 'month__lte', 'month__lt', 'month__range', 'month__in',
    'day', 'day__gte', 'day__gt', 'day__lte', 'day__lt', 'day__range', 'day__in',
    'gte',
    'gt',
    'lte',
    'lt',
    'in',
]

lookup_types_hours = [
    'exact',
    'range',
    'hour', 'hour__gte', 'hour__gt', 'hour__lte', 'hour__lt', 'hour__range', 'hour__in',
    'minute', 'minute__gte', 'minute__gt', 'minute__lte', 'minute__lt', 'minute__range', 'minute__in',
    'second', 'second__gte', 'second__gt', 'second__lte', 'second__lt', 'second__range', 'second__in',
    'gte',
    'gt',
    'lte',
    'lt',
    'in',
]

lookup_types_base = {
    'active': lookup_types_string,
    'dma_created': lookup_types_date,
    'hms_created': lookup_types_hours,
    'dma_alteration': lookup_types_date,
    'hms_alteration': lookup_types_hours,
}
