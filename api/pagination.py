from rest_framework import pagination



class PaginacaoVagas(pagination.PageNumberPagination):
    page_size = 2                          # quantos registros serão exibidos por página;
    page_query_param = 'page'              # qual o parâmetro responsável por navegar entre as páginas. 
    page_size_query_param = 'per_page'     # Valor de registros que queremos exibir em tempo de execução;
    max_page_size = 4                      # quantidade máxima de registros que será exibida por página.