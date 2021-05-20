#!/bin/bash

sudo podman run --name grafana -p 3000:3000 -d grafana/grafana:latest
