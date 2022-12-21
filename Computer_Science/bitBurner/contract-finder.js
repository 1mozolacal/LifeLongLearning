/** @param {NS} ns */
import { findMachinesFromHome } from 'utils.js'

export async function main(ns) {


    const otherMachines = findMachinesFromHome(ns)
    let count = 5
    for (let machine of otherMachines) {
        const files = ns.ls(machine, '.cct')

        if (files.length > 0) {
            ns.alert("Contract(s) found on " + machine + ": " + files.join(' <> '))
            count -= 1
        }
        if (count <= 0) {
            ns.alert("hidden reset of occurances")
            break
        }
    }

}