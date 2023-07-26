

/** @param {import("../.").NS } ns */
export async function main(ns) {

    let [machine, contract] = ns.args
    let data = ns.codingcontract.getData(contract, machine)
    let answer = 0

    let exploreSpots = [0]
    let explored = [0]
    while (exploreSpots.length > 0) {
        const currentSpot = exploreSpots.pop()
        const currentValue = data[currentSpot]
        if (currentSpot + currentValue >= data.length - 1) {
            answer = 1
            break;
        }
        for (let i = currentSpot + 1; i <= currentSpot + currentValue; i++) {
            if (!(explored.includes(i))) {
                explored.push(i)
                exploreSpots.push(i)
            }
        }
    }

    const reward = ns.codingcontract.attempt(answer, contract, machine)
    if (reward) {
        ns.tprint(`Contract solved successfully! Reward: ${reward}`)
    } else {
        ns.tprint(`Failed to solve contract.Type: Array Jumping Game\nAnswer: ${answer}\nData: ${data}`)
        ns.alert("Failed a Array Jumping Game Contract! ")
    }

}