# coding: utf-8

"""
    Wavefront Public API

    <p>The Wavefront public API enables you to interact with Wavefront servers using standard web service API tools. You can use the API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wavefront_api_client.api_client import ApiClient


class MetricApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_metric_details(self, m, **kwargs):  # noqa: E501
        """Get more details on a metric, including reporting sources and approximate last time reported  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_metric_details(m, async=True)
        >>> result = thread.get()

        :param async bool
        :param str m: Metric name (required)
        :param int l: limit
        :param str c: cursor value to continue if the number of results exceeds 1000
        :param list[str] h: glob pattern for sources to include in the query result
        :return: MetricDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_metric_details_with_http_info(m, **kwargs)  # noqa: E501
        else:
            (data) = self.get_metric_details_with_http_info(m, **kwargs)  # noqa: E501
            return data

    def get_metric_details_with_http_info(self, m, **kwargs):  # noqa: E501
        """Get more details on a metric, including reporting sources and approximate last time reported  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_metric_details_with_http_info(m, async=True)
        >>> result = thread.get()

        :param async bool
        :param str m: Metric name (required)
        :param int l: limit
        :param str c: cursor value to continue if the number of results exceeds 1000
        :param list[str] h: glob pattern for sources to include in the query result
        :return: MetricDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['m', 'l', 'c', 'h']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metric_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'm' is set
        if ('m' not in params or
                params['m'] is None):
            raise ValueError("Missing the required parameter `m` when calling `get_metric_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'm' in params:
            query_params.append(('m', params['m']))  # noqa: E501
        if 'l' in params:
            query_params.append(('l', params['l']))  # noqa: E501
        if 'c' in params:
            query_params.append(('c', params['c']))  # noqa: E501
        if 'h' in params:
            query_params.append(('h', params['h']))  # noqa: E501
            collection_formats['h'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/x-javascript', 'application/javascript'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/chart/metric/detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MetricDetailsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
