# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/presence_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bnet.entity_pb2
import bnet.presence_types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/presence_service.proto',
  package='bnet.protocol.presence',
  serialized_pb=_b('\n\x1b\x62net/presence_service.proto\x12\x16\x62net.protocol.presence\x1a\x11\x62net/entity.proto\x1a\x19\x62net/presence_types.proto\"\x90\x01\n\x10SubscribeRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\tentity_id\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x11\n\tobject_id\x18\x03 \x02(\x04\x12\x12\n\nprogram_id\x18\x04 \x03(\x07\"J\n\x1cSubscribeNotificationRequest\x12*\n\tentity_id\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.EntityId\"k\n\x12UnsubscribeRequest\x12)\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12*\n\tentity_id\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\"|\n\rUpdateRequest\x12*\n\tentity_id\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12?\n\x0f\x66ield_operation\x18\x02 \x03(\x0b\x32&.bnet.protocol.presence.FieldOperation\"i\n\x0cQueryRequest\x12*\n\tentity_id\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12-\n\x03key\x18\x02 \x03(\x0b\x32 .bnet.protocol.presence.FieldKey\"=\n\rQueryResponse\x12,\n\x05\x66ield\x18\x02 \x03(\x0b\x32\x1d.bnet.protocol.presence.Field\"`\n\x10OwnershipRequest\x12*\n\tentity_id\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12 \n\x11release_ownership\x18\x02 \x01(\x08:\x05\x66\x61lse')
  ,
  dependencies=[bnet.entity_pb2.DESCRIPTOR,bnet.presence_types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='bnet.protocol.presence.SubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.presence.SubscribeRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='bnet.protocol.presence.SubscribeRequest.entity_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='bnet.protocol.presence.SubscribeRequest.object_id', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='program_id', full_name='bnet.protocol.presence.SubscribeRequest.program_id', index=3,
      number=4, type=7, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=246,
)


_SUBSCRIBENOTIFICATIONREQUEST = _descriptor.Descriptor(
  name='SubscribeNotificationRequest',
  full_name='bnet.protocol.presence.SubscribeNotificationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='bnet.protocol.presence.SubscribeNotificationRequest.entity_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=322,
)


_UNSUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='UnsubscribeRequest',
  full_name='bnet.protocol.presence.UnsubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='bnet.protocol.presence.UnsubscribeRequest.agent_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='bnet.protocol.presence.UnsubscribeRequest.entity_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=431,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='bnet.protocol.presence.UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='bnet.protocol.presence.UpdateRequest.entity_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_operation', full_name='bnet.protocol.presence.UpdateRequest.field_operation', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=433,
  serialized_end=557,
)


_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='bnet.protocol.presence.QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='bnet.protocol.presence.QueryRequest.entity_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='bnet.protocol.presence.QueryRequest.key', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=664,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='bnet.protocol.presence.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='bnet.protocol.presence.QueryResponse.field', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=666,
  serialized_end=727,
)


_OWNERSHIPREQUEST = _descriptor.Descriptor(
  name='OwnershipRequest',
  full_name='bnet.protocol.presence.OwnershipRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='bnet.protocol.presence.OwnershipRequest.entity_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='release_ownership', full_name='bnet.protocol.presence.OwnershipRequest.release_ownership', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=825,
)

_SUBSCRIBEREQUEST.fields_by_name['agent_id'].message_type = bnet.entity_pb2._ENTITYID
_SUBSCRIBEREQUEST.fields_by_name['entity_id'].message_type = bnet.entity_pb2._ENTITYID
_SUBSCRIBENOTIFICATIONREQUEST.fields_by_name['entity_id'].message_type = bnet.entity_pb2._ENTITYID
_UNSUBSCRIBEREQUEST.fields_by_name['agent_id'].message_type = bnet.entity_pb2._ENTITYID
_UNSUBSCRIBEREQUEST.fields_by_name['entity_id'].message_type = bnet.entity_pb2._ENTITYID
_UPDATEREQUEST.fields_by_name['entity_id'].message_type = bnet.entity_pb2._ENTITYID
_UPDATEREQUEST.fields_by_name['field_operation'].message_type = bnet.presence_types_pb2._FIELDOPERATION
_QUERYREQUEST.fields_by_name['entity_id'].message_type = bnet.entity_pb2._ENTITYID
_QUERYREQUEST.fields_by_name['key'].message_type = bnet.presence_types_pb2._FIELDKEY
_QUERYRESPONSE.fields_by_name['field'].message_type = bnet.presence_types_pb2._FIELD
_OWNERSHIPREQUEST.fields_by_name['entity_id'].message_type = bnet.entity_pb2._ENTITYID
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['SubscribeNotificationRequest'] = _SUBSCRIBENOTIFICATIONREQUEST
DESCRIPTOR.message_types_by_name['UnsubscribeRequest'] = _UNSUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['OwnershipRequest'] = _OWNERSHIPREQUEST

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBEREQUEST,
  __module__ = 'bnet.presence_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.presence.SubscribeRequest)
  ))
_sym_db.RegisterMessage(SubscribeRequest)

SubscribeNotificationRequest = _reflection.GeneratedProtocolMessageType('SubscribeNotificationRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBENOTIFICATIONREQUEST,
  __module__ = 'bnet.presence_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.presence.SubscribeNotificationRequest)
  ))
_sym_db.RegisterMessage(SubscribeNotificationRequest)

UnsubscribeRequest = _reflection.GeneratedProtocolMessageType('UnsubscribeRequest', (_message.Message,), dict(
  DESCRIPTOR = _UNSUBSCRIBEREQUEST,
  __module__ = 'bnet.presence_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.presence.UnsubscribeRequest)
  ))
_sym_db.RegisterMessage(UnsubscribeRequest)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREQUEST,
  __module__ = 'bnet.presence_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.presence.UpdateRequest)
  ))
_sym_db.RegisterMessage(UpdateRequest)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYREQUEST,
  __module__ = 'bnet.presence_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.presence.QueryRequest)
  ))
_sym_db.RegisterMessage(QueryRequest)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYRESPONSE,
  __module__ = 'bnet.presence_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.presence.QueryResponse)
  ))
_sym_db.RegisterMessage(QueryResponse)

OwnershipRequest = _reflection.GeneratedProtocolMessageType('OwnershipRequest', (_message.Message,), dict(
  DESCRIPTOR = _OWNERSHIPREQUEST,
  __module__ = 'bnet.presence_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.presence.OwnershipRequest)
  ))
_sym_db.RegisterMessage(OwnershipRequest)


# @@protoc_insertion_point(module_scope)
