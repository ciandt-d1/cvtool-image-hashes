# coding: utf-8

from __future__ import absolute_import

from image_hash.models.image_match_response import ImageMatchResponse
from image_hash.models.image_match_search_response import ImageMatchSearchResponse
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_add(self):
        """
        Test case for add

        
        """
        data = dict(filepath='filepath_example',
                    url='url_example',
                    image=(BytesIO(b'some file data'), 'file.txt'),
                    metadata='metadata_example',
                    all_orientations=true)
        response = self.client.open('/v1/image-hashes/',
                                    method='POST',
                                    data=data,
                                    content_type='multipart/form-data')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete(self):
        """
        Test case for delete

        
        """
        response = self.client.open('/v1/image-hashes/{filepath}',
                                    method='DELETE',
                                    content_type='multipart/form-data')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_search(self):
        """
        Test case for search

        
        """
        data = dict(filepath='filepath_example',
                    url='url_example',
                    image=(BytesIO(b'some file data'), 'file.txt'),
                    metadata='metadata_example',
                    all_orientations=true)
        response = self.client.open('/v1/image-hashes/search',
                                    method='POST',
                                    data=data,
                                    content_type='multipart/form-data')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
