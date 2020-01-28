"""Generated message classes for cloudidentity version v1alpha1.

API for provisioning and managing identity resources.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'cloudidentity'


class CloudidentityGroupsCreateRequest(_messages.Message):
  r"""A CloudidentityGroupsCreateRequest object.

  Enums:
    InitialGroupConfigValueValuesEnum: Required. The initial configuration
      option for the `Group`.

  Fields:
    group: A Group resource to be passed as the request body.
    initialGroupConfig: Required. The initial configuration option for the
      `Group`.
  """

  class InitialGroupConfigValueValuesEnum(_messages.Enum):
    r"""Required. The initial configuration option for the `Group`.

    Values:
      INITIAL_GROUP_CONFIG_UNSPECIFIED: <no description>
      WITH_INITIAL_OWNER: <no description>
    """
    INITIAL_GROUP_CONFIG_UNSPECIFIED = 0
    WITH_INITIAL_OWNER = 1

  group = _messages.MessageField('Group', 1)
  initialGroupConfig = _messages.EnumField('InitialGroupConfigValueValuesEnum', 2)


class CloudidentityGroupsDeleteRequest(_messages.Message):
  r"""A CloudidentityGroupsDeleteRequest object.

  Fields:
    name: Required. The [resource
      name](https://cloud.google.com/apis/design/resource_names) of the
      `Group` to retrieve.  Must be of the form `groups/{group_id}`.
  """

  name = _messages.StringField(1, required=True)


class CloudidentityGroupsGetRequest(_messages.Message):
  r"""A CloudidentityGroupsGetRequest object.

  Fields:
    name: Required. The [resource
      name](https://cloud.google.com/apis/design/resource_names) of the
      `Group` to retrieve.  Must be of the form `groups/{group_id}`.
  """

  name = _messages.StringField(1, required=True)


class CloudidentityGroupsListRequest(_messages.Message):
  r"""A CloudidentityGroupsListRequest object.

  Enums:
    ViewValueValuesEnum: The level of detail to be returned.  If unspecified,
      defaults to `View.BASIC`.

  Fields:
    pageSize: The maximum number of results to return.  Note that the number
      of results returned may be less than this value even if there are more
      available results. To fetch all results, clients must continue calling
      this method repeatedly until the response no longer contains a
      `next_page_token`.  If unspecified, defaults to 200 for `View.BASIC` and
      to 50 for `View.FULL`.  Must not be greater than 1000 for `View.BASIC`
      or 500 for `View.FULL`.
    pageToken: The `next_page_token` value returned from a previous list
      request, if any.
    parent: Required. The parent resource under which to list all `Group`s.
      Must be of the form `identitysources/{identity_source_id}` for external-
      identity-mapped groups or `customers/{customer_id}` for Google Groups.
    view: The level of detail to be returned.  If unspecified, defaults to
      `View.BASIC`.
  """

  class ViewValueValuesEnum(_messages.Enum):
    r"""The level of detail to be returned.  If unspecified, defaults to
    `View.BASIC`.

    Values:
      VIEW_UNSPECIFIED: <no description>
      BASIC: <no description>
      FULL: <no description>
    """
    VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3)
  view = _messages.EnumField('ViewValueValuesEnum', 4)


class CloudidentityGroupsLookupRequest(_messages.Message):
  r"""A CloudidentityGroupsLookupRequest object.

  Fields:
    groupKey_id: Required. The ID of the entity.  For Google-managed entities,
      the `id` must be the email address of a group or user.  For external-
      identity-mapped entities, the `id` must be a string conforming to the
      Identity Source's requirements.  Must be unique within a `namespace`.
    groupKey_namespace: The namespace in which the entity exists.  If not
      specified, the `EntityKey` represents a Google-managed entity such as a
      Google user or a Google Group.  If specified, the `EntityKey` represents
      an external-identity-mapped group created through Admin Console. Must be
      of the form `identitysources/{identity_source_id}.
  """

  groupKey_id = _messages.StringField(1)
  groupKey_namespace = _messages.StringField(2)


class CloudidentityGroupsMembershipsCreateRequest(_messages.Message):
  r"""A CloudidentityGroupsMembershipsCreateRequest object.

  Fields:
    membership: A Membership resource to be passed as the request body.
    parent: Required. The parent `Group` resource under which to create the
      `Membership`.  Must be of the form `groups/{group_id}`.
  """

  membership = _messages.MessageField('Membership', 1)
  parent = _messages.StringField(2, required=True)


class CloudidentityGroupsMembershipsDeleteRequest(_messages.Message):
  r"""A CloudidentityGroupsMembershipsDeleteRequest object.

  Fields:
    name: Required. The [resource
      name](https://cloud.google.com/apis/design/resource_names) of the
      `Membership` to delete.  Must be of the form
      `groups/{group_id}/memberships/{membership_id}`.
  """

  name = _messages.StringField(1, required=True)


class CloudidentityGroupsMembershipsGetRequest(_messages.Message):
  r"""A CloudidentityGroupsMembershipsGetRequest object.

  Fields:
    name: Required. The [resource
      name](https://cloud.google.com/apis/design/resource_names) of the
      `Membership` to retrieve.  Must be of the form
      `groups/{group_id}/memberships/{membership_id}`.
  """

  name = _messages.StringField(1, required=True)


class CloudidentityGroupsMembershipsListRequest(_messages.Message):
  r"""A CloudidentityGroupsMembershipsListRequest object.

  Enums:
    ViewValueValuesEnum: The level of detail to be returned.  If unspecified,
      defaults to `View.BASIC`.

  Fields:
    pageSize: The maximum number of results to return.  Note that the number
      of results returned may be less than this value even if there are more
      available results. To fetch all results, clients must continue calling
      this method repeatedly until the response no longer contains a
      `next_page_token`.  If unspecified, defaults to 200 for `View.BASIC` and
      to 50 for `View.FULL`.  Must not be greater than 1000 for `View.BASIC`
      or 500 for `View.FULL`.
    pageToken: The `next_page_token` value returned from a previous list
      request, if any.
    parent: Required. The parent `Group` resource under which to lookup the
      `Membership` name.  Must be of the form `groups/{group_id}`.
    view: The level of detail to be returned.  If unspecified, defaults to
      `View.BASIC`.
  """

  class ViewValueValuesEnum(_messages.Enum):
    r"""The level of detail to be returned.  If unspecified, defaults to
    `View.BASIC`.

    Values:
      VIEW_UNSPECIFIED: <no description>
      BASIC: <no description>
      FULL: <no description>
    """
    VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)
  view = _messages.EnumField('ViewValueValuesEnum', 4)


class CloudidentityGroupsMembershipsLookupRequest(_messages.Message):
  r"""A CloudidentityGroupsMembershipsLookupRequest object.

  Fields:
    memberKey_id: Required. The ID of the entity.  For Google-managed
      entities, the `id` must be the email address of a group or user.  For
      external-identity-mapped entities, the `id` must be a string conforming
      to the Identity Source's requirements.  Must be unique within a
      `namespace`.
    memberKey_namespace: The namespace in which the entity exists.  If not
      specified, the `EntityKey` represents a Google-managed entity such as a
      Google user or a Google Group.  If specified, the `EntityKey` represents
      an external-identity-mapped group created through Admin Console. Must be
      of the form `identitysources/{identity_source_id}.
    parent: Required. The parent `Group` resource under which to lookup the
      `Membership` name.  Must be of the form `groups/{group_id}`.
  """

  memberKey_id = _messages.StringField(1)
  memberKey_namespace = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class CloudidentityGroupsMembershipsModifyMembershipRolesRequest(_messages.Message):
  r"""A CloudidentityGroupsMembershipsModifyMembershipRolesRequest object.

  Fields:
    modifyMembershipRolesRequest: A ModifyMembershipRolesRequest resource to
      be passed as the request body.
    name: The [resource
      name](https://cloud.google.com/apis/design/resource_names) of the
      `Membership` whose roles are to be modified.  Must be of the form
      `groups/{group_id}/memberships/{membership_id}`.
  """

  modifyMembershipRolesRequest = _messages.MessageField('ModifyMembershipRolesRequest', 1)
  name = _messages.StringField(2, required=True)


class CloudidentityGroupsMembershipsPatchRequest(_messages.Message):
  r"""A CloudidentityGroupsMembershipsPatchRequest object.

  Fields:
    membership: A Membership resource to be passed as the request body.
    name: Output only. The [resource
      name](https://cloud.google.com/apis/design/resource_names) of the
      `Membership`.  Shall be of the form
      `groups/{group_id}/memberships/{membership_id}`.
    updateMask: The fully-qualified names of fields to update.
  """

  membership = _messages.MessageField('Membership', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class CloudidentityGroupsPatchRequest(_messages.Message):
  r"""A CloudidentityGroupsPatchRequest object.

  Fields:
    group: A Group resource to be passed as the request body.
    name: Output only. The [resource
      name](https://cloud.google.com/apis/design/resource_names) of the
      `Group`.  Shall be of the form `groups/{group_id}`.
    updateMask: Required. The fully-qualified names of fields to update.  May
      only contain the following fields: `display_name`, `description`.
  """

  group = _messages.MessageField('Group', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class CloudidentityGroupsSearchRequest(_messages.Message):
  r"""A CloudidentityGroupsSearchRequest object.

  Enums:
    ViewValueValuesEnum: The level of detail to be returned.  If unspecified,
      defaults to `View.BASIC`.

  Fields:
    pageSize: The maximum number of results to return.  Note that the number
      of results returned may be less than this value even if there are more
      available results. To fetch all results, clients must continue calling
      this method repeatedly until the response no longer contains a
      `next_page_token`.  If unspecified, defaults to 200 for `View.BASIC` and
      to 50 for `View.FULL`.  Must not be greater than 1000 for `View.BASIC`
      or 500 for `View.FULL`.
    pageToken: The `next_page_token` value returned from a previous search
      request, if any.
    query: Required. The search query.  Only queries on the parent and labels
      of `Group`s are supported.  Must be specified in [Common Expression
      Language](https://opensource.google/projects/cel). May only contain
      equality operators on the parent (e.g. `parent ==
      'customers/{customer_id}'`) and inclusion operators on labels (e.g.,
      `'cloudidentity.googleapis.com/groups.discussion_forum' in labels`).
    view: The level of detail to be returned.  If unspecified, defaults to
      `View.BASIC`.
  """

  class ViewValueValuesEnum(_messages.Enum):
    r"""The level of detail to be returned.  If unspecified, defaults to
    `View.BASIC`.

    Values:
      VIEW_UNSPECIFIED: <no description>
      BASIC: <no description>
      FULL: <no description>
    """
    VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  query = _messages.StringField(3)
  view = _messages.EnumField('ViewValueValuesEnum', 4)


class DynamicGroupMetadata(_messages.Message):
  r"""Dynamic group metadata like queries and status.

  Fields:
    queries: Only one entry is supported for now. Memberships will be the
      union of all queries.
    status: Status of the dynamic group. Output only.
  """

  queries = _messages.MessageField('DynamicGroupQuery', 1, repeated=True)
  status = _messages.MessageField('DynamicGroupStatus', 2)


class DynamicGroupQuery(_messages.Message):
  r"""Defines a query on a resource.

  Enums:
    ResourceTypeValueValuesEnum:

  Fields:
    query: Query that determines the memberships of the dynamic group.
    resourceType: A ResourceTypeValueValuesEnum attribute.
  """

  class ResourceTypeValueValuesEnum(_messages.Enum):
    r"""ResourceTypeValueValuesEnum enum type.

    Values:
      RESOURCE_TYPE_UNSPECIFIED: <no description>
      USER: <no description>
    """
    RESOURCE_TYPE_UNSPECIFIED = 0
    USER = 1

  query = _messages.StringField(1)
  resourceType = _messages.EnumField('ResourceTypeValueValuesEnum', 2)


class DynamicGroupStatus(_messages.Message):
  r"""The current status of a dynamic group along with timestamp.

  Enums:
    StatusValueValuesEnum: Status of the dynamic group.

  Fields:
    status: Status of the dynamic group.
    statusTime: The latest time at which the dynamic group is guaranteed to be
      in the given status. For example, if status is: UP_TO_DATE - The latest
      time at which this dynamic group was confirmed to be up to date.
      UPDATING_MEMBERSHIPS - The time at which dynamic group was created.
  """

  class StatusValueValuesEnum(_messages.Enum):
    r"""Status of the dynamic group.

    Values:
      STATUS_UNSPECIFIED: Default.
      UP_TO_DATE: The dynamic group is up-to-date.
      UPDATING_MEMBERSHIPS: The dynamic group has just been created and
        memberships are being updated.
    """
    STATUS_UNSPECIFIED = 0
    UP_TO_DATE = 1
    UPDATING_MEMBERSHIPS = 2

  status = _messages.EnumField('StatusValueValuesEnum', 1)
  statusTime = _messages.StringField(2)


class EntityKey(_messages.Message):
  r"""A unique identifier for an entity in the Cloud Identity Groups API.  An
  entity can represent either a group with an optional `namespace` or a user
  without a `namespace`. The combination of `id` and `namespace` must be
  unique; however, the same `id` can be used with different `namespace`s.

  Fields:
    id: Required. The ID of the entity.  For Google-managed entities, the `id`
      must be the email address of a group or user.  For external-identity-
      mapped entities, the `id` must be a string conforming to the Identity
      Source's requirements.  Must be unique within a `namespace`.
    namespace: The namespace in which the entity exists.  If not specified,
      the `EntityKey` represents a Google-managed entity such as a Google user
      or a Google Group.  If specified, the `EntityKey` represents an
      external-identity-mapped group created through Admin Console. Must be of
      the form `identitysources/{identity_source_id}.
  """

  id = _messages.StringField(1)
  namespace = _messages.StringField(2)


class ExpiryDetail(_messages.Message):
  r"""Specifies Membership expiry attributes.

  Fields:
    expireTime: Expiration time for the Membership.
  """

  expireTime = _messages.StringField(1)


class Group(_messages.Message):
  r"""A group within the Cloud Identity Groups API.  A `Group` is a collection
  of entities, where each entity is either a user or another group.

  Messages:
    LabelsValue: Required. The labels that apply to the `Group`.  Must not
      contain more than one entry. Must contain the entry
      `'system/groups/external': ''` if the `Group` is an external-identity-
      mapped group or `'cloudidentity.googleapis.com/groups.discussion_forum':
      ''` if the `Group` is a Google Group.

  Fields:
    createTime: Output only. The time when the `Group` was created.
    description: An extended description to help users determine the purpose
      of a `Group`.  Must not be longer than 4,096 characters.
    displayName: The display name of the `Group`.
    dynamicGroupMetadata: Dynamic group metadata like queries and status.
    groupKey: Required. Immutable. The `EntityKey` of the `Group`.
    labels: Required. The labels that apply to the `Group`.  Must not contain
      more than one entry. Must contain the entry `'system/groups/external':
      ''` if the `Group` is an external-identity-mapped group or
      `'cloudidentity.googleapis.com/groups.discussion_forum': ''` if the
      `Group` is a Google Group.
    name: Output only. The [resource
      name](https://cloud.google.com/apis/design/resource_names) of the
      `Group`.  Shall be of the form `groups/{group_id}`.
    parent: Required. Immutable. The resource name of the entity under which
      this `Group` resides in the Cloud Identity resource hierarchy.  Must be
      of the form `identitysources/{identity_source_id}` for external-
      identity-mapped groups or `customers/{customer_id}` for Google Groups.
    updateTime: Output only. The time when the `Group` was last updated.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Required. The labels that apply to the `Group`.  Must not contain more
    than one entry. Must contain the entry `'system/groups/external': ''` if
    the `Group` is an external-identity-mapped group or
    `'cloudidentity.googleapis.com/groups.discussion_forum': ''` if the
    `Group` is a Google Group.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  createTime = _messages.StringField(1)
  description = _messages.StringField(2)
  displayName = _messages.StringField(3)
  dynamicGroupMetadata = _messages.MessageField('DynamicGroupMetadata', 4)
  groupKey = _messages.MessageField('EntityKey', 5)
  labels = _messages.MessageField('LabelsValue', 6)
  name = _messages.StringField(7)
  parent = _messages.StringField(8)
  updateTime = _messages.StringField(9)


class ListGroupsResponse(_messages.Message):
  r"""The response message for GroupsService.ListGroups.

  Fields:
    groups: The `Group`s under the specified `parent`.
    nextPageToken: A continuation token to retrieve the next page of results,
      or empty if there are no more results available.
  """

  groups = _messages.MessageField('Group', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListMembershipsResponse(_messages.Message):
  r"""The response message for MembershipsService.ListMemberships.

  Fields:
    memberships: The `Membership`s under the specified `parent`.
    nextPageToken: A continuation token to retrieve the next page of results,
      or empty if there are no more results available.
  """

  memberships = _messages.MessageField('Membership', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class LookupGroupNameResponse(_messages.Message):
  r"""The response message for GroupsService.LookupGroupName.

  Fields:
    name: Output only. The [resource
      name](https://cloud.google.com/apis/design/resource_names) of the
      looked-up `Group`.
  """

  name = _messages.StringField(1)


class LookupMembershipNameResponse(_messages.Message):
  r"""The response message for MembershipsService.LookupMembershipName.

  Fields:
    name: The [resource
      name](https://cloud.google.com/apis/design/resource_names) of the
      looked-up `Membership`.  Must be of the form
      `groups/{group_id}/memberships/{membership_id}`.
  """

  name = _messages.StringField(1)


class Membership(_messages.Message):
  r"""A membership within the Cloud Identity Groups API.  A `Membership`
  defines a relationship between a `Group` and an entity belonging to that
  `Group`, referred to as a "member".

  Enums:
    TypeValueValuesEnum: Output only. The type of the membership.

  Fields:
    createTime: Output only. The time when the `Membership` was created.
    expiryDetail: The expiry details of the `MembershipRole`.  May be set if
      the only `MembershipRole` is one with `name` `MEMBER`. Must not be set
      if any other `MembershipRole`s exist.
    name: Output only. The [resource
      name](https://cloud.google.com/apis/design/resource_names) of the
      `Membership`.  Shall be of the form
      `groups/{group_id}/memberships/{membership_id}`.
    preferredMemberKey: Required. Immutable. The `EntityKey` of the member.
    roles: The `MembershipRole`s that apply to the `Membership`.  If
      unspecified, defaults to a single `MembershipRole` with `name` `MEMBER`
      and no `expiry_detail`.  Must not contain duplicate `MembershipRole`s
      with the same `name`.
    type: Output only. The type of the membership.
    updateTime: Output only. The time when the `Membership` was last updated.
  """

  class TypeValueValuesEnum(_messages.Enum):
    r"""Output only. The type of the membership.

    Values:
      TYPE_UNSPECIFIED: Default. Should not be used.
      USER: Represents user type.
      SERVICE_ACCOUNT: Represents service account type.
      GROUP: Represents group type.
      OTHER: Represents other type.
    """
    TYPE_UNSPECIFIED = 0
    USER = 1
    SERVICE_ACCOUNT = 2
    GROUP = 3
    OTHER = 4

  createTime = _messages.StringField(1)
  expiryDetail = _messages.MessageField('ExpiryDetail', 2)
  name = _messages.StringField(3)
  preferredMemberKey = _messages.MessageField('EntityKey', 4)
  roles = _messages.MessageField('MembershipRole', 5, repeated=True)
  type = _messages.EnumField('TypeValueValuesEnum', 6)
  updateTime = _messages.StringField(7)


class MembershipRole(_messages.Message):
  r"""A membership role within the Cloud Identity Groups API.  A
  `MembershipRole` defines the privileges granted to a `Membership`.

  Fields:
    expiryDetail: The expiry details of the `MembershipRole`.  Expiry details
      are only supported for `MEMBER` `MembershipRoles`.  May be set if `name`
      is `MEMBER`. Must not be set if `name` is any other value.
    name: Required. Immutable. The name of the `MembershipRole`.  Must be one
      of `OWNER`, `MANAGER`, `MEMBER`.
  """

  expiryDetail = _messages.MessageField('MembershipRoleExpiryDetail', 1)
  name = _messages.StringField(2)


class MembershipRoleExpiryDetail(_messages.Message):
  r"""The `MembershipRole` expiry details.

  Fields:
    expireTime: The time at which the `MembershipRole` will expire.
  """

  expireTime = _messages.StringField(1)


class ModifyMembershipRolesRequest(_messages.Message):
  r"""The request message for MembershipsService.ModifyMembershipRoles.

  Fields:
    addRoles: The `MembershipRole`s to be added.  Adding or removing roles in
      the same request as updating roles is not supported.  Must not be set if
      `update_roles_params` is set.
    removeRoles: The `name`s of the `MembershipRole`s to be removed.  Adding
      or removing roles in the same request as updating roles is not
      supported.  It is not possible to remove the `MEMBER` `MembershipRole`.
      If you wish to delete a `Membership`, call
      MembershipsService.DeleteMembership instead.  Must not contain `MEMBER`.
      Must not be set if `update_roles_params` is set.
    updateRolesParams: The `MembershipRole`s to be updated.  Updating roles in
      the same request as adding or removing roles is not supported.  Must not
      be set if either `add_roles` or `remove_roles` is set.
  """

  addRoles = _messages.MessageField('MembershipRole', 1, repeated=True)
  removeRoles = _messages.StringField(2, repeated=True)
  updateRolesParams = _messages.MessageField('UpdateMembershipRolesParams', 3, repeated=True)


class ModifyMembershipRolesResponse(_messages.Message):
  r"""The response message for MembershipsService.ModifyMembershipRoles.

  Fields:
    membership: The `Membership` resource after modifying its
      `MembershipRole`s.
  """

  membership = _messages.MessageField('Membership', 1)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class SearchGroupsResponse(_messages.Message):
  r"""The response message for GroupsService.SearchGroups.

  Fields:
    groups: The `Group`s that match the search query.
    nextPageToken: A continuation token to retrieve the next page of results,
      or empty if there are no more results available.
  """

  groups = _messages.MessageField('Group', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details.  You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class UpdateMembershipRolesParams(_messages.Message):
  r"""The details of an update to a `MembershipRole`.

  Fields:
    fieldMask: The fully-qualified names of fields to update.  May only
      contain the field `expiry_detail`.
    membershipRole: The `MembershipRole`s to be updated.  Only `MEMBER`
      `MembershipRoles` can currently be updated.  May only contain a
      `MembershipRole` with `name` `MEMBER`.
  """

  fieldMask = _messages.StringField(1)
  membershipRole = _messages.MessageField('MembershipRole', 2)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
