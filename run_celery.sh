#!/bin/bash

su -m djuser -c "celery worker -A boil_project.celery -l info -Q default -n default@%h"