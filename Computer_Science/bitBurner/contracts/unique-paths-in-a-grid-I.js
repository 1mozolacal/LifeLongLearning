/** @param {NS} ns */

export async function main(ns) {

    let [machine, contract] = ns.args
    let data = ns.codingcontract.getData(contract, machine)
    let answer = 0

    let [columns, rows] = data
    let memo = Array(rows).fill().map(() => Array(columns));
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < columns; c++) {
            if (r == 0 || c == 0) {
                memo[r][c] = 1
            } else {
                memo[r][c] = memo[r - 1][c] + memo[r][c - 1]
            }
        }
    }
    answer = memo[rows - 1][columns - 1]

    const reward = ns.codingcontract.attempt(answer, contract, machine)
    if (reward) {
        ns.tprint(`Contract solved successfully! Reward: ${reward}`)
    } else ns.tprint(`Failed to solve contract.Type: XXXXX\nAnswer: ${answer}\nData: ${data}`)

}