#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 项目枚举模块 }
# @Date: 2022/03/06 18:21
from enum import Enum


class BaseEnum(Enum):
    """枚举基类"""

    @classmethod
    def get_member_values(cls):
        return [item.value for item in cls._member_map_.values()]

    @classmethod
    def get_member_names(cls):
        return [name for name in cls._member_names_]


class StrEnum(str, BaseEnum):
    """字符串枚举"""
    pass


class IntEnum(int, BaseEnum):
    """整型枚举"""
    pass


class UserRole(StrEnum):
    """用户角色"""
    admin = 'admin'         # 管理员
    tenant = 'tenant'       # 租客
    landlord = 'landlord'   # 房东
    steward = 'steward'     # 管家


class UserState(StrEnum):
    """用户状态"""
    normal = 'normal'
    deleted = 'deleted'


class RentType(StrEnum):
    """出租类型"""
    normal = 'normal'
    deleted = 'deleted'


class RentState(StrEnum):
    """出租状态"""
    normal = 'normal'
    deleted = 'deleted'


class HouseDirection(StrEnum):
    """房屋朝向"""
    north = 'north'
    south = 'south'
    east = 'east'
    west = 'west'


class HouseType(StrEnum):
    """房屋类型"""
    housing_development = 'housing_development_test'
    department = 'department'


class RedisDataType(StrEnum):
    """ Redis 数据类型 """
    STRING = 'STRING'
    LIST = 'LIST'
    HASH = 'HASH'
    SET = 'SET'
    ZSET = 'ZSET'

