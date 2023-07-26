import { findMachinesFromHome } from '/utils.js'

let sinceLastRebalance = 0
let rebalanceFrequency = 10 * 1000
let fastRebalance = false

let target = 'n00dles'

let ratio = {
    'hack': 1,
    'weaken': 2,
    'grow': 10
}
let nextRatio = {
    'hack': 'weaken',
    'weaken': 'grow',
    'grow': 'hack'
}
let adding = 'hack'
let addingAmount = ratio[adding]
let scripts = {
    'hack': 'hacking/hack.js',
    'weaken': 'hacking/weaken.js',
    'grow': 'hacking/grow.js'
}

/** @param {import("../.").NS } ns */
export async function main(ns) {

    while (true) {


        if (Date.now() - sinceLastRebalance > rebalanceFrequency || fastRebalance) {
            fastRebalance = false

            //check if target should be changed

            //hack new machines
            const machines = findMachinesFromHome(ns)
            const hackedMachines = []
            machines.forEach(machine => {
                if (!ns.getServer(machine).hasAdminRights) {
                    if (hackMachine(ns, machine) > 0) {
                        hackedMachines.push(machine)
                    }
                } else if (machine != 'home') {
                    hackedMachines.push(machine)
                }
            })

            //Add the ratio amount to machines
            hackedMachines.forEach(machine => {
                const spareRam = ns.getServerMaxRam(machine) - ns.getServerUsedRam(machine)
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
                    fastRebalance = true
                }
            })

        }


        await ns.sleep(100)
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