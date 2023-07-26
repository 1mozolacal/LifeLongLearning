
/** @param {NS} ns */
export async function main(ns) {


    const turnOffHacknet = 100000//0.1 mill
    const turnOnStocks = 10000000//10mill

    const alertFlags = {}

    const hacknetPID = ns.exec('maintainHacknet.js', 'home')
    const masterHackerPID = ns.exec('hacking/hack-master.js', 'home')
    await ns.asleep(1000)

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
            ns.exec('stocks/stock-long.js', 'home')
            await ns.sleep(100)
        }

        if ('stock' in alertFlags && 'hacknet' in alertFlags) {
            break;
        }

        await ns.asleep(10000)
    }

}