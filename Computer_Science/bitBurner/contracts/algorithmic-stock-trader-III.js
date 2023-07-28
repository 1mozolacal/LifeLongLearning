/** @param {NS} ns */
export async function main(ns) {

    let [machine, contract] = ns.args
    let data = ns.codingcontract.getData(contract, machine)
    let answer = 0

    if (data.length < 4) {
        answer = stockOne(data)
    } else {
        for (let i = 1; i < data.length - 2; i++) {
            const batchProfits = stockOne(data.slice(0, i + 1)) + stockOne(data.slice(i))
            answer = Math.max(batchProfits, answer)
        }
    }

    const reward = ns.codingcontract.attempt(answer, contract, machine)
    if (reward) {
        ns.tprint(`Contract solved successfully! Reward: ${reward}`)
    } else ns.tprint(`Failed to solve contract.Type: Algorithmic Stock Trader I\nAnswer: ${answer}\nData: ${data}`)

}

function stockOne(data) {
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
    return mostProfit
}