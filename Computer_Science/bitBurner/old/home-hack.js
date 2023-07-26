/** @param {NS} ns */
import { canHackMachine, hackMachine } from 'utils/utils.js'
export async function main(ns) {

    const target = ns.args.length == 0 ?
        getTopMachineForLevel(ns, Math.floor(ns.getHackingLevel() / 2)) || 'n00dles' :
        ns.args[0]

    const extraRam = ns.args.length > 1 ? ns.args[1] : 100

    if (!canHackMachine(ns, target)) {
        ns.alert("Can't hack this machine")
        ns.exit()
    } else if (canHackMachine(ns, target) && !ns.hasRootAccess(target)) {
        hackMachine(ns, target)
    }

    ns.scriptKill('general-hack.js', 'home')

    ns.exec('general-hack.js',
        'home',
        Math.floor((ns.getServerMaxRam('home') - ns.getServerUsedRam('home') - extraRam) / ns.getScriptRam('general-hack.js')),
        target)

}