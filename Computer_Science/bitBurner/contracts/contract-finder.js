import { findMachinesFromHome } from 'utils/utils.js'

/** @param {NS} ns */
export async function main(ns) {


    const otherMachines = findMachinesFromHome(ns)
    let count = 10
    for (let machine of otherMachines) {
        const files = ns.ls(machine, '.cct')

        if (files.length > 0) {
            ns.alert("Contract(s) found on " + machine + ": \n" + files.map(ele => {
                return `${ele} - ${ns.codingcontract.getContractType(ele, machine)}`
            }).join('\n'))
            count -= 1
        }
        if (count <= 0) {
            ns.alert("hidden reset of occurances")
            break
        }
    }

}