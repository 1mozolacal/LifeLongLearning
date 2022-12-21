/** @param {NS} ns */
import { findMachinesFromHome } from 'utils.js'

export async function main(ns) {


    const otherMachines = findMachinesFromHome(ns)
    for (let machine of otherMachines) {
        const contracts = ns.ls(machine, '.cct')

        for (let contract of contracts) {

        }
    }

}