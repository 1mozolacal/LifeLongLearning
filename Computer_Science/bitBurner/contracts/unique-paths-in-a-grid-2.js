

/** @param {import(".").NS } ns */
export default async function solve(ns) {

    const otherMachines = findMachinesFromHome(ns)
    for (let machine of otherMachines) {
        const contracts = ns.ls(machine, '.cct')

        for (let contract of contracts) {

        }
    }

}