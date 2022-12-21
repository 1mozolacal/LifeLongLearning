/** @param {NS} ns */
export async function main(ns) {


    if (!ns.stock.hasWSEAccount()) {
        const bought = ns.stock.purchaseWseAccount()
        if (!bought) {
            exit("you need a WSE Account")
        }
    }
    if (!ns.stock.hasTIXAPIAccess()) {
        const bought = ns.stock.purchaseTixApi()
        if (!bought) {
            exit("you need TIX API")
        }
    }
    if (!ns.stock.has4SDataTIXAPI()) {
        const bought = ns.stock.purchase4SMarketDataTixApi()
        if (!bought) {
            exit("you need 4S API")
        }
    }


}