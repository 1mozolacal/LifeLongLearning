/** @param {NS} ns */
import { findMachinesFromHome, hackMachine, formatMoney } from 'utils/utils.js'

export async function main(ns) {
    var topMachine = null
    const machines = findMachinesFromHome(ns)
    machines.forEach(machine => {
        if (ns.getServerRequiredHackingLevel(machine) < ns.getHackingLevel()) {
            if (topMachine == null || ns.getServerMaxMoney(topMachine) < ns.getServerMaxMoney(machine)) {
                topMachine = machine
            }
        }
    })
    if (topMachine == null) {
        ns.alert("You can't hack anything")
    } else {
        ns.alert(`The top machine you can hack is ${topMachine} with value of ${formatMoney(ns.getServerMaxMoney(topMachine))} `
            + `with security of ${ns.getServerMinSecurityLevel(topMachine)}.\nCurrent Money is ${formatMoney(ns.getServerMoneyAvailable(topMachine))} `
            + `current security is ${ns.getServerSecurityLevel(topMachine)}`)
    }
}