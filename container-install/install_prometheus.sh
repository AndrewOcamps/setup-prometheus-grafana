#!/bin/bash

sudo podman run --name prometheus -p 9090:9090 -v prometheus.yml:/etc/prometheus/prometheus.yml -d prom/prometheus
