import os
import connexion
import json
import logging

from image_hash.models import ImageHashRequest, ImageHashSearchRequest, ImageMatchResponse, ImageMatchSearchResponse, ImageMatchSearchItem, Metadata

from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
from image_match.goldberg import ImageSignature

log = logging.getLogger('werkzeug')

ES = Elasticsearch('http://elasticsearch:9200')
INDEX_NAME = 'cvtool'
ES_DOC_TYPE = 'image_hash'


def parent_id(tenant_id, project_id):
    return '%s|%s' % (tenant_id, project_id)

def signature_es(index_name):
    return SignatureES(ES, index=index_name, doc_type=ES_DOC_TYPE)

def dist_to_percent(dist):
    return (1 - dist) * 100    

def add(tenant_id, project_id, image_hash_request):
    """
    add
    Adds an image signature to the database.
    :param tenant_id: tenant id
    :type tenant_id: str
    :param project_id: project id
    :type project_id: str
    :param image_hash_request: ImageHash to create
    :type image_hash_request: dict | bytes

    :rtype: ImageMatchResponse
    """
    if connexion.request.is_json:
        image_hash_request = ImageHashRequest.from_dict(connexion.request.get_json())
        ses = signature_es(tenant_id)
        metadata = image_hash_request.metadata if image_hash_request.metadata is not None else dict()
        metadata['parent_id'] = parent_id(tenant_id, project_id)
        ses.add_image(image_hash_request.filepath, image_hash_request.url, bytestream=False, metadata=metadata)
        return ImageMatchResponse.from_dict({
            'status': 'ok',
            'error': [],
            'method': 'add',
            'result': []
        })        


def search(tenant_id, project_id, search_request):
    """
    search
    Searches for a similar image in the database. Scores range from 0 to 100, with 100 being a perfect match.
    :param tenant_id: tenant id
    :type tenant_id: str
    :param project_id: project id
    :type project_id: str
    :param search_request: Search parameters
    :type search_request: dict | bytes

    :rtype: ImageMatchSearchResponse
    """

    request = connexion.request
    if request.is_json:
        search_request = ImageHashSearchRequest.from_dict(request.get_json())
        ses = signature_es(INDEX_NAME)
        matches = ses.search_image(
                path=search_request.url,
                all_orientations=search_request.all_orientations,
                bytestream=False,
                pre_filter={"term": {"metadata.parent_id": parent_id(tenant_id, project_id)}})

        response = ImageMatchSearchResponse.from_dict({
            'status': 'ok',
            'error': [],
            'method': 'search'
        })
        response.results = [to_item(m) for m in matches]
        return response    


def to_item(m): 
    return ImageMatchSearchItem.from_dict({
            'score': dist_to_percent(m['dist']),
            'filepath': m['path'],
            'metadata': Metadata.from_dict(m['metadata'])
    })