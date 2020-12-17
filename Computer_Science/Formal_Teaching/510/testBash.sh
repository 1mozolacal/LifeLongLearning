#!/bin/bash
sqlplus64 "CMOZOLA/02099122@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle.scs.ryerson.ca)(Port=1521))(CONNECT_DATA=(SID=orcl)))" @"test"
sleep 3
