#!/usr/bin/python
import os
from dateutil.parser import parse


def read_properties():
    try:
        azkaban_job_prop_file = os.environ["JOB_PROP_FILE"]
        azkaban_job_out_prop_file = os.environ["JOB_OUTPUT_PROP_FILE"]
    except KeyError:
        return None

    with open(azkaban_job_prop_file) as f:
        content = f.readlines()
    d = [x.strip().split("=") for x in content]
    dict = {}
    for item in d:
        if len(item) == 2:
            dict[item[0]] = item[1]

    dict['azkaban.flow.start.timestamp'] = parse(
        dict['azkaban.flow.start.timestamp'].replace("\\", "")[:25])

    print ('JOB_NAME:%s '%dict['azkaban.job.id'])

    return dict,azkaban_job_out_prop_file

