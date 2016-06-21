# -*- coding: utf-8 -*-
"""
Created on Tue May  3 17:16:16 2016

@author: guadalupecasuso
"""# Copyright (c) Microsoft Corporation.  All rights reserved.

"""End to end test.
"""


import pydocumentdb.document_client as document_client

masterKey = 'z1LJzktmyrZyWaYlKQM4laSYvYiVdY3tDQ5faiIkB2MJavDXxt4mc0M6zLCwvdkAfdiBOVuopxPvwBOOX0qePA=='
host = 'https://drones.documents.azure.com:443/'


client = document_client.DocumentClient(host,{'masterKey': masterKey})
databases = list(client.ReadDatabases())

    