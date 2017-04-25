# coding: utf-8

from __future__ import absolute_import
from image_hash.models.metadata import Metadata
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ImageHashRequest(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, filepath=None, url=None, metadata=None):
        """
        ImageHashRequest - a model defined in Swagger

        :param filepath: The filepath of this ImageHashRequest.
        :type filepath: str
        :param url: The url of this ImageHashRequest.
        :type url: str
        :param metadata: The metadata of this ImageHashRequest.
        :type metadata: Metadata
        """
        self.swagger_types = {
            'filepath': str,
            'url': str,
            'metadata': Metadata
        }

        self.attribute_map = {
            'filepath': 'filepath',
            'url': 'url',
            'metadata': 'metadata'
        }

        self._filepath = filepath
        self._url = url
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ImageHashRequest of this ImageHashRequest.
        :rtype: ImageHashRequest
        """
        return deserialize_model(dikt, cls)

    @property
    def filepath(self):
        """
        Gets the filepath of this ImageHashRequest.
        The path to save the image to in the database. If another image already exists at the given path, it will be overwritten.

        :return: The filepath of this ImageHashRequest.
        :rtype: str
        """
        return self._filepath

    @filepath.setter
    def filepath(self, filepath):
        """
        Sets the filepath of this ImageHashRequest.
        The path to save the image to in the database. If another image already exists at the given path, it will be overwritten.

        :param filepath: The filepath of this ImageHashRequest.
        :type filepath: str
        """

        self._filepath = filepath

    @property
    def url(self):
        """
        Gets the url of this ImageHashRequest.
        The image to add to the database.

        :return: The url of this ImageHashRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ImageHashRequest.
        The image to add to the database.

        :param url: The url of this ImageHashRequest.
        :type url: str
        """

        self._url = url

    @property
    def metadata(self):
        """
        Gets the metadata of this ImageHashRequest.

        :return: The metadata of this ImageHashRequest.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this ImageHashRequest.

        :param metadata: The metadata of this ImageHashRequest.
        :type metadata: Metadata
        """

        self._metadata = metadata

