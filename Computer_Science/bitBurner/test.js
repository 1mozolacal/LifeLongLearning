import { findMachinesFromHome, formatMoney } from 'utils/utils.js'


export async function main(ns) {
    ns.scriptKill('hacking/hack-master.js', 'home')
    const othersMachines = findMachinesFromHome(ns)
    othersMachines.forEach(async (machine) => {
        ns.scriptKill('hacking/hack.js', machine)
        ns.scriptKill('hacking/grow.js', machine)
        ns.scriptKill('hacking/weaken.js', machine)
    })
    await ns.sleep(100)
}