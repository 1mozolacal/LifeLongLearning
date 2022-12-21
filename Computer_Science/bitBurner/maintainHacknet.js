/** @param {NS} ns */
export async function main(ns) {

    var spent = 0;

    var minCash = 0
    if (ns.args.length > 0) {
        minCash = ns.args[0]
    }
    var upgradeFrequency = 500
    if (ns.args.length > 1) {
        upgradeFrequency = ns.args[1]
    }
    var quickBuy = true


    while (true) {

        var cheapestUpgrade = null //[n,type,amount]
        for (var node = 0; node < ns.hacknet.numNodes(); node++) {
            var level = ns.hacknet.getLevelUpgradeCost(node, 1)
            var ram = ns.hacknet.getRamUpgradeCost(node, 1)
            var core = ns.hacknet.getCoreUpgradeCost(node, 1)
            var buy = ns.hacknet.getPurchaseNodeCost(node, 1)

            if (cheapestUpgrade == null || level < cheapestUpgrade[2]) {
                cheapestUpgrade = [node, 'level', level]
            }
            if (cheapestUpgrade == null || ram < cheapestUpgrade[2]) {
                cheapestUpgrade = [node, 'ram', ram]
            }
            if (cheapestUpgrade == null || core < cheapestUpgrade[2]) {
                cheapestUpgrade = [node, 'core', core]
            }
            if (cheapestUpgrade == null || buy < cheapestUpgrade[2]) {
                cheapestUpgrade = [node, 'buy', buy]
            }
        }
        if (cheapestUpgrade == null) {
            cheapestUpgrade = [0, 'buy', 0]
        }

        if (ns.getPlayer().money > cheapestUpgrade[2] + minCash) {
            var upgradeType = cheapestUpgrade[1]
            var upgradeNode = cheapestUpgrade[0]
            if (upgradeType === 'level') {
                ns.hacknet.upgradeLevel(upgradeNode, 1)
                spent += cheapestUpgrade[2]
                ns.print("Bought level for " + upgradeNode)
            } else if (upgradeType === 'ram') {
                ns.hacknet.upgradeRam(upgradeNode, 1)
                spent += cheapestUpgrade[2]
                ns.print("Bought ram for " + upgradeNode)
            } else if (upgradeType === 'core') {
                ns.hacknet.upgradeCore(upgradeNode, 1)
                spent += cheapestUpgrade[2]
                ns.print("Bought core for " + upgradeNode)
            } else if (upgradeType === 'buy') {
                ns.hacknet.purchaseNode()
            }
        } else {
            ns.print("can't afford purcahse of " + cheapestUpgrade[1] + ' for ' + cheapestUpgrade[0] + ' in the amount of ' + cheapestUpgrade[2])
        }

        ns.print("total spent:" + spent)
        if (quickBuy && cheapestUpgrade[2] * 100 < ns.getPlayer().money) {
            await ns.sleep(10)
        } else {
            await ns.sleep(upgradeFrequency)
        }
    }

}