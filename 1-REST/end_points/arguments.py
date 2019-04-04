''' argumets api expects '''
from flask_restplus import reqparse

gene_suggestion_arguments = reqparse.RequestParser()
gene_suggestion_arguments.add_argument('query', type=str, help='Query', default="")
gene_suggestion_arguments.add_argument('species', type=str, help='Species', required=True)
gene_suggestion_arguments.add_argument('limit', type=int, help='Limit', required=True)
