# -*- coding: utf-8 -*-
"""
OpenNebula Driver for Linstor
Copyright 2018 LINBIT USA LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import json

from linstor_helper import resource

NODE_DATA = """
[
  {
    "resource_states": [
      {
        "vlm_states": [
          {
            "disk_state": "UpToDate",
            "vlm_nr": 0
          }
        ],
        "in_use": false,
        "rsc_name": "bill",
        "node_name": "boudicca"
      },
      {
        "vlm_states": [
          {
            "disk_state": "UpToDate",
            "vlm_nr": 0
          }
        ],
        "in_use": false,
        "rsc_name": "bill2000",
        "node_name": "boudicca"
      },
      {
        "vlm_states": [
          {
            "disk_state": "UpToDate",
            "vlm_nr": 0
          }
        ],
        "in_use": false,
        "rsc_name": "bill",
        "node_name": "charlemagne"
      },
      {
        "vlm_states": [
          {
            "disk_state": "UpToDate",
            "vlm_nr": 0
          }
        ],
        "in_use": false,
        "rsc_name": "bill2000",
        "node_name": "charlemagne"
      },
      {
        "vlm_states": [
          {
            "disk_state": "UpToDate",
            "vlm_nr": 0
          }
        ],
        "in_use": false,
        "rsc_name": "bill",
        "node_name": "attila"
      },
      {
        "vlm_states": [
          {
            "disk_state": "UpToDate",
            "vlm_nr": 0
          }
        ],
        "in_use": false,
        "rsc_name": "bill2000",
        "node_name": "attila"
      }
    ],
    "resources": [
      {
        "vlms": [
          {
            "meta_disk": "internal",
            "device_path": "/dev/drbd1000",
            "vlm_nr": 0,
            "stor_pool_name": "thin",
            "stor_pool_uuid": "193bd06a-1267-4478-ac23-85f75290f14b",
            "vlm_minor_nr": 1000,
            "backing_disk": "/dev/drbdpool/bill_00000",
            "vlm_uuid": "c3887fc4-d208-4d33-b021-8d92d50dece2",
            "vlm_dfn_uuid": "dbb7c487-cc96-4fb0-ab55-91b32346322a"
          }
        ],
        "node_uuid": "9198fcab-2ed6-4039-8385-2e25cfd2aa35",
        "uuid": "17d39ccc-3995-4345-a52e-9f209cdde2dd",
        "node_name": "attila",
        "props": [
          {
            "value": "thin",
            "key": "AutoSelectedStorPoolName"
          },
          {
            "value": "7",
            "key": "PeerSlots"
          },
          {
            "value": "thin",
            "key": "StorPoolName"
          }
        ],
        "rsc_dfn_uuid": "9c298a4b-a2ae-4855-a931-08fa4826f3ed",
        "name": "bill"
      },
      {
        "vlms": [
          {
            "meta_disk": "internal",
            "device_path": "/dev/drbd1000",
            "vlm_nr": 0,
            "stor_pool_name": "thin",
            "stor_pool_uuid": "921af4e0-ff6d-43d6-b56a-a3f8cd45678f",
            "vlm_minor_nr": 1000,
            "backing_disk": "/dev/drbdpool/bill_00000",
            "vlm_uuid": "f58c12f4-79d2-4b10-9818-1716c178cb51",
            "vlm_dfn_uuid": "dbb7c487-cc96-4fb0-ab55-91b32346322a"
          }
        ],
        "node_uuid": "10f01093-2516-4d30-bc8d-a7b1ab5e72b2",
        "uuid": "c56356e4-f35f-4706-933b-cba9cf8baf5e",
        "node_name": "boudicca",
        "props": [
          {
            "value": "thin",
            "key": "AutoSelectedStorPoolName"
          },
          {
            "value": "7",
            "key": "PeerSlots"
          },
          {
            "value": "thin",
            "key": "StorPoolName"
          }
        ],
        "rsc_dfn_uuid": "9c298a4b-a2ae-4855-a931-08fa4826f3ed",
        "name": "bill"
      },
      {
        "vlms": [
          {
            "meta_disk": "internal",
            "device_path": "/dev/drbd1000",
            "vlm_nr": 0,
            "stor_pool_name": "thin",
            "stor_pool_uuid": "254472cf-fad9-4d0b-a57b-f783c40ac179",
            "vlm_minor_nr": 1000,
            "backing_disk": "/dev/drbdpool/bill_00000",
            "vlm_uuid": "eaa32672-18ee-4737-8e6b-7d3c55744f8b",
            "vlm_dfn_uuid": "dbb7c487-cc96-4fb0-ab55-91b32346322a"
          }
        ],
        "node_uuid": "172da4c8-250a-468f-bc0c-f4a4fd5d8d04",
        "uuid": "f6c4b45c-6e5f-41f2-ae1a-843305b52ee9",
        "node_name": "charlemagne",
        "props": [
          {
            "value": "thin",
            "key": "AutoSelectedStorPoolName"
          },
          {
            "value": "7",
            "key": "PeerSlots"
          },
          {
            "value": "thin",
            "key": "StorPoolName"
          }
        ],
        "rsc_dfn_uuid": "9c298a4b-a2ae-4855-a931-08fa4826f3ed",
        "name": "bill"
      },
      {
        "vlms": [
          {
            "meta_disk": "internal",
            "device_path": "/dev/drbd1003",
            "vlm_nr": 0,
            "stor_pool_name": "thin",
            "stor_pool_uuid": "193bd06a-1267-4478-ac23-85f75290f14b",
            "vlm_minor_nr": 1003,
            "backing_disk": "/dev/drbdpool/bill2000_00000",
            "vlm_uuid": "c5bd9741-2e57-49c5-9d74-536f1072002d",
            "vlm_props": [
              {
                "value": "bill",
                "key": "RestoreFromResource"
              },
              {
                "value": "bill-snap",
                "key": "RestoreFromSnapshot"
              },
              {
                "value": "thin",
                "key": "StorPoolName"
              }
            ],
            "vlm_dfn_uuid": "8bc9bba2-10c5-4a25-9dd1-07c977f089ce"
          }
        ],
        "node_uuid": "9198fcab-2ed6-4039-8385-2e25cfd2aa35",
        "uuid": "3f81d6d6-8bda-40a6-b43f-8a7d8c0d63ef",
        "node_name": "attila",
        "props": [
          {
            "value": "7",
            "key": "PeerSlots"
          }
        ],
        "rsc_dfn_uuid": "41eb00e5-bff7-4c14-8dbb-76d28fd815ee",
        "name": "bill2000"
      },
      {
        "vlms": [
          {
            "meta_disk": "internal",
            "device_path": "/dev/drbd1003",
            "vlm_nr": 0,
            "stor_pool_name": "thin",
            "stor_pool_uuid": "921af4e0-ff6d-43d6-b56a-a3f8cd45678f",
            "vlm_minor_nr": 1003,
            "backing_disk": "/dev/drbdpool/bill2000_00000",
            "vlm_uuid": "ce628247-3a1f-4596-8dde-d8407399329a",
            "vlm_props": [
              {
                "value": "bill",
                "key": "RestoreFromResource"
              },
              {
                "value": "bill-snap",
                "key": "RestoreFromSnapshot"
              },
              {
                "value": "thin",
                "key": "StorPoolName"
              }
            ],
            "vlm_dfn_uuid": "8bc9bba2-10c5-4a25-9dd1-07c977f089ce"
          }
        ],
        "node_uuid": "10f01093-2516-4d30-bc8d-a7b1ab5e72b2",
        "uuid": "a885348a-d57d-4fef-b15c-91867308ef62",
        "node_name": "boudicca",
        "props": [
          {
            "value": "7",
            "key": "PeerSlots"
          }
        ],
        "rsc_dfn_uuid": "41eb00e5-bff7-4c14-8dbb-76d28fd815ee",
        "name": "bill2000"
      },
      {
        "vlms": [
          {
            "meta_disk": "internal",
            "device_path": "/dev/drbd1009",
            "vlm_nr": 1,
            "stor_pool_name": "thin",
            "stor_pool_uuid": "254472cf-fad9-4d0b-a57b-f783c40ac179",
            "vlm_minor_nr": 1009,
            "backing_disk": "/dev/drbdpool/bill2000_00009",
            "vlm_uuid": "babd12e8-a6c7-438e-b5e0-3d460c34d86d",
            "vlm_props": [
              {
                "value": "bill",
                "key": "RestoreFromResource"
              },
              {
                "value": "bill-snap",
                "key": "RestoreFromSnapshot"
              },
              {
                "value": "thin",
                "key": "StorPoolName"
              }
            ],
            "vlm_dfn_uuid": "8bc9bba2-10c5-4a25-9dd1-07c977f089ce"
          },
          {
            "meta_disk": "internal",
            "device_path": "/dev/drbd1003",
            "vlm_nr": 0,
            "stor_pool_name": "thin",
            "stor_pool_uuid": "254472cf-fad9-4d0b-a57b-f783c40ac179",
            "vlm_minor_nr": 1003,
            "backing_disk": "/dev/drbdpool/bill2000_00000",
            "vlm_uuid": "babd12e8-a6c7-438e-b5e0-3d460c34d86d",
            "vlm_props": [
              {
                "value": "bill",
                "key": "RestoreFromResource"
              },
              {
                "value": "bill-snap",
                "key": "RestoreFromSnapshot"
              },
              {
                "value": "thin",
                "key": "StorPoolName"
              }
            ],
            "vlm_dfn_uuid": "8bc9bba2-10c5-4a25-9dd1-07c977f089ce"
          }
        ],
        "node_uuid": "172da4c8-250a-468f-bc0c-f4a4fd5d8d04",
        "uuid": "8eaad34b-eea5-4988-8193-71282109173c",
        "node_name": "charlemagne",
        "props": [
          {
            "value": "7",
            "key": "PeerSlots"
          }
        ],
        "rsc_dfn_uuid": "41eb00e5-bff7-4c14-8dbb-76d28fd815ee",
        "name": "bill2000"
      }
    ]
  }
]
"""

INTERFACE_DATA = """
[
  {
    "nodes": [
      {
        "connection_status": 2,
        "uuid": "9198fcab-2ed6-4039-8385-2e25cfd2aa35",
        "net_interfaces": [
          {
            "address": "192.168.6.193",
            "uuid": "bb679899-01fc-4ba6-8485-05e0426074b7",
            "name": "default"
          }
        ],
        "props": [
          {
            "value": "default",
            "key": "CurStltConnName"
          }
        ],
        "type": "SATELLITE",
        "name": "attila"
      },
      {
        "connection_status": 2,
        "uuid": "10f01093-2516-4d30-bc8d-a7b1ab5e72b2",
        "net_interfaces": [
          {
            "address": "192.168.6.192",
            "uuid": "b34eff00-3eb0-49cf-b6a2-ebf4056e20fb",
            "name": "default"
          }
        ],
        "props": [
          {
            "value": "default",
            "key": "CurStltConnName"
          }
        ],
        "type": "SATELLITE",
        "name": "boudicca"
      },
      {
        "connection_status": 2,
        "uuid": "172da4c8-250a-468f-bc0c-f4a4fd5d8d04",
        "net_interfaces": [
          {
            "address": "192.168.6.191",
            "uuid": "d94c7bfe-9117-4bcd-831e-745ca78ca5ec",
            "name": "default"
          }
        ],
        "props": [
          {
            "value": "default",
            "key": "CurStltConnName"
          }
        ],
        "type": "SATELLITE",
        "name": "charlemagne"
      },
      {
        "connection_status": 0,
        "uuid": "c78d312b-77a1-44f2-802f-ca0dac78e0ba",
        "net_interfaces": [
          {
            "address": "192.168.6.190",
            "uuid": "8e9e4cdd-9241-4b4d-ba12-ea6100dbc33b",
            "name": "default"
          }
        ],
        "props": [
          {
            "value": "default",
            "key": "CurStltConnName"
          }
        ],
        "type": "CONTROLLER",
        "name": "vercingetorix"
      }
    ]
  }
]
"""


def test_path():
    res = resource.Resource(name="bill")
    res.path = NODE_DATA
    assert res.path == "/dev/drbd1000"

    res = resource.Resource(name="bill2000")
    res.path = NODE_DATA
    assert res.path == "/dev/drbd1003"


def test_deployment_nodes():
    res = resource.Resource(name="bill")
    assert set(res._deployed_nodes(json.loads(NODE_DATA)[0]["resources"])) == set(
        ["charlemagne", "boudicca", "attila"]
    )


def test_get_node_interface():
    res = resource.Resource(name="bill")
    assert res._get_node_interface(INTERFACE_DATA, "vercingetorix") == "192.168.6.190"
