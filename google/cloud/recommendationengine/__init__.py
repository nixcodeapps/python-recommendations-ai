# -*- coding: utf-8 -*-
#
from google.cloud.recommendationengine import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.recommendationengine_v1beta1.services.catalog_service.client import (
    CatalogServiceClient,
)
from google.cloud.recommendationengine_v1beta1.services.catalog_service.async_client import (
    CatalogServiceAsyncClient,
)
from google.cloud.recommendationengine_v1beta1.services.prediction_api_key_registry.client import (
    PredictionApiKeyRegistryClient,
)
from google.cloud.recommendationengine_v1beta1.services.prediction_api_key_registry.async_client import (
    PredictionApiKeyRegistryAsyncClient,
)
from google.cloud.recommendationengine_v1beta1.services.prediction_service.client import (
    PredictionServiceClient,
)
from google.cloud.recommendationengine_v1beta1.services.prediction_service.async_client import (
    PredictionServiceAsyncClient,
)
from google.cloud.recommendationengine_v1beta1.services.user_event_service.client import (
    UserEventServiceClient,
)
from google.cloud.recommendationengine_v1beta1.services.user_event_service.async_client import (
    UserEventServiceAsyncClient,
)

from google.cloud.recommendationengine_v1beta1.types.catalog import CatalogItem
from google.cloud.recommendationengine_v1beta1.types.catalog import Image
from google.cloud.recommendationengine_v1beta1.types.catalog import ProductCatalogItem
from google.cloud.recommendationengine_v1beta1.types.catalog_service import (
    CreateCatalogItemRequest,
)
from google.cloud.recommendationengine_v1beta1.types.catalog_service import (
    DeleteCatalogItemRequest,
)
from google.cloud.recommendationengine_v1beta1.types.catalog_service import (
    GetCatalogItemRequest,
)
from google.cloud.recommendationengine_v1beta1.types.catalog_service import (
    ListCatalogItemsRequest,
)
from google.cloud.recommendationengine_v1beta1.types.catalog_service import (
    ListCatalogItemsResponse,
)
from google.cloud.recommendationengine_v1beta1.types.catalog_service import (
    UpdateCatalogItemRequest,
)
from google.cloud.recommendationengine_v1beta1.types.common import FeatureMap
from google.cloud.recommendationengine_v1beta1.types.import_ import CatalogInlineSource
from google.cloud.recommendationengine_v1beta1.types.import_ import GcsSource
from google.cloud.recommendationengine_v1beta1.types.import_ import (
    ImportCatalogItemsRequest,
)
from google.cloud.recommendationengine_v1beta1.types.import_ import (
    ImportCatalogItemsResponse,
)
from google.cloud.recommendationengine_v1beta1.types.import_ import ImportErrorsConfig
from google.cloud.recommendationengine_v1beta1.types.import_ import ImportMetadata
from google.cloud.recommendationengine_v1beta1.types.import_ import (
    ImportUserEventsRequest,
)
from google.cloud.recommendationengine_v1beta1.types.import_ import (
    ImportUserEventsResponse,
)
from google.cloud.recommendationengine_v1beta1.types.import_ import InputConfig
from google.cloud.recommendationengine_v1beta1.types.import_ import (
    UserEventImportSummary,
)
from google.cloud.recommendationengine_v1beta1.types.import_ import (
    UserEventInlineSource,
)
from google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service import (
    CreatePredictionApiKeyRegistrationRequest,
)
from google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service import (
    DeletePredictionApiKeyRegistrationRequest,
)
from google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service import (
    ListPredictionApiKeyRegistrationsRequest,
)
from google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service import (
    ListPredictionApiKeyRegistrationsResponse,
)
from google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service import (
    PredictionApiKeyRegistration,
)
from google.cloud.recommendationengine_v1beta1.types.prediction_service import (
    PredictRequest,
)
from google.cloud.recommendationengine_v1beta1.types.prediction_service import (
    PredictResponse,
)
from google.cloud.recommendationengine_v1beta1.types.user_event import EventDetail
from google.cloud.recommendationengine_v1beta1.types.user_event import ProductDetail
from google.cloud.recommendationengine_v1beta1.types.user_event import (
    ProductEventDetail,
)
from google.cloud.recommendationengine_v1beta1.types.user_event import (
    PurchaseTransaction,
)
from google.cloud.recommendationengine_v1beta1.types.user_event import UserEvent
from google.cloud.recommendationengine_v1beta1.types.user_event import UserInfo
from google.cloud.recommendationengine_v1beta1.types.user_event_service import (
    CollectUserEventRequest,
)
from google.cloud.recommendationengine_v1beta1.types.user_event_service import (
    ListUserEventsRequest,
)
from google.cloud.recommendationengine_v1beta1.types.user_event_service import (
    ListUserEventsResponse,
)
from google.cloud.recommendationengine_v1beta1.types.user_event_service import (
    PurgeUserEventsMetadata,
)
from google.cloud.recommendationengine_v1beta1.types.user_event_service import (
    PurgeUserEventsRequest,
)
from google.cloud.recommendationengine_v1beta1.types.user_event_service import (
    PurgeUserEventsResponse,
)
from google.cloud.recommendationengine_v1beta1.types.user_event_service import (
    WriteUserEventRequest,
)

__all__ = (
    "CatalogServiceClient",
    "CatalogServiceAsyncClient",
    "PredictionApiKeyRegistryClient",
    "PredictionApiKeyRegistryAsyncClient",
    "PredictionServiceClient",
    "PredictionServiceAsyncClient",
    "UserEventServiceClient",
    "UserEventServiceAsyncClient",
    "CatalogItem",
    "Image",
    "ProductCatalogItem",
    "CreateCatalogItemRequest",
    "DeleteCatalogItemRequest",
    "GetCatalogItemRequest",
    "ListCatalogItemsRequest",
    "ListCatalogItemsResponse",
    "UpdateCatalogItemRequest",
    "FeatureMap",
    "CatalogInlineSource",
    "GcsSource",
    "ImportCatalogItemsRequest",
    "ImportCatalogItemsResponse",
    "ImportErrorsConfig",
    "ImportMetadata",
    "ImportUserEventsRequest",
    "ImportUserEventsResponse",
    "InputConfig",
    "UserEventImportSummary",
    "UserEventInlineSource",
    "CreatePredictionApiKeyRegistrationRequest",
    "DeletePredictionApiKeyRegistrationRequest",
    "ListPredictionApiKeyRegistrationsRequest",
    "ListPredictionApiKeyRegistrationsResponse",
    "PredictionApiKeyRegistration",
    "PredictRequest",
    "PredictResponse",
    "EventDetail",
    "ProductDetail",
    "ProductEventDetail",
    "PurchaseTransaction",
    "UserEvent",
    "UserInfo",
    "CollectUserEventRequest",
    "ListUserEventsRequest",
    "ListUserEventsResponse",
    "PurgeUserEventsMetadata",
    "PurgeUserEventsRequest",
    "PurgeUserEventsResponse",
    "WriteUserEventRequest",
)
