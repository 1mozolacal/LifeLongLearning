/** @param {NS} ns */

export async function main(ns) {

    let [machine, contract] = ns.args
    let data = ns.codingcontract.getData(contract, machine)
    let answer = 0

    //Soltuion here

    const reward = ns.codingcontract.attempt(answer, contract, machine)
    if (reward) {
        ns.tprint(`Contract solved successfully! Reward: ${reward}`)
    } else ns.tprint(`Failed to solve contract.Type: XXXXX\nAnswer: ${answer}\nData: ${data}`)

}