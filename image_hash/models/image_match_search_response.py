# coding: utf-8

from __future__ import absolute_import
from image_hash.models.image_match_search_item import ImageMatchSearchItem
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ImageMatchSearchResponse(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, method=None, error=None, status=None, results=None):
        """
        ImageMatchSearchResponse - a model defined in Swagger

        :param method: The method of this ImageMatchSearchResponse.
        :type method: str
        :param error: The error of this ImageMatchSearchResponse.
        :type error: str
        :param status: The status of this ImageMatchSearchResponse.
        :type status: str
        :param results: The results of this ImageMatchSearchResponse.
        :type results: List[ImageMatchSearchItem]
        """
        self.swagger_types = {
            'method': str,
            'error': str,
            'status': str,
            'results': List[ImageMatchSearchItem]
        }

        self.attribute_map = {
            'method': 'method',
            'error': 'error',
            'status': 'status',
            'results': 'results'
        }

        self._method = method
        self._error = error
        self._status = status
        self._results = results

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ImageMatchSearchResponse of this ImageMatchSearchResponse.
        :rtype: ImageMatchSearchResponse
        """
        return deserialize_model(dikt, cls)

    @property
    def method(self):
        """
        Gets the method of this ImageMatchSearchResponse.

        :return: The method of this ImageMatchSearchResponse.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this ImageMatchSearchResponse.

        :param method: The method of this ImageMatchSearchResponse.
        :type method: str
        """

        self._method = method

    @property
    def error(self):
        """
        Gets the error of this ImageMatchSearchResponse.

        :return: The error of this ImageMatchSearchResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this ImageMatchSearchResponse.

        :param error: The error of this ImageMatchSearchResponse.
        :type error: str
        """

        self._error = error

    @property
    def status(self):
        """
        Gets the status of this ImageMatchSearchResponse.

        :return: The status of this ImageMatchSearchResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ImageMatchSearchResponse.

        :param status: The status of this ImageMatchSearchResponse.
        :type status: str
        """

        self._status = status

    @property
    def results(self):
        """
        Gets the results of this ImageMatchSearchResponse.

        :return: The results of this ImageMatchSearchResponse.
        :rtype: List[ImageMatchSearchItem]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this ImageMatchSearchResponse.

        :param results: The results of this ImageMatchSearchResponse.
        :type results: List[ImageMatchSearchItem]
        """

        self._results = results

