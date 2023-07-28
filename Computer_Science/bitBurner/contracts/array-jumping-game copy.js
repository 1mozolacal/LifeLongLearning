

/** @param {import("../.").NS } ns */
export async function main(ns) {

    let [machine, contract] = ns.args
    let data = ns.codingcontract.getData(contract, machine)
    let answer = 0

    // let exploreSpots = [0]
    // let explored = [0]
    // while (exploreSpots.length > 0) {
    //     const currentSpot = exploreSpots.pop()
    //     const currentValue = data[currentSpot]
    //     if (currentSpot + currentValue >= data.length - 1) {
    //         answer = 1
    //         break;
    //     }
    //     for (let i = currentSpot + 1; i <= currentSpot + currentValue; i++) {
    //         if (!(explored.includes(i))) {
    //             explored.push(i)
    //             exploreSpots.push(i)
    //         }
    //     }
    // }



    const reward = ns.codingcontract.attempt(answer, contract, machine)
    if (reward) {
        ns.tprint(`Contract solved successfully! Reward: ${reward}`)
    } else {
        ns.tprint(`Failed to solve contract.Type: Array Jumping Game\nAnswer: ${answer}\nData: ${data}`)
        ns.alert("Failed a Array Jumping Game Contract! ")
    }

}

/*
Array Jumping Game II
You are attempting to solve a Coding Contract. You have 3 tries remaining, after which the contract will self-destruct.


You are given the following array of integers:

1,2,3,2,3,1,0,3,1,3,5,3,4,3,1,4

Each element in the array represents your MAXIMUM jump length at that position. This means that if you are at position i and your maximum jump length is n, you can jump to any position from i to i+n.

Assuming you are initially positioned at the start of the array, determine the minimum number of jumps to reach the end of the array.

If it's impossible to reach the end, then the answer should be 0.*/