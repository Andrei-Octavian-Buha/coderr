from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'page_size' # Permite utilizatorului să pună ?page_size=X
    max_page_size = 100