#!/usr/bin/env python
# encoding:utf-8

class EnumErrorCode():
    S_OK = 0x00000000
    E_Database_Error = 0x10000000
    E_Database_Multi_Result = 0x10000001
    E_Database_No_Result = 0x10000002
    E_Update_Error = 0x20000000
    E_Validate_Fail = 0x30000000
    E_Validate_His_Fail = 0x30000001
    E_INVALID_ARG = 0x40000000
    E_Warehouse_No_Result = 0x50000000