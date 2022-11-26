/** @param {NS} ns */
export async function main(ns) {
    if (ns.args.length > 0) {
        while (true) {
            for (var i = 0; i < ns.args.length; i++) {

                var targetServer = ns.args[i]
                if (ns.getServerMinSecurityLevel(targetServer) + 5 < ns.getServerSecurityLevel(targetServer)) {
                    await ns.weaken(targetServer)
                } else if (ns.getServerMaxMoney(targetServer) * 0.75 > ns.getServerMoneyAvailable(targetServer)) {
                    await ns.grow(targetServer)
                } else {
                    await ns.hack(ns.args[i]);
                }
            }
        }
    }
}