# Overview

This is the base layer for creating a Juju Charm compatible with Open Source Mano (OSM).

Charms written to be used with OSM follow a specific pattern that allow for better integration into

- Primitives are executed via [Juju Actions]
- A charm may manage the configuration of an application running on a different host, commonly referred to as a "proxy charm".

# Usage

To create an OSM charm:

```bash
$ charm create -t osm my-charm
```

## Deployment and Scale out

When OSM deploys charms, it is assigned a name that corresponds with the VNFs unique id.

When operating as a "proxy charm", there is a 1:1 relationship between a deployed application in Juju and a Virtual Machine managed by OSM. When a VNF is scaled up, it's associated charm is re-deployed under a new alias.

Non-proxy charms are scaled as usual with Juju; additional units are added to the application.

## Known Limitations and Issues


# Configuration


# Contact Information


## Upstream Project Name

  - Upstream website
  - Upstream bug tracker
  - Upstream mailing list or contact information
  - Feel free to add things if it's useful for users
