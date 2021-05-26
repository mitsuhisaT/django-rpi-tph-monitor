"""
Functions for converting Django QuerySet to CVSs.

@date 02 May 2021
@author mitsuhisaT <asihustim@gmail.com>

See:
    https://docs.djangoproject.com/en/3.2/howto/outputting-csv/
    https://www.codingforentrepreneurs.com/blog/django-queryset-to-csv-files-datasets
"""
import pandas as pd


def get_field_names(model, ignore_fields=['content_object']):
    """
    Get fields names.

    This method gets all model field names (as strings) and return a list
    of them ignoring the ones we know don't work (like the 'content_object'
    field).

    Args:
        ignore_fields List<str>: a list of field names to ignore by default.

    Returns:
        List(str): field names.
    """
    flds = model._meta.fields
    return list(set([f.name for f in flds if f.name not in ignore_fields]))


def get_lookup_fields(model, fields=None):
    """
    Get lookup fields.

    This method compare the lookups we want vs the lookups that are
    available. It ignores the unavailable fields we passed.

    Args:
        fields List(str): a list of field name strings.

    Returns:
        List(str) : a list of field names.
    """
    field_names = get_field_names(model)
    if fields is not None:
        '''
        we'll iterate through all the passed field_names and verify they
        are valid bby only includeing the valid ones.
        '''
        lookup_fields = []
        for x in fields:
            if '__' in x:
                # the __ is for ForeignKey lookups
                lookup_fields.append(x)
            elif x in field_names:
                lookup_fields.append(x)
    else:
        '''
        No field names were passed, use the default model fields.
        '''
        lookup_fields = field_names
    return lookup_fields


def qs2dataset(qs, fields=None):
    """
    Convert QuerySet to dictionaries.

    This method simply calling the fields we formed on the queryset and
    turning it into a list of dictionaries with key/value pairs.

    Args:
        qs (QuerySet): any Djang QuerySet.
        fields List(str): a list of field name strings, ignore non-model
            field names.

    Returns:
        List(dict): a list of dictionaries(key: filed name, value: data).
    """
    lookup_fields = get_lookup_fields(qs.model, fields=fields)
    return list(qs.values(*lookup_fields))


def qs2dataframe(qs, fields=None, index=None):
    """
    Convert from dataset to dataframe.

    Args:
        qs (QuerySet): an QuerySet from Django.
        fields List(str): a list of field names from the Model of the QuerySet.
        index (str): the preferred index column we want our dataframe
        to be set to.

    Returns:
        pandas.DataFrame:
    """
    lookup_fields = get_lookup_fields(qs.model, fields=fields)
    index_col = None
    if index in lookup_fields:
        index_col = index
    elif 'id' in lookup_fields:
        index_col = 'id'
    values = qs2dataset(qs, fields=fields)
    df = pd.DataFrame.from_records(
        values,
        columns=lookup_fields,
        index=index_col,
        )
    return df
