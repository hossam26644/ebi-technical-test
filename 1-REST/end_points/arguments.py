''' argumets expected by gene_suggest get method '''
from flask_restplus import reqparse

gene_suggestion_arguments = reqparse.RequestParser()
gene_suggestion_arguments.add_argument('query',
									   type=str,
									   help='the partial query typed by the user, e.g. `brc` ',
									   default="")

gene_suggestion_arguments.add_argument('species',
									    type=str, help='the name of the target species, e.g. `homo_sapiens`',
									    required=True)

gene_suggestion_arguments.add_argument('limit',
										type=int,
										help='the maximum number of suggestions to return, e.g. `10`',
										required=True)
