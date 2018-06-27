from charmhelpers.core.hookenv import (
    action_fail,
    action_set,
)

import charms.osm
from charms.reactive import (
    when,
    when_not,
    set_flag,
    clear_flag,
)

#####################
# Operational Logic #
#####################


def vnf_reboot():
    """Reboot the VNF."""

    # Implement your operational logic here.

    # It could be as simple as calling `reboot` or you may need to perform
    # multiple steps to safely remove the VNF from production. Execute
    # each step here.

    # Return either STATE_SUCCESS or STATE_FAIL and a status message.
    return (charms.osm.STATE_SUCCESS, "Not supported.")


def vnf_restart():
    """Reboot the VNF."""

    # Implement your operational logic here.

    # It could be as simple as calling `stopping` and `starting` your VNF,
    # or you may need to perform other steps. Execute those step here.

    state, _ = vnf_stop()
    if state == charms.osm.STATE_SUCCESS:
        state, _ = vnf_start()
        if state == charms.osm.STATE_SUCCESS:
            return (charms.osm.STATE_SUCCESS, "VNF Restarted")

    return (charms.osm.STATE_FAIL, "VNF restart failed")


def vnf_start():
    """Start the VNF."""

    # Implement your operational logic here.

    # It could be as simple as starting a service or you may need to perform
    # multiple steps to safely start the VNF. Execute those step here.

    # Return either STATE_SUCCESS or STATE_FAIL and a status message.
    return (charms.osm.STATE_SUCCESS, "Not supported.")


def vnf_stop():
    """Stop the VNF."""

    # Implement your operational logic here.

    # It could be as simple as stopping a service or you may need to perform
    # multiple steps to safely remove the VNF from production. Execute
    # each step here.

    # Return either STATE_SUCCESS or STATE_FAIL and a status message.
    return (charms.osm.STATE_SUCCESS, "Not supported.")


def vnf_upgrade():
    """Uprade the VNF software."""

    # Implement your operational logic here.

    # If your VNF supports inline software upgrades, you can perform the steps
    # to do that here.

    # Return either STATE_SUCCESS or STATE_FAIL and a status message.
    return (charms.osm.STATE_SUCCESS, "Not supported.")


#########
# Hooks #
#########

@when_not('osm-base.installed')
def install_osm_base():
    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #
    set_flag('osm-base.installed')


###################
# Action Handlers #
###################

@when('actions.reboot')
def action_reboot():
    state = ''
    status = ''
    try:
        state, status = vnf_reboot()

    except Exception as e:
        # If any exception happens within the action execution, we'll capture
        # it and report it via `action_fail`. Normal errors within the
        # execution of your operational logic should be caught, the state
        # should be set to STATE_FAIL and returned with a meaningful status.
        action_fail('Primitive failed: {} ({})'.format(e))
    else:
        # Send the state and a status message to the operator.
        action_set({'state': state, 'status': status})

        # If we're in a FAIL state, call action_fail to maintain compatibility
        # with charms not specific to OSM.
        if state == charms.osm.STATE_FAIL:
            action_fail('Primitive failed.')
    finally:
        clear_flag('actions.reboot')


@when('actions.start')
def action_start():
    state = ''
    status = ''
    try:
        state, status = vnf_start()
    except Exception as e:
        # If any exception happens within the action execution, we'll capture
        # it and report it via `action_fail`. Normal errors within the
        # execution of your operational logic should be caught, the state
        # should be set to STATE_FAIL and returned with a meaningful status.
        action_fail('Primitive failed: {} ({})'.format(e))
    else:
        # Send the state and a status message to the operator.
        action_set({'state': state, 'status': status})

        # If we're in a FAIL state, call action_fail to maintain compatibility
        # with charms not specific to OSM.
        if state == charms.osm.STATE_FAIL:
            action_fail('Primitive failed.')
    finally:
        clear_flag('actions.start')


@when('actions.stop')
def action_stop():
    state = ''
    status = ''
    try:
        state, status = vnf_stop()
    except Exception as e:
        # If any exception happens within the action execution, we'll capture
        # it and report it via `action_fail`. Normal errors within the
        # execution of your operational logic should be caught, the state
        # should be set to STATE_FAIL and returned with a meaningful status.
        action_fail('Primitive failed: {} ({})'.format(e))
    else:
        # Send the state and a status message to the operator.
        action_set({'state': state, 'status': status})

        # If we're in a FAIL state, call action_fail to maintain compatibility
        # with charms not specific to OSM.
        if state == charms.osm.STATE_FAIL:
            action_fail('Primitive failed.')
    finally:
        clear_flag('actions.stop')


@when('actions.restart')
def action_restart():
    state = ''
    status = ''
    try:
        state, status = vnf_restart()
    except Exception as e:
        # If any exception happens within the action execution, we'll capture
        # it and report it via `action_fail`. Normal errors within the
        # execution of your operational logic should be caught, the state
        # should be set to STATE_FAIL and returned with a meaningful status.
        action_fail('Primitive failed: {} ({})'.format(e))
    else:
        # Send the state and a status message to the operator.
        action_set({'state': state, 'status': status})

        # If we're in a FAIL state, call action_fail to maintain compatibility
        # with charms not specific to OSM.
        if state == charms.osm.STATE_FAIL:
            action_fail('Primitive failed.')
    finally:
        clear_flag('actions.restart')


@when('actions.upgrade')
def action_upgrade():
    state = ''
    status = ''
    try:
        state, status = vnf_upgrade()
    except Exception as e:
        # If any exception happens within the action execution, we'll capture
        # it and report it via `action_fail`. Normal errors within the
        # execution of your operational logic should be caught, the state
        # should be set to STATE_FAIL and returned with a meaningful status.
        action_fail('Primitive failed: {} ({})'.format(e))
    else:
        # Send the state and a status message to the operator.
        action_set({'state': state, 'status': status})

        # If we're in a FAIL state, call action_fail to maintain compatibility
        # with charms not specific to OSM.
        if state == charms.osm.STATE_FAIL:
            action_fail('Primitive failed.')
    finally:
        clear_flag('actions.upgrade')
