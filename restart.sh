#!/bin/sh
psql -f del_exam.sql -d postgres
psql -f exam.sql -d postgres
python3 fill.py
