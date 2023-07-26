import { findMachinesFromHome } from 'utils/utils.js'

/** @param {NS} ns */
export async function main(ns) {


    const otherMachines = findMachinesFromHome(ns)
    for (let machine of otherMachines) {
        const contracts = ns.ls(machine, '.cct')

        for (let contract of contracts) {
            let contractType = ns.codingcontract.getContractType(contract, machine)
            switch (contractType) {
                case "Array Jumping Game":
                    ns.run("contracts/array-jumping-game.js", 1, machine, contract)
                    break;
                case "Algorithmic Stock Trader I":
                    ns.run("contracts/algorithmic-stock-trader-I.js", 1, machine, contract)
                    break;
                default:
                    ns.alert("Does not have solution for >" + contractType + "<")
            }
        }
    }

}

/*

Sanitize Parentheses in Expression
Algorithmic Stock Trader I
Encryption II: Vigenère Cipher
Find Largest Prime Factor
*/


// neo-net: contract-101727.cct
// the-hub: contract-598727.cct
// summit-uni: contract-429021.cct
// catalyst: contract-125092.cct
// helios: contract-809503.cct
