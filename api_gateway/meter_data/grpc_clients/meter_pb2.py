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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmeter.proto\x12\x05meter\"H\n\x0eReadingRequest\x12\x12\n\nstart_date\x18\x01 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x02 \x01(\t\x12\x10\n\x08meter_id\x18\x03 \x01(\x05\"\x83\x01\n\x10MeterDataPayload\x12\x14\n\x0cmeter_serial\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x03 \x01(\x05\x12\r\n\x05value\x18\x04 \x01(\x02\x12\x0e\n\x06source\x18\x05 \x01(\t\x12\x16\n\x0ereading_reason\x18\x06 \x01(\t\"<\n\x07Reading\x12\r\n\x05value\x18\x01 \x01(\x05\x12\x12\n\ncreated_at\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\"3\n\x0fReadingResponse\x12 \n\x08readings\x18\x01 \x03(\x0b\x32\x0e.meter.Reading\"#\n\x15ReadingCreateResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x32\x95\x01\n\x0cMeterService\x12<\n\x0bGetReadings\x12\x15.meter.ReadingRequest\x1a\x16.meter.ReadingResponse\x12G\n\x0e\x43reateReadings\x12\x17.meter.MeterDataPayload\x1a\x1c.meter.ReadingCreateResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_READINGREQUEST']._serialized_start=22
  _globals['_READINGREQUEST']._serialized_end=94
  _globals['_METERDATAPAYLOAD']._serialized_start=97
  _globals['_METERDATAPAYLOAD']._serialized_end=228
  _globals['_READING']._serialized_start=230
  _globals['_READING']._serialized_end=290
  _globals['_READINGRESPONSE']._serialized_start=292
  _globals['_READINGRESPONSE']._serialized_end=343
  _globals['_READINGCREATERESPONSE']._serialized_start=345
  _globals['_READINGCREATERESPONSE']._serialized_end=380
  _globals['_METERSERVICE']._serialized_start=383
  _globals['_METERSERVICE']._serialized_end=532
# @@protoc_insertion_point(module_scope)
