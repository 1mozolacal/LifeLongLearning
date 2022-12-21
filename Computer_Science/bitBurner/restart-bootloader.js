/** @param {NS} ns */
import { getTopMachineForLevel } from 'utils.js'
export async function main(ns) {


    const turnOffHacknet = 2000000//2 mill
    const turnOnStocks = 10000000//10mill

    const alertFlags = {}

    ns.exec('worm2.js', 'home', 1, 'n00dles')
    const hacknetPID = ns.exec('maintainHacknet.js', 'home')
    await ns.asleep(1000)
    const noodlesPID = ns.exec('general-hack.js', 'home', Math.floor((ns.getServerMaxRam('home') - ns.getServerUsedRam('home') - 100) / ns.getScriptRam('general-hack.js')), 'n00dles')

    while (true) {
        let playerCash = ns.getPlayer().money
        if (playerCash > turnOffHacknet && !('hacknet' in alertFlags)) {
            ns.alert("Turning hacknet upgrades off")
            alertFlags['hacknet'] = true
            ns.kill(hacknetPID)
        }
        if (playerCash > turnOnStocks && !('stock' in alertFlags)) {
            ns.alert("Turning on the stocks machine, brrrr")
            alertFlags['stock'] = true
            ns.kill(noodlesPID)
            ns.exec('stock-long.js', 'home')
            const newTarget = getTopMachineForLevel(ns, Math.floor(ns.getHackingLevel() / 2)) || 'n00dles'
            ns.exec('worm2.js', 'home', 1, newTarget)
            await ns.sleep(100)
            ns.exec('general-hack.js', 'home', Math.floor((ns.getServerMaxRam('home') - ns.getServerUsedRam('home') - 100) / ns.getScriptRam('general-hack.js')), newTarget)
        }

        if ('stock' in alertFlags && 'hacknet' in alertFlags) {
            break;
        }

        await ns.asleep(10000)
    }

}