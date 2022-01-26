#---------------------------------------------------------------------------------------------------------------------
#  Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.                                           *
#                                                                                                                    *
#  Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance    *
#  with the License. A copy of the License is located at                                                             *
#                                                                                                                    *
#      http://www.apache.org/licenses/LICENSE-2.0                                                                    *
#                                                                                                                    *
#  or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES *
#  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions    *
#  and limitations under the License.                                                                                *
#---------------------------------------------------------------------------------------------------------------------
"""Validator for incoming filter api parameters"""

from marshmallow import Schema, fields

"""
{
   "filters":{
      "software":{
         "swVersion":""
      },
      "anomalies": ["OilTemp"],
      "troubleCodes": ["U1234"],
      "vehicle":{
         "vin":[],
         "make":[],
         "model":[],
         "year":[]
      },
      "boundaries":[
         [-115.384126, 35.912202, -114.947419, 36.265106]
      ]
   },
   "timestamp": "2020-05-10T03:55:54.125Z"
}
"""
# [left,bottom,right,top]


class VehicleFilterAPISchema(Schema):
    filters = fields.Nested("ChildFiltersSchema", required=True)
    timestamp = fields.Str()


class ChildFiltersSchema(Schema):
    software = fields.Dict(keys=fields.Str(), values=fields.Str(), required=True)
    anomalies = fields.List(fields.Str(), required=True)
    troubleCodes = fields.List(fields.Str(), required=True)
    vehicle = fields.Nested("ChildVehicleSchema", required=True)
    boundaries = fields.List(fields.List(fields.Float()), required=True)


class ChildVehicleSchema(Schema):
    vin = fields.List(fields.Str())
    make = fields.List(fields.Str())
    model = fields.List(fields.Str())
    year = fields.List(fields.Int())
