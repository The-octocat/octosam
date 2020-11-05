# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StorageProfile(Model):
    """Storage Profile properties of a server.

    :param backup_retention_days: Backup retention days for the server.
    :type backup_retention_days: int
    :param geo_redundant_backup: Enable Geo-redundant or not for server
     backup. Possible values include: 'Enabled', 'Disabled'
    :type geo_redundant_backup: str or
     ~azure.mgmt.rdbms.postgresql.models.GeoRedundantBackup
    :param storage_mb: Max storage allowed for a server.
    :type storage_mb: int
    """

    _attribute_map = {
        'backup_retention_days': {'key': 'backupRetentionDays', 'type': 'int'},
        'geo_redundant_backup': {'key': 'geoRedundantBackup', 'type': 'str'},
        'storage_mb': {'key': 'storageMB', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(StorageProfile, self).__init__(**kwargs)
        self.backup_retention_days = kwargs.get('backup_retention_days', None)
        self.geo_redundant_backup = kwargs.get('geo_redundant_backup', None)
        self.storage_mb = kwargs.get('storage_mb', None)
