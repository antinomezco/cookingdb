from rest_framework import pagination


class StandardResultsSetPagination(pagination.PageNumberPagination):
    # change the records per page from here
    page_size = 8
    # change the query name for the amount of records per page, ex: size=8
    page_size_query_param = 'size'
