# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meter.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmeter.proto\x12\x05meter\"H\n\x0eReadingRequest\x12\x12\n\nstart_date\x18\x01 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x02 \x01(\t\x12\x10\n\x08meter_id\x18\x03 \x01(\x05\"<\n\x07Reading\x12\r\n\x05value\x18\x01 \x01(\x05\x12\x12\n\ncreated_at\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\"3\n\x0fReadingResponse\x12 \n\x08readings\x18\x01 \x03(\x0b\x32\x0e.meter.Reading\"#\n\x15ReadingCreateResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x32\x93\x01\n\x0cMeterService\x12<\n\x0bGetReadings\x12\x15.meter.ReadingRequest\x1a\x16.meter.ReadingResponse\x12\x45\n\x0e\x43reateReadings\x12\x15.meter.ReadingRequest\x1a\x1c.meter.ReadingCreateResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_READINGREQUEST']._serialized_start=22
  _globals['_READINGREQUEST']._serialized_end=94
  _globals['_READING']._serialized_start=96
  _globals['_READING']._serialized_end=156
  _globals['_READINGRESPONSE']._serialized_start=158
  _globals['_READINGRESPONSE']._serialized_end=209
  _globals['_READINGCREATERESPONSE']._serialized_start=211
  _globals['_READINGCREATERESPONSE']._serialized_end=246
  _globals['_METERSERVICE']._serialized_start=249
  _globals['_METERSERVICE']._serialized_end=396
# @@protoc_insertion_point(module_scope)
