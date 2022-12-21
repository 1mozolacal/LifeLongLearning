/** @param {NS} ns */
import { findMachinesFromHome, findServer, formatMoney } from 'utils.js'
export async function main(ns) {
    if (ns.args.lenght < 1) {
        ns.alert("You need to pass in a server name")
    } else {
        ns.alert("" + findServer(ns, ns.args[0]))
    }

}