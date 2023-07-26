export function findServer(ns, machine) {
    let results = dfs(ns, 'home', machine, { 'home': true })
    if (results) {
        return results.reverse()
    } else {
        return "Not found."
    }
}

function dfs(ns, current, target, visited) {
    if (current == target) {
        return [current]
    }
    const connections = ns.scan(current)


    for (let ele of connections) {
        if (!(ele in visited)) {
            visited[ele] = true
            var status = dfs(ns, ele, target, visited)
            if (status) {
                status.push(current)
                return status
            }
        }
    }
    return false
}

export function hackMachine(ns, machine, script, target) {
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
        ns.print("Too unskilled for " + machine)
        return
    }
    var attackAmount = 0
    Object.entries(attacks).forEach(att => {
        const [file, func] = att
        ns.print(att)
        if (ns.fileExists(file, 'home')) {
            attackAmount += 1
            func(machine)
        }
    })
    if (ns.getServerNumPortsRequired(machine) <= attackAmount) {
        ns.nuke(machine)
    } else {
        ns.print("Can't open enough ports for " + machine)
        return
    }
    //install virus
    var threads = Math.floor(ns.getServerMaxRam(machine) / ns.getScriptRam(script, 'home'))
    if (threads > 0) {
        ns.scp(script, machine, 'home')
        ns.killall(machine, true)
        ns.exec(script, machine, threads, target)
    } else {
        ns.print("NOT enough ram!")
        return
    }


}


export function findMachinesFromHome(ns) {
    /*
    This function will preform a breath first seach to 
    find all nodes connected to home. It is returns all
    server names in an array.
    */
    var foundMachines = { 'home': true }
    var scanQueue = ['home']
    while (scanQueue.length != 0) {
        findMachinesHelper(ns, foundMachines, scanQueue)
    }
    return Object.entries(foundMachines).map(ele => {
        const [key, value] = ele
        return key
    })
}

function findMachinesHelper(ns, inputFound, inputQueue) {
    /*
    inputFound is an dictionary
    inputQueue is a array
    NOTE: has side effects
    */
    if (inputQueue.lenght == 0) {
        ns.print("No more nodes to explore")
        ns.exit()
    }
    var scanOn = inputQueue[0]
    inputQueue.splice(0, 1)

    var newNodes = ns.scan(scanOn)
    var hackNodes = []
    newNodes.forEach(ele => {
        if (!(ele in inputFound)) {
            inputFound[ele] = true
            hackNodes.push(ele)
            ns.print("FOUND: " + ele)
        }
    })

    inputQueue.push(...hackNodes)
    return hackNodes
}

export function formatMoney(money) {
    const mapping = [
        ["Trillion", 1000000000000],
        ["Billion", 1000000000],
        ["Milltion", 1000000],
        ["Thousand", 1000],
    ]
    for (let pair of mapping) {
        var [name, amount] = pair
        if (money > amount) {
            return (money / amount).toFixed(2).toString() + " " + name
        }
    }
    return money
}