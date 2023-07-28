import { findMachinesFromHome, formatMoney } from 'utils/utils.js'

let target = ''
let targetServer = ''
let sellTarget = 0
const logFile = 'blind-long-log.txt'

/** @param {NS} ns */
export async function main(ns) {
    await ns.write(logFile, 'Staring...\n', 'w')
    while (true) {

        if (target == '') {
            const [newTarget, _, newTargetServer] = await findNextStock(ns)
            ns.alert(`first pos >${newTarget}<`)
            await maxBuy(ns, newTarget)
            await stopHacking(ns)
            await growPosition(ns, newTargetServer)
            target = newTarget
            targetServer = newTargetServer
            sellTarget = 0
            await ns.write(logFile, `Started on ${target}\n`)
        } else if (ns.getServerMoneyAvailable(targetServer) > 0.9 * ns.getServerMaxMoney(targetServer)) {
            if (sellTarget > ns.stock.getBidPrice(target)) {
                const [newTarget, _, newTargetServer] = await findNextStock(ns)
                await maxSell(ns, target)
                await maxBuy(ns, newTarget)
                await stopHacking(ns)
                await growPosition(ns, newTargetServer)
                target = newTarget
                targetServer = newTargetServer
                sellTarget = 0
                await ns.write(logFile, `Switching to ${target}\n`)
            } else {
                sellTarget = (sellTarget + ns.stock.getBidPrice(target)) / 2
                ns.write(logFile, `Waiting on good sell price for ${target} - ${sellTarget}; Currently at ${ns.stock.getBidPrice(target)}\n`)
                await ns.sleep(60 * 1000)
            }

        } else {
            ns.write(logFile, `Growing ${target} - ${Math.round(ns.getServerMoneyAvailable(targetServer) / ns.getServerMaxMoney(targetServer) * 100)}% - ${ns.stock.getBidPrice(target)}\n`)
            await ns.sleep(24 * 1000)
        }

        await ns.sleep(10)
    }

}


/** @param {NS} ns */
async function findNextStock(ns) {
    let symbols = getMap()

    let selected = []
    let topLevel = 0
    for (const index in symbols) {
        const ele = symbols[index]
        const [stock, english, server] = ele
        if (ns.getServerRequiredHackingLevel(server) < ns.getHackingLevel()
            && ns.getServerMoneyAvailable(server) < 0.6 * ns.getServerMaxMoney(server)) {
            if (ns.getServerRequiredHackingLevel(server) > topLevel) {
                topLevel = ns.getServerRequiredHackingLevel(server)
                selected = ele
            }
            await ns.write(logFile, `Possible selection:${ele} ${formatMoney(ns.stock.getMaxShares(stock) * ns.stock.getBidPrice(stock))}\n`)
        }
    }

    if (selected.length == 0) {
        ns.alert("Can't find server to grow. Shutting down blind long script.")
        ns.exit()
    }
    return selected
}

function getMap() {

    var symbolMap = [
        ["AERO", "AeroCorp", "aerocorp"],
        ["APHE", "Alpha Enterprises", "alpha-ent"],
        ["BLD", "Blade Industries", "blade"],
        ["CLRK", "Clarke Incorporated", "clarkinc"],
        // ["CTK", "CompuTek", "comptek"], not found
        ["CTYS", "Catalyst Ventures", "catalyst"],
        ["DCOMM", "DefComm", "defcomm"],
        ["ECP", "ECorp", "ecorp"],
        ["FLCM", "Fulcrum Technologies", "fulcrumassets"],
        ["FNS", "FoodNStuff", "foodnstuff"],
        ["FSIG", "Four Sigma", "4sigma"],
        ["GPH", "Global Pharmaceuticals", "global-pharm"],
        ["HLS", "Helios Labs", "helios"],
        ["ICRS", "Icarus Microsystems", "icarus"],
        ["JGN", "Joe's Guns", "joesguns"],
        ["KGI", "KuaiGong International", "kuai-gong"],
        ["LXO", "LexoCorp", "lexo-corp"],
        ["MDYN", "Microdyne Technologies", "microdyne"],
        ["MGCP", "MegaCorp", "megacorp"],
        ["NTLK", "NetLink Technologies", "netlink"],
        ["NVMD", "Nova Medical", "nova-med"],
        ["OMGA", "Omega Software", "omega-net"],
        ["OMN", "Omnia Cybersystems", "omnia"],
        ["OMTK", "OmniTek Incorporated", "omnitek"],
        ["RHOC", "Rho Contruction", "rho-construction"],
        ["SGC", "Sigma Cosmetics", "sigma-cosmetics"],
        ["SLRS", "Solaris Space Systems", "solaris"],
        ["STM", "Storm Technologies", "stormtech"],
        ["SYSC", "SysCore Securities", "syscore"],
        ["TITN", "Titan Laboratories", "titan-labs"],
        ["UNV", "Universal Energy", "univ-energy"],
        ["VITA", "VitaLife", "vitalife"],
        // ["WDS","Watchdog Security",""] doesn't have a server
    ];

    return symbolMap;

}


/** @param {NS} ns */
async function stopHacking(ns) {
    ns.scriptKill('hacking/hack-master.js', 'home')
    const othersMachines = findMachinesFromHome(ns)
    othersMachines.forEach(async (machine) => {
        ns.scriptKill('hacking/hack.js', machine)
        ns.scriptKill('hacking/grow.js', machine)
        ns.scriptKill('hacking/weaken.js', machine)
    })
    await ns.sleep(100)
}

/** @param {NS} ns */
async function growPosition(ns, buy) {

    let target = buy

    let ratio = {
        'weaken': 2,
        'grow': 10
    }
    let nextRatio = {
        'weaken': 'grow',
        'grow': 'weaken'
    }
    let adding = 'weaken'
    let addingAmount = ratio[adding]
    let scripts = {
        'hack': 'hacking/hack.js',
        'weaken': 'hacking/weaken.js',
        'grow': 'hacking/grow.js'
    }
    const machines = findMachinesFromHome(ns)
    const hackedMachines = []
    machines.forEach(machine => {
        if (!ns.getServer(machine).hasAdminRights) {
            if (hackMachine(ns, machine) > 0) {
                hackedMachines.push(machine)
            }
        } else {
            hackedMachines.push(machine)
        }
    })
    for (let times = 0; times < 10; times++) {//10 times just to fill up servers
        hackedMachines.forEach(machine => {
            let spareRam = ns.getServerMaxRam(machine) - ns.getServerUsedRam(machine)
            if (machine == 'home') {
                spareRam -= 10//save room for other programs
            }
            const script = scripts[adding]

            const threads = Math.min(addingAmount, Math.floor(spareRam / ns.getScriptRam(script, 'home')))
            if (threads > 0) {
                ns.scp(script, machine, 'home')
                ns.exec(script, machine, threads, target)
                addingAmount -= threads
                if (addingAmount <= 0) {
                    adding = nextRatio[adding]
                    addingAmount = ratio[adding]
                }
            }

        })
    }
}

function hackMachine(ns, machine) {
    /*
    This will try to nuke the provided machine when upload a mining script
    */
    const attacks = {
        "BruteSSH.exe": ns.brutessh,
        "FTPCrack.exe": ns.ftpcrack,
        "relaySMTP.exe": ns.relaysmtp,
        "HTTPWorm.exe": ns.httpworm,
        "SQLInject.exe": ns.sqlinject
    }
    if (ns.getServerRequiredHackingLevel(machine) > ns.getHackingLevel()) {
        //too unskilled 
        return -1
    }
    var attackAmount = 0
    Object.entries(attacks).forEach(att => {
        const [file, func] = att
        if (ns.fileExists(file, 'home')) {
            attackAmount += 1
            func(machine)
        }
    })
    if (ns.getServerNumPortsRequired(machine) <= attackAmount) {
        ns.nuke(machine)
        return 1
    } else {
        //can't open enough ports
        return -2
    }
}

/** @param {NS} ns */
async function maxBuy(ns, buy) {
    const buyAmount = Math.min(Math.floor((ns.getPlayer().money - 100000) / (1.1 * ns.stock.getAskPrice(buy))), ns.stock.getMaxShares(buy))
    const priceBought = ns.stock.buyStock(buy, buyAmount)
    await ns.write(logFile, `${buy} - Bought ${buyAmount} at ${priceBought}\n`)
    await ns.sleep(100)
}

/** @param {NS} ns */
async function maxSell(ns, sell) {
    ns.stock.sellStock(sell, ns.stock.getPosition(sell)[0])
    await ns.sleep(100)
}