#!/usr/bin/python
#
# Copyright 2018 Kaggle Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Kaggle API

    API for kaggle.com  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kaggle.models.dataset_upload_file import DatasetUploadFile  # noqa: F401,E501


class DatasetNewVersionRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'version_notes': 'str',
        'description': 'str',
        'files': 'list[DatasetUploadFile]',
        'convert_to_csv': 'bool',
        'category_ids': 'list[str]',
        'delete_old_versions': 'bool'
    }

    attribute_map = {
        'version_notes': 'versionNotes',
        'description': 'description',
        'files': 'files',
        'convert_to_csv': 'convertToCsv',
        'category_ids': 'categoryIds',
        'delete_old_versions': 'deleteOldVersions'
    }

    def __init__(self, version_notes=None, description=None, files=None, convert_to_csv=True, category_ids=None, delete_old_versions=False):  # noqa: E501
        """DatasetNewVersionRequest - a model defined in Swagger"""  # noqa: E501

        self._version_notes = None
        self._description = None
        self._files = None
        self._convert_to_csv = None
        self._category_ids = None
        self._delete_old_versions = None
        self.discriminator = None

        self.version_notes = version_notes
        if description is not None:
            self.description = description
        self.files = files
        if convert_to_csv is not None:
            self.convert_to_csv = convert_to_csv
        if category_ids is not None:
            self.category_ids = category_ids
        if delete_old_versions is not None:
            self.delete_old_versions = delete_old_versions

    @property
    def version_notes(self):
        """Gets the version_notes of this DatasetNewVersionRequest.  # noqa: E501


        :return: The version_notes of this DatasetNewVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._version_notes

    @version_notes.setter
    def version_notes(self, version_notes):
        """Sets the version_notes of this DatasetNewVersionRequest.


        :param version_notes: The version_notes of this DatasetNewVersionRequest.  # noqa: E501
        :type: str
        """
        if version_notes is None:
            raise ValueError("Invalid value for `version_notes`, must not be `None`")  # noqa: E501

        self._version_notes = version_notes

    @property
    def description(self):
        """Gets the description of this DatasetNewVersionRequest.  # noqa: E501


        :return: The description of this DatasetNewVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DatasetNewVersionRequest.


        :param description: The description of this DatasetNewVersionRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def files(self):
        """Gets the files of this DatasetNewVersionRequest.  # noqa: E501


        :return: The files of this DatasetNewVersionRequest.  # noqa: E501
        :rtype: list[DatasetUploadFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this DatasetNewVersionRequest.


        :param files: The files of this DatasetNewVersionRequest.  # noqa: E501
        :type: list[DatasetUploadFile]
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files

    @property
    def convert_to_csv(self):
        """Gets the convert_to_csv of this DatasetNewVersionRequest.  # noqa: E501


        :return: The convert_to_csv of this DatasetNewVersionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._convert_to_csv

    @convert_to_csv.setter
    def convert_to_csv(self, convert_to_csv):
        """Sets the convert_to_csv of this DatasetNewVersionRequest.


        :param convert_to_csv: The convert_to_csv of this DatasetNewVersionRequest.  # noqa: E501
        :type: bool
        """

        self._convert_to_csv = convert_to_csv

    @property
    def category_ids(self):
        """Gets the category_ids of this DatasetNewVersionRequest.  # noqa: E501


        :return: The category_ids of this DatasetNewVersionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._category_ids

    @category_ids.setter
    def category_ids(self, category_ids):
        """Sets the category_ids of this DatasetNewVersionRequest.


        :param category_ids: The category_ids of this DatasetNewVersionRequest.  # noqa: E501
        :type: list[str]
        """

        self._category_ids = category_ids

    @property
    def delete_old_versions(self):
        """Gets the delete_old_versions of this DatasetNewVersionRequest.  # noqa: E501


        :return: The delete_old_versions of this DatasetNewVersionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._delete_old_versions

    @delete_old_versions.setter
    def delete_old_versions(self, delete_old_versions):
        """Sets the delete_old_versions of this DatasetNewVersionRequest.


        :param delete_old_versions: The delete_old_versions of this DatasetNewVersionRequest.  # noqa: E501
        :type: bool
        """

        self._delete_old_versions = delete_old_versions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DatasetNewVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
