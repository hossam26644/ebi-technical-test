''' gene operations module, only including the gene-suggest get method '''
from flask_restplus import Resource
from apis.api import api
from models import models
from .arguments import gene_suggestion_arguments as arguments


gene_operations_namespace = api.namespace('gene_operations',
                                          description='EBI technical test service')

@gene_operations_namespace.route('/gene_suggest')
class GeneSuggest(Resource):
    ''' main resource class'''

    @api.expect(arguments)
    def get(self):
        ''' gene-suggest get method'''
        args = arguments.parse_args()
        query = args.get('query')
        species = args.get('species')
        limit = args.get('limit')

        #retrive_list_from_database function
        gene_suggestions = self.retrive_list_from_database(query, species, limit)
        #Using marshmallow for serialization (using the Geneschema)
        gene_schema = models.GeneSchema(many=True)
        output = gene_schema.dump(gene_suggestions).data
        #Return results in JSON to the user
        return {'result_list': output}

    #Takes query arguments and uses ORM model to get results
    def retrive_list_from_database(self, query, species, limit):
        ''' function that retrives result from database'''
        gene = models.Gene
        gene_suggestions = gene.query.filter_by(species=species)	\
                                    .filter(gene.display_label.like(query+'%'))\
                                    .with_entities(gene.display_label)\
                                    .group_by(gene.display_label)  \
                                    .order_by(gene.display_label)\
                                    .limit(limit).all()
        return gene_suggestions
