#!/bin/bash

gunicorn obs.wsgi:application --config obs/gunicorn.conf.py
