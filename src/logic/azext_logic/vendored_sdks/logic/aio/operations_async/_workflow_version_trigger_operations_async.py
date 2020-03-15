# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class WorkflowVersionTriggerOperations:
    """WorkflowVersionTriggerOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~logic_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def list_callback_url(
        self,
        resource_group_name: str,
        workflow_name: str,
        version_id: str,
        trigger_name: str,
        parameters: Optional["models.GetCallbackUrlParameters"] = None,
        **kwargs
    ) -> "models.WorkflowTriggerCallbackUrl":
        """Get the callback url for a trigger of a workflow version.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workflow_name: The workflow name.
        :type workflow_name: str
        :param version_id: The workflow versionId.
        :type version_id: str
        :param trigger_name: The workflow trigger name.
        :type trigger_name: str
        :param parameters: The callback URL parameters.
        :type parameters: ~logic_management_client.models.GetCallbackUrlParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkflowTriggerCallbackUrl or the result of cls(response)
        :rtype: ~logic_management_client.models.WorkflowTriggerCallbackUrl
        :raises: ~logic_management_client.models.ErrorResponseException:
        """
        cls: ClsType["models.WorkflowTriggerCallbackUrl"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-05-01"

        # Construct URL
        url = self.list_callback_url.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workflowName': self._serialize.url("workflow_name", workflow_name, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str'),
            'triggerName': self._serialize.url("trigger_name", trigger_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if parameters is not None:
            body_content = self._serialize.body(parameters, 'GetCallbackUrlParameters')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        deserialized = self._deserialize('WorkflowTriggerCallbackUrl', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list_callback_url.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/versions/{versionId}/triggers/{triggerName}/listCallbackUrl'}
