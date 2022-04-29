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
    admin = 'admin'  # 管理员
    tenant = 'tenant'  # 租客
    landlord = 'landlord'  # 房东
    steward = 'steward'  # 管家


class UserState(StrEnum):
    """用户状态"""
    normal = 'normal'
    deleted = 'deleted'


class UserAuthStatus(StrEnum):
    """用户实名认证状态"""
    unauthorized = 'unauthorized'  # 未实名认证
    authorized = 'authorized'  # 已实名认证
    auditing = 'auditing'  # 审核中
    unapprove = 'unapprove'  # 审核未通过


class RentType(StrEnum):
    """出租类型"""
    whole = 'whole'  # 整租
    share = 'share'  # 合租


class RentState(StrEnum):
    """出租状态"""
    rent = 'rent'  # 已出租
    not_rent = 'not_rent'  # 未出租


class OrderState(StrEnum):
    """订单状态"""
    no_pay = 'no_pay'  # 未支付
    payed = 'payed'  # 已支付
    canceled = 'canceled'  # 已取消
    deleted = 'deleted'  # 已删除


class RentTimeUnitEnum(StrEnum):
    """ 租赁时间单位枚举 """
    day = 'day'  # 日结
    month = 'month'  # 月结
    quarter = 'quarter'  # 季度结
    half_year = 'half_year'  # 半年结
    year = 'year'  # 年结


class HouseDirectionEnum(StrEnum):
    """房屋朝向"""
    north = 'north'
    south = 'south'
    east = 'east'
    west = 'west'


class HouseElevatorEnum(IntEnum):
    """ 房屋电梯情况 """
    no = 0  # 没有
    yes = 1  # 有


class HouseLightingEnum(IntEnum):
    """ 房屋采光情况 """
    bad = 0  # 差
    general = 1  # 一般
    normal = 2  # 正常
    good = 3  # 良好
    excellent = 4  # 极好


class HouseType(StrEnum):
    """房屋类型"""
    department = 'department'  # 公寓
    community = 'community'  # 小区
    residential = 'residential'  # 普通住宅


class HouseState(StrEnum):
    """ 房屋状态 """
    up = 'up'  # 已上架
    down = 'down'  # 已下架
    auditing = 'auditing'  # 审核中状态
    deleted = 'deleted'  # 已删除


class RedisDataType(StrEnum):
    """ Redis 数据类型 """
    STRING = 'STRING'
    LIST = 'LIST'
    HASH = 'HASH'
    SET = 'SET'
    ZSET = 'ZSET'


class RequestMethodEnum(StrEnum):
    """ 请求方法枚举 """
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
