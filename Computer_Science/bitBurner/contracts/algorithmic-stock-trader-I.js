/** @param {NS} ns */
export async function main(ns) {

    let [machine, contract] = ns.args
    let data = ns.codingcontract.getData(contract, machine)
    let answer = 0

    let nextHighest = Array(data.length - 1)
    nextHighest[nextHighest.length - 1] = data[data.length - 1]
    for (let i = nextHighest.length - 2; i >= 0; i--) {
        nextHighest[i] = Math.max(data[i + 1], nextHighest[i + 1])
    }

    let mostProfit = 0
    for (let i = 0; i < nextHighest.length; i++) {
        const profit = nextHighest[i] - data[i]
        mostProfit = Math.max(mostProfit, profit)
    }
    answer = mostProfit

    const reward = ns.codingcontract.attempt(answer, contract, machine)
    if (reward) {
        ns.tprint(`Contract solved successfully! Reward: ${reward}`)
    } else ns.tprint(`Failed to solve contract.Type: Algorithmic Stock Trader I\nAnswer: ${answer}\nData: ${data}`)

}