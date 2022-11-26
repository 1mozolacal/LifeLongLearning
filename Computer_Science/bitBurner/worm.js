/** @param {NS} ns */
import { findMachinesFromHome, hackMachine } from 'utils.js'

export async function main(ns) {

    const target = ns.args.length > 0 ? ns.args[0] : 'n00dles'
    const machines = findMachinesFromHome(ns)
    machines.forEach(machine => {
        hackMachine(ns, machine, 'general-hack.js', target)
    })
}